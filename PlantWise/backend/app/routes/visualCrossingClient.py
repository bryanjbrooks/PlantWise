# Description: This file contains the routes for the Visual Crossing API.
# Notes: See documentation for license information.
# File: openWeatherClient.py

# FOR TESTING PURPOSES ONLY
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Import the necessary modules
from app.core.keys import getVisualCrossingKey
from app.core.weatherHistory import addDailyWeather, addMultipleDailyWeather, checkWeatherCollection
from app.core.frostDates import calculateFrostDates, getAverageFrostDates
import asyncio
from datetime import datetime, timedelta
from fastapi import APIRouter
import httpx
# We need this to run synchronous database operations in asynchronous code
from starlette.concurrency import run_in_threadpool

# FastAPI Router
router = APIRouter()

# Visual Crossing API URL
VISUAL_CROSSING_API_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

# Visual Crossing API Key
VISUAL_CROSSING_API_KEY = getVisualCrossingKey()

# Get weather data for a location on a specific date
@router.get("/weather")
async def getWeatherData(lat: float, long: float, date: str, zipCode: str):
    requestURL = f"{VISUAL_CROSSING_API_URL}{lat},{long}/{date}?unitGroup=us&key={VISUAL_CROSSING_API_KEY}&contentType=json"

    async with httpx.AsyncClient() as client:
        response = await client.get(requestURL)
        responseData = response.json()
        
    # Extract the relevant data from the response
    minTemp = responseData["days"][0]["tempmin"]

    # Build the daily weather data
    daily = {
        "date": date,
        "min": minTemp
    }
    
    # Extract the relevant data from the response
    # cloudCover = responseData["days"][0]["cloudcover"]
    # humidity = responseData["days"][0]["humidity"]
    # precip = responseData["days"][0]["precip"]
    # minTemp = responseData["days"][0]["tempmin"]
    # maxTemp = responseData["days"][0]["tempmax"]
    # pressure = responseData["days"][0]["pressure"]  
    # maxWindSpeed = responseData["days"][0]["windspeed"]
    # maxWindDirection = responseData["days"][0]["winddir"]

    # Run the synchronous function in a threadpool so it doesn't block the event loop
    result = await run_in_threadpool(addDailyWeather, zipCode, date, daily)
    return daily  # includes both date and minTemp

    
@router.get("/historicalWeather")
async def getHistoricalWeatherData(lat: float, long: float, zipCode: str, years: int = 30):
    endDate = datetime.now() - timedelta(days=1)
    startDate = datetime(endDate.year - years, 1, 1)
    allResults = []

    print(f'Start Date: {startDate}')
    print(f'End Date: {endDate}')

    # Loop through each year
    for year in range(startDate.year, endDate.year + 1):
        yearStart = datetime(year, 1, 1).strftime("%Y-%m-%d")
        yearEnd = datetime(year, 12, 31).strftime("%Y-%m-%d")
        requestURL = f"{VISUAL_CROSSING_API_URL}{lat},{long}/{yearStart}/{yearEnd}?unitGroup=us&key={VISUAL_CROSSING_API_KEY}&contentType=json"

        async with httpx.AsyncClient() as client:
            response = await client.get(requestURL)
            if response.status_code == 200:
                responseData = response.json()
                # Extract only the date and tempmin for each day
                for day in responseData.get("days", []):
                    allResults.append({
                        "date": day["datetime"],
                        "min": day["tempmin"]
                    })
            else:
                print(f"Failed to fetch data for year {year}: {response.status_code}")

        # Pause to avoid hitting API rate limits
        await asyncio.sleep(1)

    print(f"Total days of data retrieved: {len(allResults)}")

    # Write the data to the database
    result = await run_in_threadpool(addMultipleDailyWeather, zipCode, allResults)
    print(f"Data written to database: {result}")
    return allResults

    
# THIS IS FOR TESTING PURPOSES ONLY
# Test the OpenWeather API connection and get the historical weather data for 95926
async def main():
    print("Getting historical weather for 95926...\nThis may take a while...")
    start = time.time()
    res = await getHistoricalWeatherData(39.746027, -121.836171, "95926")
    elapsed = time.time() - start
    print(res)
    print(f"Execution time: {elapsed:.2f} seconds")
    # print("Getting weather data for 95926 on 2025-03-11...")
    # res = await getWeatherData(39.746027, -121.836171, "2025-03-11", "95926")
    print(res)
    res2 = calculateFrostDates("95926")
    print(f'\n{res2}')
    res3 = getAverageFrostDates("95926")
    print(f'\n{res3}')

if __name__ == "__main__":
    asyncio.run(main())