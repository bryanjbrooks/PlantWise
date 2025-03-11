# Description: Contains the function to calculate the last frost date
# for each year for a given location (by zip code) and to insert that data into the database.
# Notes: Assumes weather data dates are in ISO format "YYYY-MM-DD".
# File: lastFrost.py

from app.core.database import getDB
from app.core.weatherHistory import getWeatherData
from fastapi import APIRouter
from pymongo import MongoClient
from datetime import datetime

# FastAPI Router
router = APIRouter()

# Database for last frost dates
lastFrostDB = getDB("lastFrost")

# Collection for storing last frost dates by year
lastFrostCollection = lastFrostDB["lastFrostDates"]

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

# Get the average last frost date (month and day) for a given zip code
@router.get("/getAverageLastFrostDate")
def getAverageLastFrostDate(zipCode: str):
    # Retrieve documents for this zip code (each document has fields "zipCode", "year", and "lastFrostDate")
    docs = list(lastFrostCollection.find({"zipCode": zipCode}, {"_id": 0, "lastFrostDate": 1}))
    if not docs:
        return {"error": "No last frost data found for this location."}

    totalDayOfYear = 0
    count = 0

    for doc in docs:
        dateStr = doc.get("lastFrostDate")
        try:
            dt = datetime.strptime(dateStr, "%Y-%m-%d")
        except Exception as e:
            continue  # Skip any invalid date formats
        dayOfYear = dt.timetuple().tm_yday
        totalDayOfYear += dayOfYear
        count += 1

    if count == 0:
        return {"error": "No valid frost dates found."}

    # Calculate the average day of the year (as an integer)
    avgDay = int(round(totalDayOfYear / count))

    # Convert the average day-of-year back to a date in a reference non-leap year (e.g., 2021)
    referenceYear = 2021  # A non-leap year for consistency
    avgDate = datetime(referenceYear, 1, 1) + timedelta(days=avgDay - 1)
    avgDateStr = avgDate.strftime("%m-%d")  # Returns a string like "04-15"

    return {"zipCode": zipCode, "averageLastFrostDate": avgDateStr}
