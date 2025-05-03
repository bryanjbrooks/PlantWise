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

# Helper function to fetch a vegetable by name
def get_vegetable_by_name(name: str):
    return veg.find_one({"Vegetable": name}, {"_id": 0})

# Get all vegetables
@router.get("/getVegetables")
def get_vegetables():
    vegetables = list(veg.find({}, {"_id": 0}))
    return {"vegetables": vegetables}

# Get a vegetable by its name
@router.get("/getVegetable")
def get_vegetable(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable

# Get the scientific name of a vegetable
@router.get("/getVegetableScientific")
def get_scientific(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Scientific_Name", f"No scientific name available for {name}")

# Get the zone(s) for a vegetable
@router.get("/getVegetableZone")
def get_zone(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Zones", f"No zone information available for {name}")

# Get the planting season(s) for a vegetable
@router.get("/getVegetableSeasons")
def get_seasons(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return {
        "Spring": vegetable.get("Planting_Season_Spring", False),
        "Summer": vegetable.get("Planting_Season_Summer", False),
        "Fall": vegetable.get("Planting_Season_Fall", False),
        "Winter": vegetable.get("Planting_Season_Winter", False),
    }

# Get the planting time(s) for a vegetable
@router.get("/getVegetablePlantingTimes")
def get_planting_times(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return {
        "Spring": vegetable.get("Planting_Time_Spring"),
        "Summer": vegetable.get("Planting_Time_Summer"),
        "Fall": vegetable.get("Planting_Time_Fall"),
        "Winter": vegetable.get("Planting_Time_Winter"),
    }

# Get the maturity time for a vegetable
@router.get("/getVegetableMaturityTime")
def get_maturity_time(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Maturity_Time", f"No maturity time available for {name}")

# Get the germination time for a vegetable
@router.get("/getVegetableGerminationTime")
def get_germination_time(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Germination_Time", f"No germination time available for {name}")

# Get the harvest time(s) for a vegetable
@router.get("/getVegetableHarvestTimes")
def get_harvest_times(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return {
        "Spring": vegetable.get("Harvest_Time_Spring"),
        "Summer": vegetable.get("Harvest_Time_Summer"),
        "Fall": vegetable.get("Harvest_Time_Fall"),
        "Winter": vegetable.get("Harvest_Time_Winter"),
    }

# Get the temperature range for a vegetable
@router.get("/getVegetableTemperatureRange")
def get_temperature_range(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Temperature_Range", f"No temperature range available for {name}")

# Get the light requirements for a vegetable
@router.get("/getVegetableLightRequirements")
def get_light_requirements(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Light_Requirements", f"No light requirements available for {name}")

# Get the watering needs for a vegetable
@router.get("/getVegetableWateringNeeds")
def get_watering_needs(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Watering_Needs", f"No watering needs available for {name}")

# Get the fertilizer needs for a vegetable
@router.get("/getVegetableFertilizerNeeds")
def get_fertilizer_needs(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Fertilizer_Needs", f"No fertilizer needs available for {name}")

# Get the pruning needs for a vegetable
@router.get("/getVegetablePruningNeeds")
def get_pruning_needs(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Pruning_Needs", f"No pruning needs available for {name}")

# Get the soil type for a vegetable
@router.get("/getVegetableSoilType")
def get_soil_type(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Soil_Type", f"No soil type available for {name}")

# Get the soil pH for a vegetable
@router.get("/getVegetableSoilPH")
def get_soil_ph(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Soil_pH", f"No soil pH available for {name}")

# Get the pest management tips for a vegetable
@router.get("/getVegetablePestManagement")
def get_pest_management(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Pest_Management", f"No pest management information available for {name}")

# Get the disease management tips for a vegetable
@router.get("/getVegetableDiseaseManagement")
def get_disease_management(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Disease_Management", f"No disease management information available for {name}")

# Get the companion plants for a vegetable
@router.get("/getVegetableCompanionPlants")
def get_companion_plants(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Companion_Plants", f"No companion plants available for {name}")

# Get the regional tips for a vegetable
@router.get("/getVegetableRegionalTips")
def get_regional_tips(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Regional_Tips", f"No regional tips available for {name}")

# Get the special instructions for a vegetable
@router.get("/getVegetableSpecialInstructions")
def get_special_instructions(name: str):
    vegetable = get_vegetable_by_name(name)
    if not vegetable:
        return {"error": "Vegetable not found"}
    return vegetable.get("Special_Instructions", f"No special instructions available for {name}")