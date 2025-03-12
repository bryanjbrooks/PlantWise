# Description: This file contains the routes for the OpenWeather API.
# Notes: See documentation for license information.
# File: openWeatherClient.py

# FOR TESTING PURPOSES ONLY
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Import the necessary modules
from app.core.keys import getOpenWeatherKey
from app.core.weatherHistory import addDailyWeather, addMultipleDailyWeather
from app.core.frostDates import calculateFrostDates, getAverageFrostDates
import asyncio
from datetime import datetime, timedelta
from fastapi import APIRouter
import httpx
# We need this to run synchronous database operations in asynchronous code
from starlette.concurrency import run_in_threadpool

# FastAPI Router
router = APIRouter()

# OpenWeather API URL
OPENWEATHER_API_URL = "https://api.openweathermap.org/data/3.0/onecall/day_summary?"

# OpenWeather API Key
OPENWEATHER_API_KEY = getOpenWeatherKey()

# Get weather data for a location on a specific date
@router.get("/weather")
async def getWeatherData(lat: float, long: float, date: str, zipCode: str):
    requestURL = f"{OPENWEATHER_API_URL}lat={lat}&lon={long}&date={date}&units=imperial&appid={OPENWEATHER_API_KEY}"

    async with httpx.AsyncClient() as client:
        response = await client.get(requestURL)
        responseData = response.json()

    # print(responseData)
    minTemp = responseData["temperature"]["min"]

    # Run the synchronous function in a threadpool so it doesn't block the event loop
    result = await run_in_threadpool(addDailyWeather, zipCode, date, minTemp)
    return {"minTemp": minTemp}  # changed from insertedId since we're already storing in threadpool

# Get historical weather data for a location for the past 6 full years plus the current year
@router.get("/historicalWeather")
async def getHistoricalWeatherData(lat: float, long: float, zipCode: str):
    endDate = datetime.now()
    startDate = datetime(2019, 1, 1)
    allDates = []

    print(f'Start Date: {startDate}')
    print(f'End Date: {endDate}')

    # Build a list of date strings ("YYYY-MM-DD")
    currentDate = startDate
    while currentDate <= endDate:
        allDates.append(currentDate.strftime("%Y-%m-%d"))
        currentDate += timedelta(days=1)

    print(len(allDates))

    batchSize = 5
    allResults = []
    allDateStrs = []

    for i in range(0, len(allDates), batchSize):
        batchDates = allDates[i:i+batchSize]
        tasks = [getWeatherData(lat, long, dateStr, zipCode) for dateStr in batchDates]
        batchResults = await asyncio.gather(*tasks)
        allResults.extend(batchResults)
        allDateStrs.extend(batchDates)
        # Pause for 1 seconds to stay within the rate limit
        await asyncio.sleep(1)

    # Combine each date with its corresponding weather data
    temps = []
    for dateStr, weatherData in zip(allDateStrs, allResults):
        minTemp = weatherData["minTemp"]
        temps.append({"date": dateStr, "min": minTemp})

    # Insert the batch of weather records into the database
    result = await run_in_threadpool(addMultipleDailyWeather, zipCode, temps)
    return result["message"]

# THIS IS FOR TESTING PURPOSES ONLY
# Test the OpenWeather API connection and get the historical weather data for 95926
async def main():
    # print("Getting historical weather for 95926...\nThis may take a while...")
    # res = await getHistoricalWeatherData(39.746027, -121.836171, "95926")
    print("Getting weather data for 95926 on 2025-03-11...")
    res = await getWeatherData(39.746027, -121.836171, "2025-03-11", "95926")
    print(res)
    res2 = calculateFrostDates("95926")
    print(f'\n{res2}')
    res3 = getAverageFrostDates("95926")
    print(f'\n{res3}')

if __name__ == "__main__":
    asyncio.run(main())