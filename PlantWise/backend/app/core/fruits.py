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

# Helper function to fetch a fruit by name
def get_fruit(name: str):
    return fruits.find_one({"Fruit": name}, {"_id": 0})

# Get all fruits
@router.get("/getFruits")
def getFruits():
    return list(fruits.find({}, {"_id": 0}))

# Get a fruit by its name
@router.get("/getFruit")
def getFruit(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit

# Get the scientific name of a fruit
@router.get("/getFruitScientific")
def getScientific(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Scientific_Name", f"No scientific name available for {name}")

# Get the zone(s) for a fruit
@router.get("/getFruitZone")
def getZone(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Zones", f"No zone information available for {name}")

# Get the planting season(s) for a fruit
@router.get("/getFruitSeasons")
def getSeasons(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": f"{name} not found"}
    return {
        "Spring": fruit.get("Planting_Season_Spring", False),
        "Summer": fruit.get("Planting_Season_Summer", False),
        "Fall": fruit.get("Planting_Season_Fall", False),
        "Winter": fruit.get("Planting_Season_Winter", False),
    }

# Get the planting time(s) for a fruit
@router.get("/getFruitPlantingTimes")
def getPlantingTimes(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return {
        "Spring": fruit.get("Planting_Time_Spring"),
        "Summer": fruit.get("Planting_Time_Summer"),
        "Fall": fruit.get("Planting_Time_Fall"),
        "Winter": fruit.get("Planting_Time_Winter"),
    }

# Get the maturity time for a fruit
@router.get("/getFruitMaturityTime")
def getMaturityTime(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Maturity_Time", f"No maturity time available for {name}")

# Get the germination time for a fruit
@router.get("/getFruitGerminationTime")
def getGerminationTime(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Germination_Time", f"No germination time available for {name}")

# Get the harvest time(s) for a fruit
@router.get("/getFruitHarvestTimes")
def getHarvestTimes(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return {
        "Spring": fruit.get("Harvest_Time_Spring"),
        "Summer": fruit.get("Harvest_Time_Summer"),
        "Fall": fruit.get("Harvest_Time_Fall"),
        "Winter": fruit.get("Harvest_Time_Winter"),
    }

# Get the temperature range for a fruit
@router.get("/getFruitTemperatureRange")
def getTemperatureRange(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Temperature_Range", f"No temperature range available for {name}")

# Get the light requirements for a fruit
@router.get("/getFruitLightRequirements")
def getLightRequirements(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Light_Requirements", f"No light requirements available for {name}")

# Get the watering needs for a fruit
@router.get("/getFruitWateringNeeds")
def getWateringNeeds(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Watering_Needs", f"No watering needs available for {name}")

# Get the fertilizer needs for a fruit
@router.get("/getFruitFertilizerNeeds")
def getFertilizerNeeds(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Fertilizer_Needs", f"No fertilizer needs available for {name}")

# Get the pruning needs for a fruit
@router.get("/getFruitPruningNeeds")
def getPruningNeeds(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Pruning_Needs", f"No pruning needs available for {name}")

# Get the soil type for a fruit
@router.get("/getFruitSoilType")
def getSoilType(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Soil_Type", f"No soil type available for {name}")

# Get the soil pH for a fruit
@router.get("/getFruitSoilPH")
def getSoilPH(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Soil_pH", f"No soil pH available for {name}")

# Get the special instructions for a fruit
@router.get("/getFruitSpecialInstructions")
def getSpecialInstructions(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Special_Instructions", f"No special instructions available for {name}")

# Get the companion plants for a fruit
@router.get("/getFruitCompanionPlants")
def getCompanionPlants(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Companion_Plants", f"No companion plants available for {name}")

# Get the regional tips for a fruit
@router.get("/getFruitRegionalTips")
def getRegionalTips(name: str):
    fruit = get_fruit(name)
    if not fruit:
        return {"error": "Fruit not found"}
    return fruit.get("Regional_Tips", f"No regional tips available for {name}")