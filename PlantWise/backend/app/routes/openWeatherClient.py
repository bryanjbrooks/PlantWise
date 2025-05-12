# Description: This file contains the routes for the OpenWeather API.
# Notes: See documentation for license information.
# File: openWeatherClient.py

# FOR TESTING PURPOSES ONLY
import sys
import time
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Import the necessary modules
from app.core.keys import getOpenWeatherKey
from app.core.keys import getOpenWeatherKey2
from app.core.futureWeather import addMultipleDailyFutureWeather, getFutureFrostDays
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

# OpenWeather API URL for historical weather
OPENWEATHER_API_URL = "https://api.openweathermap.org/data/3.0/onecall/day_summary?"
# OpenWeather API URL for future weather
OPENWEATHER_API_URL2 = "https://api.openweathermap.org/data/2.5/forecast/daily?"

# OpenWeather API Keys
OPENWEATHER_API_KEY = getOpenWeatherKey()
OPENWEATHER_API_KEY2 = getOpenWeatherKey2()

# Get weather data for a location on a specific date
@router.get("/weather")
async def getWeatherData(lat: float, long: float, date: str, zipCode: str):
    requestURL = f"{OPENWEATHER_API_URL}lat={lat}&lon={long}&date={date}&units=imperial&appid={OPENWEATHER_API_KEY}"

    async with httpx.AsyncClient() as client:
        response = await client.get(requestURL)
        responseData = response.json()

    # Extract the relevant data from the response
    minTemp = responseData["temperature"]["min"]

    # Build the daily weather data
    daily = {
        "date": date,
        "min": minTemp
    }

    # Run the synchronous function in a threadpool so it doesn't block the event loop
    result = await run_in_threadpool(addDailyWeather, zipCode, date, daily)
    return daily  # includes both date and minTemp

# Get historical weather data for a location for the past 30 full years plus the current year
@router.get("/historicalWeather")
async def getHistoricalWeatherData(lat: float, long: float, zipCode: str, years: int = 30):
    endDate = datetime.now() - timedelta(days=1)
    startDate = datetime(endDate.year - years, 1, 1)
    allDates = []

    print(f'Start Date: {startDate}')
    print(f'End Date: {endDate}')

    # Build a list of date strings ("YYYY-MM-DD")
    currentDate = startDate
    while currentDate <= endDate:
        allDates.append(currentDate.strftime("%Y-%m-%d"))
        currentDate += timedelta(days=1)

    print(f"Total dates: {len(allDates)}")

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
        minTemp = weatherData["min"]
        temps.append({"date": dateStr, "min": minTemp})

    # Insert the batch of weather records into the database
    result = await run_in_threadpool(addMultipleDailyWeather, zipCode, temps)
    return result["message"]

# Get future weather data for a location for the next 16 days
@router.get("/futureWeather")
async def getFutureWeather(lat: float, long: float, zipCode: str):
    requestURL = f"{OPENWEATHER_API_URL2}lat={lat}&lon={long}&cnt=16&units=imperial&appid={OPENWEATHER_API_KEY2}"

    endDate = datetime.now() + timedelta(days=15)
    startDate = datetime.now()
    allDates = []

    print(f'Start Date: {startDate}')
    print(f'End Date: {endDate}')

    # Build a list of date strings ("YYYY-MM-DD")
    currentDate = startDate
    while currentDate <= endDate:
        allDates.append(currentDate.strftime("%Y-%m-%d"))
        currentDate += timedelta(days=1)

    print(f"Total dates: {len(allDates)}")

    # Get the future weather
    async with httpx.AsyncClient() as client:
        response = await client.get(requestURL)
        responseData = response.json()

    # Extract the minimum temperature for each day
    temps = []
    for day in responseData["list"]:
        dateStr = datetime.utcfromtimestamp(day["dt"]).strftime("%Y-%m-%d")
        minTemp = day["temp"]["min"]
        temps.append({"date": dateStr, "min": minTemp})

    # Insert the batch of weather records into the database
    result = await run_in_threadpool(addMultipleDailyFutureWeather, zipCode, temps)
    return {"message": result["message"], "data": temps}

    # This is for testing purposes
    # return temps


# THIS IS FOR TESTING PURPOSES ONLY
# Test the OpenWeather API connection and get the historical weather data for 95926
async def main():
    # print("Getting historical weather for 95926...\nThis may take a while...")
    # start = time.time()
    # res = await getHistoricalWeatherData(39.746027, -121.836171, "95926")
    # elapsed = time.time() - start
    # print(res)
    # print(f"Execution time: {elapsed:.2f} seconds")
    # print("Getting weather data for 95926 on 2025-03-11...")
    # res = await getWeatherData(39.746027, -121.836171, "2025-03-11", "95926")
    # print(res)
    # res2 = calculateFrostDates("95926")
    # print(f'\n{res2}')
    # res3 = getAverageFrostDates("95926")
    # print(f'\n{res3}')
    print("Getting future weather for 95926..")
    res = await getFutureWeather(39.746027, -121.836171, "95926")
    print(res)
    res2 = getFutureFrostDays("95926")
    print("Future frost dates for 95926")
    print(res2)

if __name__ == "__main__":
    asyncio.run(main())