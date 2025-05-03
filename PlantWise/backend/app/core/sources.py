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
hz = db["hardinessZones"]
plantImages = db["plantImages"]
datesGuides = db["plantingDatesGuides"]
weather = db["weather"]

# Collections


@router.get("/hardinessZones")
def getHardinessZoneSources():
  return 