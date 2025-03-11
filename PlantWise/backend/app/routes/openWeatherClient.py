# Description: This file contains the routes for the OpenWeather API.
# Notes: See documentation for license information.
# File: openWeatherClient.py

import asyncio
from datetime import datetime, timedelta
from fastapi import APIRouter
import httpx
# We need this to run synchronous database operations in asynchronous code
from starlette.concurrency import run_in_threadpool

# FOR TESTING PURPOSES ONLY
# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.core.keys import getOpenWeatherKey
from app.core.weatherHistory import addDailyWeather, addMultipleDailyWeather

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
    
    minTemp = responseData["temperature"]["min"]
    
    # Run the synchronous function in a threadpool so it doesn't block the event loop
    result = await run_in_threadpool(addDailyWeather, zipCode, date, minTemp)
    return {"insertedId": str(result.inserted_id)}

# Get historical weather data for a location for the past 2 years
@router.get("/historicalWeather")
async def getHistoricalWeatherData(lat: float, long: float, zipCode: str):
    endDate = datetime.now()
    startDate = endDate - timedelta(days=2*365)  # Past 2 years
    allDates = []
    
    # Build a list of date strings ("YYYY-MM-DD")
    currentDate = startDate
    while currentDate <= endDate:
        allDates.append(currentDate.strftime("%Y-%m-%d"))
        currentDate += timedelta(days=1)
        
    print(len(allDates))
    
    # batchSize = 5
    # allResults = []
    # allDateStrs = []
    
    # # Process dates in batches to respect the 5 requests per second limit
    # for i in range(0, len(allDates), batchSize):
    #     batchDates = allDates[i:i+batchSize]
    #     tasks = [getWeatherData(lat, long, dateStr, zipCode) for dateStr in batchDates]
    #     batchResults = await asyncio.gather(*tasks)
    #     allResults.extend(batchResults)
    #     allDateStrs.extend(batchDates)
    #     # Pause for 1 second to stay within the rate limit
    #     await asyncio.sleep(1)
    
    # # Combine each date with its corresponding weather data
    # temps = []
    # for dateStr, weatherData in zip(allDateStrs, allResults):
    #     minTemp = weatherData["temperature"]["min"]
    #     maxTemp = weatherData["temperature"]["max"]
    #     temps.append({"date": dateStr, "minTemp": minTemp, "maxTemp": maxTemp})
    
    # # Insert the batch of weather records into the database
    # result = await run_in_threadpool(addMultipleDailyWeather, zipCode, temps)
    # return {"insertedIds": [str(doc.inserted_id) for doc in result.inserted_ids]}

# Test the Geocodio API connection and get the coordinates of a zip code and an address
# async def main():
#     minTemp = await getHistoricalWeatherData(39.746027, -121.836171, 95926)
#     # print(type(minTemp))
#     # print(f"Minimum temperature on 2025-01-01: {minTemp}°F")
#     # minTemps = await getHistoricalWeatherData(39.746027, -121.836171)
#     # print(minTemps)

# if __name__ == "__main__":
#     asyncio.run(main())