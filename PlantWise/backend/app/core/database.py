# Description: PlantWise MongoDB connection
# Notes: 
# File: database.py

import os
from fastapi import APIRouter
from pymongo import MongoClient

# FastAPI Router
router = APIRouter()

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)

# Returns a database object by name
def getDB(dbName: str):
    return client[dbName]

# Check the connection to the MongoDB client
@router.get("/checkDB")
def checkClient():
    return client.server_info()