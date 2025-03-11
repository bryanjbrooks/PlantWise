# Description: Contains the connection to the plants database fruits collection
# and all of the functions to get information about various fruits.
# Notes: 
# File: fruits.py

from fastapi import APIRouter
from pymongo import MongoClient

# FastAPI Router
router = APIRouter()

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)

# Database and Collection
db = client["plants"]
fruits = db["fruits"]

# Check if the database is connected
@router.get("/checkDB")
def checkPlantsDB():
    return client.server_info()

# Get all fruits
@router.get("/getFruits")
def getFruits():
    # Ignore the MongoDB `_id` field
    return list(fruits.find({}, {"_id": 0}))

# Get a fruit by its name
@router.get("/getFruit")
def getFruit(name: str):
    return fruits.find_one({"Fruit:": name}, {"_id": 0})

# Get the zone(s) for a fruit
@router.get("/getFruitZone")
def getZone(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Zones", "No zone information available")

# Get the planting season(s) for a fruit
@router.get("/getFruitSeason")
def getSeason(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Planting_Season", "No season information available")

# Get the planting time(s) for a fruit
@router.get("/getFruitPlantingTimes")
def getTimes(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Planting_Time", "No planting time available")

# Check the special instructions for a fruit
def getInstructions(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Special_Instructions", "No special instructions available")