# Description: Contains all of the functions to add and retrieve historical weather data
# from the weather database.
# Notes: 
# File: weatherHistory.py

from app.core.database import getDB
from fastapi import APIRouter
from pymongo import MongoClient

# FastAPI Router
router = APIRouter()

# Weather Database
weather = getDB("weatherHistory")

# Check if the database is connected
@router.get("/checkDB")
def checkDB():
    return client.server_info()

# Check if the collection (zip code) already exists
@router.get("/checkWeatherCollection")
def checkWeatherCollection(zipCode: str):
    return zipCode in weather.list_collection_names()

# Add individual daily weather data
@router.post("/addDailyWeather")
def addDailyWeather(zipCode: str, date: str, minTemp: float):
    # Create collection if it doesn't exist
    if not checkWeatherCollection(zipCode):
        weather.create_collection(zipCode)

    # Insert daily weather data
    collection = weather[zipCode]
    daily = {
        "date": date,
        "min": minTemp
    }
    return {"insertedId": str(collection.insert_one(daily).inserted_id)}

# Add multiple days of weather data
@router.post("/addMultipleDailyWeather")
def addMultipleDailyWeather(zipCode: str, data: list):
    if not checkWeatherCollection(zipCode):
        weather.create_collection(zipCode)

    collection = weather[zipCode]
    return {"insertedIds": [str(doc.inserted_id) for doc in collection.insert_many(data).inserted_ids]}

# Get all weather data for a zip code
@router.get("/getWeatherData")
def getWeatherData(zipCode: str):
    if not checkWeatherCollection(zipCode):
        return {"error": "No weather data found for this location."}

    collection = weather[zipCode]
    data = list(collection.find({}, {"_id": 0}))
    return {"weatherData": data}

# Update weather data for a specific zip code
@router.put("/updateWeatherData")
def updateWeatherData(zipCode: str, date: str, minTemp: float):
    if not checkWeatherCollection(zipCode):
        return {"error": "No weather data found for this location."}
    
    collection = weather[zipCode]
    query = {"date": date}
    new_values = {"$set": {"min": minTemp}}
    result = collection.update_one(query, new_values)
    return {"modifiedCount": result.modified_count}