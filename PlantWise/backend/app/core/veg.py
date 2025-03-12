# Description: Contains the connection to the plants database vegetables 
# collection and all of the functions to get information about various
# vegetables.
# Notes: 
# File: veg.py

from app.core.database import getDB
from fastapi import APIRouter
from pymongo import MongoClient

# FastAPI Router
router = APIRouter()

# Database and Collection
db = getDB("plants")
veg = db["vegetables"]

# Get all vegetables
@router.get("/getVegetables")
def get_vegetables():
    # Exclude MongoDB `_id` field
    vegetables = list(veg.find({}, {"_id": 0}))  
    return {"vegetables": vegetables}

# Get a vegetable by its name
@router.get("/getVegetable")
def get_vegetable(name: str):
    vegetable = veg.find_one({"Vegetable": name}, {"_id": 0})
    return {"vegetable": vegetable}

# Get the zone(s) for a vegetable
@router.get("/getVegetableZone")
def get_zone(name: str):
    vegetable = get_vegetable(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return {"zone": vegetable.get("Zones", "No zone information available")}

# Get the planting season(s) for a vegetable
@router.get("/getVegetableSeason")
def get_season(name: str):
    vegetable = get_vegetable(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return {"season": vegetable.get("Planting_Season", "No season information available")}

# Get the planting time(s) for a vegetable
@router.get("/getVegetablePlantingTimes")
def get_times(name: str):
    vegetable = get_vegetable(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return {"planting_time": vegetable.get("Planting_Time", "No planting time available")}