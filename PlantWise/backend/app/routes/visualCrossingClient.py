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
@router.get("/")
async def getWeatherData(lat: float, long: float, date: str, zipCode: str):
    requestURL = f"{VISUAL_CROSSING_API_URL}{lat},{long}/{date}?unitGroup=us&key={VISUAL_CROSSING_API_KEY}&contentType=json"

    async with httpx.AsyncClient() as client:
        response = await client.get(requestURL)
        responseData = response.json()

    # Extract the relevant data from the response
    cloudCover = responseData["days"][0]["cloudcover"]
    humidity = responseData["days"][0]["humidity"]
    precip = responseData["days"][0]["precip"]
    minTemp = responseData["days"][0]["tempmin"]
    maxTemp = responseData["days"][0]["tempmax"]
    pressure = responseData["days"][0]["pressure"]  
    maxWindSpeed = responseData["days"][0]["windspeed"]
    maxWindDirection = responseData["days"][0]["winddir"]