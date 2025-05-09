# Description: This file contains the routes for the Visual Crossing API.
# Notes: See documentation for license information.
# File: openWeatherClient.py

# FOR TESTING PURPOSES ONLY
import sys
import time
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
    # includes both date and minTemp, this is for testing purposes
    # return daily  
    return result["message"]

async def fetchWeatherData(url: str):
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            print(f"\nHTTP error while fetching:\n{url}")
            print(f"Status code: {e.response.status_code}")
            print(f"Response text: {e.response.text[:300]}")  # Show a snippet
        except httpx.RequestError as e:
            print(f"\nNetwork error while fetching:\n{url}")
            print(f"Details: {str(e)}")
        except Exception as e:
            print(f"\nUnexpected error while fetching:\n{url}")
            print(f"Details: {str(e)}")
        return None

@router.get("/historicalWeather")
async def getHistoricalWeatherData(lat: float, long: float, zipCode: str, years: int = 30):
    endDate = datetime.now() - timedelta(days=1)
    startDate = datetime(endDate.year - years, 1, 1)
    allResults = []

    print(f'Start Date: {startDate}')
    print(f'End Date: {endDate}')

    # 🆕 Store all URLs by year so we can retry specific ones later
    urls_by_year = {}

    # Loop through each year
    for year in range(startDate.year, endDate.year + 1):
        yearStart = datetime(year, 1, 1).strftime("%Y-%m-%d")
        yearEnd = datetime(year, 12, 31).strftime("%Y-%m-%d")
        if year == endDate.year:
            yearEnd = endDate.strftime("%Y-%m-%d")

        requestURL = f"{VISUAL_CROSSING_API_URL}{lat},{long}/{yearStart}/{yearEnd}?unitGroup=us&key={VISUAL_CROSSING_API_KEY}&include=days&contentType=json"
        print(f"Requesting data from {yearStart} to {yearEnd}")

        # Track the request URL per year for retry logic
        urls_by_year[year] = requestURL

    # Run all tasks concurrently
    tasks = [fetchWeatherData(url) for url in urls_by_year.values()]
    responses = await asyncio.gather(*tasks)

    # Process responses
    failed_years = []  # Track which years failed
    for i, (year, url) in enumerate(urls_by_year.items()):
        responseData = responses[i]
        if responseData and "days" in responseData:
            for day in responseData["days"]:
                allResults.append({
                    "date": day["datetime"],
                    "min": day["tempmin"]
                })
        else:
            print(f"Initial fetch failed for year {year}")
            failed_years.append(year)

    # Retry any failed years
    if failed_years:
        print(f"Retrying failed years: {failed_years}")
        retry_tasks = [fetchWeatherData(urls_by_year[year]) for year in failed_years]
        retry_responses = await asyncio.gather(*retry_tasks)

        for i, year in enumerate(failed_years):
            responseData = retry_responses[i]
            if responseData and "days" in responseData:
                print(f"Retry successful for year {year}")
                for day in responseData["days"]:
                    allResults.append({
                        "date": day["datetime"],
                        "min": day["tempmin"]
                    })
            else:
                print(f"Retry failed for year {year}")

    print(f"Total days of data retrieved: {len(allResults)}")

    # Write the data to the database
    result = await run_in_threadpool(addMultipleDailyWeather, zipCode, allResults)

    # Calculate the average frost dates now that we have gotten the historical weather data
    calculateFrostDates(zipCode)

    # This is for testing purposes
    # return allResults
    return result["message"]


    
# THIS IS FOR TESTING PURPOSES ONLY
# Test the OpenWeather API connection and get the historical weather data for 95926
async def main():
    # print("Getting 1 year plus the current year of historical weather for 95926...\nThis may take a while...")
    # start = time.time()
    # res = await getHistoricalWeatherData(39.746027, -121.836171, "95926")
    # elapsed = time.time() - start
    # print(res)
    # print(f"Execution time: {elapsed:.2f} seconds")
    # print("Getting 30 years plus the current year of historical weather for 940087...\nThis may take a while...")
    # start = time.time()
    # res = await getHistoricalWeatherData(37.368832, -122.036346, "94087")
    # elapsed = time.time() - start
    # print(res)
    # print(f"Execution time: {elapsed:.2f} seconds")
    # print("Getting weather data for 95926 on 2025-05-01...")
    # res = await getWeatherData(39.746027, -121.836171, "2025-05-01", "95926")
    # print(res)
    # res2 = calculateFrostDates("95926")
    # print(f'\n{res2}')
    # res3 = getAverageFrostDates("95926")
    # print(f'\n{res3}')
    # res2 = calculateFrostDates("94087")
    # print(f'\n{res2}')
    res3 = getAverageFrostDates("94087")
    print(f'\n{res3}')

if __name__ == "__main__":
    asyncio.run(main())