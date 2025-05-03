# Description: Contains the connection to the plants database herbs collection
# and all of the functions to get information about various herbs
# Notes: 
# File: herbs.py

from app.core.database import getDB
from fastapi import APIRouter
from pymongo import MongoClient

# FastAPI Router
router = APIRouter()

# Database and Collection
db = getDB("plants")
herbs = db["herbs"]

# Helper function to fetch an herb by name
def get_herb(name: str):
    return herbs.find_one({"Herb": name}, {"_id": 0})

# Get all herbs
@router.get("/getHerbs")
def getHerbs():
    herbs_list = list(herbs.find({}, {"_id": 0}))
    return {"herbs": herbs_list}

# Get an herb by its name
@router.get("/getHerb")
def getHerb(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb

# Get the scientific name of an herb
@router.get("/getHerbScientific")
def getScientific(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Scientific_Name", f"No scientific name available for {name}")

# Get the zone(s) for an herb
@router.get("/getHerbZone")
def getZone(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Zones", f"No zone information available for {name}")

# Get the planting season(s) for an herb
@router.get("/getHerbSeasons")
def getSeasons(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return {
        "Spring": herb.get("Planting_Season_Spring", False),
        "Summer": herb.get("Planting_Season_Summer", False),
        "Fall": herb.get("Planting_Season_Fall", False),
        "Winter": herb.get("Planting_Season_Winter", False),
    }

# Get the planting time(s) for an herb
@router.get("/getHerbPlantingTimes")
def getPlantingTimes(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return {
        "Spring": herb.get("Planting_Time_Spring"),
        "Summer": herb.get("Planting_Time_Summer"),
        "Fall": herb.get("Planting_Time_Fall"),
        "Winter": herb.get("Planting_Time_Winter"),
    }

# Get the maturity time for an herb
@router.get("/getHerbMaturityTime")
def getMaturityTime(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Maturity_Time", f"No maturity time available for {name}")

# Get the germination time for an herb
@router.get("/getHerbGerminationTime")
def getGerminationTime(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Germination_Time", f"No germination time available for {name}")

# Get the harvest time(s) for an herb
@router.get("/getHerbHarvestTimes")
def getHarvestTimes(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return {
        "Spring": herb.get("Harvest_Time_Spring"),
        "Summer": herb.get("Harvest_Time_Summer"),
        "Fall": herb.get("Harvest_Time_Fall"),
        "Winter": herb.get("Harvest_Time_Winter"),
    }

# Get the temperature range for an herb
@router.get("/getHerbTemperatureRange")
def getTemperatureRange(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Temperature_Range", f"No temperature range available for {name}")

# Get the light requirements for an herb
@router.get("/getHerbLightRequirements")
def getLightRequirements(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Light_Requirements", f"No light requirements available for {name}")

# Get the watering needs for an herb
@router.get("/getHerbWateringNeeds")
def getWateringNeeds(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Watering_Needs", f"No watering needs available for {name}")

# Get the fertilizer needs for an herb
@router.get("/getHerbFertilizerNeeds")
def getFertilizerNeeds(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Fertilizer_Needs", f"No fertilizer needs available for {name}")

# Get the pruning needs for an herb
@router.get("/getHerbPruningNeeds")
def getPruningNeeds(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Pruning_Needs", f"No pruning needs available for {name}")

# Get the soil type for an herb
@router.get("/getHerbSoilType")
def getSoilType(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Soil_Type", f"No soil type available for {name}")

# Get the soil pH for an herb
@router.get("/getHerbSoilPH")
def getSoilPH(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Soil_pH", f"No soil pH available for {name}")

# Get the pest management tips for an herb
@router.get("/getHerbPestManagement")
def getPestManagement(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Pest_Management", f"No pest management information available for {name}")

# Get the disease management tips for an herb
@router.get("/getHerbDiseaseManagement")
def getDiseaseManagement(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Disease_Management", f"No disease management information available for {name}")

# Get the companion plants for an herb
@router.get("/getHerbCompanionPlants")
def getCompanionPlants(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Companion_Plants", f"No companion plants available for {name}")

# Get the regional tips for an herb
@router.get("/getHerbRegionalTips")
def getRegionalTips(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Regional_Tips", f"No regional tips available for {name}")

# Get the special instructions for an herb
@router.get("/getHerbSpecialInstructions")
def getSpecialInstructions(name: str):
    herb = get_herb(name)
    if not herb:
        return {"error": "Herb not found"}
    return herb.get("Special_Instructions", f"No special instructions available for {name}")