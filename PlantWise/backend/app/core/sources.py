# Description: Contains the connection to the plant and image source databases
# and all of the functions to get information about various nuts
# Notes: 
# File: nuts.py

from app.core.database import getDB
from fastapi import APIRouter
from pymongo import MongoClient

# FastAPI Router
router = APIRouter()

# Sources database
db = getDB("sources")

# Collections
hz = db["hardinessZones"]
plantImages = db["plantImages"]
datesGuides = db["plantingDatesGuides"]
weather = db["weather"]

# Collections


# Get all documents from the hardiness zones collection
@router.get("/hardinessZones")
def getHardinessZoneSources():
    return list(hz.find({}, {"_id": 0}))

# Get all documents from the plant images collection
@router.get("/plantImages")
def getPlantImageSources():
    return list(plantImages.find({}, {"_id": 0}))

# Get all documents from the planting dates guides collection
@router.get("/plantingDatesGuides")
def getPlantingDatesGuidesSources():
    return list(datesGuides.find({}, {"_id": 0}))

# Get all documents from the weather collection
@router.get("/weather")
def getWeatherSources():
    return list(weather.find({}, {"_id": 0}))