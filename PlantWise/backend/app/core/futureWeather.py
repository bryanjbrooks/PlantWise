from app.core.database import getDB
from fastapi import APIRouter
from pymongo import MongoClient

# FastAPI Router
router = APIRouter()

# Future Weather Database
db = getDB("futureWeather")

# Future Weather Collections
temps = db["temps"]

# Check if the collection (zip code) already exists
@router.get("/checkWeatherCollection")
def checkWeatherCollection(zipCode: str):
    return zipCode in db.list_collection_names()
  
def addDailyWeather(zipCode: str, date: str, daily: dict):
    # If the collection exists, delete it to make way for the most updated forecast
    if checkWeatherCollection(zip):
        db[zipCode].drop()
        # Find the temps in the temps collection
        

    # Create collection if it doesn't exist
    db.create_collection(zipCode)

    # Insert daily weather data
    collection = weather[zipCode]
    return {"insertedId": str(collection.insert_one(daily).inserted_id)}