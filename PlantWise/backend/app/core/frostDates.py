# Description: Contains the function to calculate the last frost date
# for each year for a given location (by zip code) and to insert that data into the database.
# Notes: Assumes weather data dates are in ISO format "YYYY-MM-DD".
# File: frostDates.py

from app.core.database import getDB
from app.core.weatherHistory import getWeatherData, checkWeatherCollection
from fastapi import APIRouter
from pymongo import MongoClient
from datetime import datetime, timedelta

# FastAPI Router
router = APIRouter()

# Databases for spring and fall frost dates and average frost dates
frostDatesDB = getDB("frostDates")

# Calculate the last spring and first fall frost dates for each year
@router.get("/calculateFrostDates")
def calculateFrostDates(zipCode: str):
    weatherData = getWeatherData(zipCode)
    if "error" in weatherData:
        return weatherData

    weatherRecords = weatherData["weatherData"]

    # Group by year
    recordsByYear = {}
    for record in weatherRecords:
        try:
            recordDate = datetime.strptime(record["date"], "%Y-%m-%d")
        except Exception:
            continue
        year = recordDate.year
        recordsByYear.setdefault(year, []).append(record)

    frostData = {}
    for year, records in recordsByYear.items():
        records.sort(key=lambda r: r["date"])  # oldest to newest

        spring = [r for r in records if datetime.strptime(r["date"], "%Y-%m-%d").month < 7]
        fall = [r for r in records if datetime.strptime(r["date"], "%Y-%m-%d").month >= 7]

        lastSpringFrost = None
        for r in reversed(spring):
            if r["min"] <= 32:
                lastSpringFrost = datetime.strptime(r["date"], "%Y-%m-%d").strftime("%m-%d")  # Keep only MM-DD
                break

        firstFallFrost = None
        for r in fall:
            if r["min"] <= 32:
                firstFallFrost = datetime.strptime(r["date"], "%Y-%m-%d").strftime("%m-%d")  # Keep only MM-DD
                break

        frostData[year] = {
            "lastSpringFrost": lastSpringFrost,
            "firstFallFrost": firstFallFrost
        }

        # Store in frostDates DB with collection name as zipCode
        collection = frostDatesDB[str(zipCode)]
        collection.update_one(
            {"year": year},
            {"$set": frostData[year]},
            upsert=True
        )

    # Calculate and store average frost dates
    lastSpringDates = [v["lastSpringFrost"] for v in frostData.values() if v["lastSpringFrost"]]
    firstFallDates = [v["firstFallFrost"] for v in frostData.values() if v["firstFallFrost"]]

    def computeAverage(dateStrs):
        total, count = 0, 0
        for d in dateStrs:
            try:
                dt = datetime.strptime(d, "%m-%d")
                total += dt.timetuple().tm_yday
                count += 1
            except:
                continue
        if count == 0:
            return None
        avgDay = int(round(total / count))
        avgDate = datetime(2021, 1, 1) + timedelta(days=avgDay - 1)
        return avgDate.strftime("%m-%d")  # Only store MM-DD

    avgLastSpring = computeAverage(lastSpringDates)
    avgFirstFall = computeAverage(firstFallDates)

    frostDatesDB["average"].update_one(
        {"_id": str(zipCode)},
        {"$set": {
            "lastSpringFrost": {"date": avgLastSpring},
            "firstFallFrost": {"date": avgFirstFall}
        }},
        upsert=True
    )

    return {"frostByYear": frostData, "averages": {
        "lastSpringFrost": avgLastSpring,
        "firstFallFrost": avgFirstFall
    }}

# Get average frost dates for a zip code
@router.get("/getAverageFrostDates")
def getAverageFrostDates(zipCode: str):
    collection = frostDatesDB["average"]
    doc = collection.find_one({"_id": str(zipCode)}, {"_id": 0})
    if not doc:
        # Check to see if there is historical data for this zip code
        collection = checkWeatherCollection[str(zipCode)]
        if collection:
            calculateFrostDates(zipCode)
            doc = collection.find_one({"_id": str(zipCode)}, {"_id": 0})
        else:
            return {"error": "No average frost data found for this location."}
    return doc