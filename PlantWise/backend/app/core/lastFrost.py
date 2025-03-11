# Description: This file contains the function to calculate the last frost date
# for each year for a given location (by zip code) and to insert that data into the database.
# Notes: Assumes weather data dates are in ISO format "YYYY-MM-DD".
# File: lastFrost.py

from fastapi import APIRouter
from pymongo import MongoClient
from datetime import datetime
from app.core.weatherHistory import getWeatherData  # Assumes this function returns weather data in the form {"weatherData": [...]}

# FastAPI Router
router = APIRouter()

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)

# Database for last frost dates
lastFrostDB = client["lastFrost"]

# Collection for storing last frost dates by year
lastFrostCollection = lastFrostDB["lastFrostDates"]

# Check if the database is connected
@router.get("/checkDB")
def checkDB():
    return client.server_info()

# Calculate and store the last frost date for each year for a given zip code
@router.get("/calculateLastFrostEachYear")
def calculateLastFrostEachYear(zipCode: str):
    # Retrieve weather data for the given zip code
    weatherData = getWeatherData(zipCode)
    if "error" in weatherData:
        return weatherData

    weatherRecords = weatherData["weatherData"]

    # Group weather records by year
    recordsByYear = {}
    for record in weatherRecords:
        try:
            # Parse the date (assumed format "YYYY-MM-DD")
            recordDate = datetime.strptime(record["date"], "%Y-%m-%d")
        except Exception as e:
            continue  # Skip this record if date parsing fails

        year = recordDate.year
        recordsByYear.setdefault(year, []).append(record)

    # For each year, find the last frost date (last date with min temperature <= 32°F)
    lastFrostByYear = {}
    for year, records in recordsByYear.items():
        # Sort records in descending order (latest dates first)
        records.sort(key=lambda r: r["date"], reverse=True)
        lastFrostDate = None
        for rec in records:
            if rec["min"] <= 32:
                lastFrostDate = rec["date"]
                break
        if lastFrostDate:
            lastFrostByYear[year] = lastFrostDate

    # Insert or update the last frost dates in the database
    for year, frostDate in lastFrostByYear.items():
        lastFrostCollection.update_one(
            {"zipCode": zipCode, "year": year},
            {"$set": {"lastFrostDate": frostDate}},
            upsert=True
        )

    return {"zipCode": zipCode, "lastFrostByYear": lastFrostByYear}
