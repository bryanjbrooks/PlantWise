# Description: Contains the connection to the plants database vegetables 
# collection and all of the functions to get information about various
# vegetables.
# Notes: 
# File: veg.py

from fastapi import APIRouter
from pymongo import MongoClient

# FastAPI Router
router = APIRouter()

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)

# Database and Collection
db = client["plants"]
veg = db["vegetables"]

# Check if the database is connected
@router.get("/checkDB")
def checkPlantsDB():
    return client.server_info()
  
# Get a list all vegetables
@router.get("/getVegetables")
def get_vegetables():
    # Exclude MongoDB `_id` field
    vegetables = list(veg.find({}, {"_id": 0}))  
    return {"vegetables": vegetables}