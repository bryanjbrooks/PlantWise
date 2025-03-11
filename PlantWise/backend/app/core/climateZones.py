# Description: Contains the connection to the climate database and the 
# locations collections and all of the functions to get the hardiness zones for
# a zip code.
# Notes: MongoDB does not allow leading 0's in int32 types, so the zip codes 
# are stored as strings.
# The zone and zip code data in the database is from the following source:
# https://prism.oregonstate.edu/projects/plant_hardiness_zones.php
# File: climateDB.py

from app.core.database import getDB
from fastapi import APIRouter, Query
from pymongo import MongoClient

# FastAPI Router
router = APIRouter()

# Database and Collection
db = getDB("climateZones")
us = db["US"]

# Get the USDA hardiness zone for an Alaska, Hawaii, Puerto Rico or contiguous US zip code
@router.get("/getZone")
def getZone(zip: str = Query(..., min_length=5, max_length=5)):
    return us.find_one({"zipcode": zip}, {"_id": 0})