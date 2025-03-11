# Description: Contains the connection to the plants database herbs collection
# and all of the functions to get information about various herbs
# Notes: 
# File: herbs.py

from fastapi import APIRouter
from pymongo import MongoClient

# FastAPI Router
router = APIRouter()

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)

# Database and Collection
db = client["plants"]
herbs = db["herbs"]

# Check if the database is connected
@router.get("/checkPlantsDB")
def checkPlantsDB():
    return client.server_info()

# Get all herbs
@router.get("/getHerbs")
def getHerbs():
    herbs_list = list(herbs.find({}, {"_id": 0}))  # Avoid overwriting `herbs`
    return {"herbs": herbs_list}

# Get an herb by its name
@router.get("/getHerb")
def getHerb(name: str):
    return herbs.find_one({"Herb": name}, {"_id": 0})

# Get the zone(s) for an herb
@router.get("/getHerbZone")
def getZone(name: str):
    herb = getHerb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Zones", "No zone information available")

# Get the planting season(s) for an herb
@router.get("/getHerbSeason")
def getSeason(name: str):
    herb = getHerb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Planting_Season", "No season information available")

# Get the planting time(s) for an herb
@router.get("/getHerbTimes")
def getTimes(name: str):
    herb = getHerb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Planting_Time", "No planting time available")

# Check the special instructions for an herb
@router.get("/getHerbInstructions")
def getInstructions(name: str):
    herb = getHerb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Special_Instructions", "No special instructions available")