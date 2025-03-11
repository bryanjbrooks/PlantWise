# Description: Contains the connection to the plants database fruits collection
# and all of the functions to get information about various fruits.
# Notes: 
# File: fruits.py

from app.core.database import getDB
from fastapi import APIRouter
from pymongo import MongoClient

# FastAPI Router
router = APIRouter()

# Database and Collection
db = getDB("plants")
fruits = db["fruits"]

# Get all fruits
@router.get("/getFruits")
def getFruits():
    # Ignore the MongoDB `_id` field
    return list(fruits.find({}, {"_id": 0}))

# Get a fruit by its name
@router.get("/getFruit")
def getFruit(name: str):
    return fruits.find_one({"Fruit": name}, {"_id": 0})

# Get the zone(s) for a fruit
@router.get("/getFruitZone")
def getZone(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Zones", f"No zone information available for {name}")

# Get the planting season(s) for a fruit
@router.get("/getFruitSeason")
def getSeason(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": f"{name} not found"}
    return fruit.get("Planting_Season", f"No season information available for {name}")

# Get the planting time(s) for a fruit
@router.get("/getFruitPlantingTimes")
def getTimes(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Planting_Time", f"No planting time available for {name}")

# Check the special instructions for a fruit
def getInstructions(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Special_Instructions", f"No special instructions available for {name}")