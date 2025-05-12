from app.core.database import getDB
from fastapi import APIRouter
from pymongo import MongoClient

# FastAPI Router
router = APIRouter()

# Future Weather Database
weather = getDB("futureWeather")

@router.post("/addDailyFutureWeather")
def addDailyFutureWeather(zipCode: str, date: str, daily: dict):
    # If the collection exists, delete it to make way for the most updated forecast
    if checkFutureWeatherCollection(zipCode):
        weather[zipCode].drop()

    # Create collection if it doesn't exist
    weather.create_collection(zipCode)

    # Insert daily weather data
    collection = weather[zipCode]
    return {"insertedId": str(collection.insert_one(daily).inserted_id)}

# Add multiple days of weather data
@router.post("/addMultipleFutureDailyWeather")
def addMultipleDailyFutureWeather(zipCode: str, data: list):
    if not checkFutureWeatherCollection(zipCode):
        weather.create_collection(zipCode)
    else:
        weather[zipCode].drop()
        weather.create_collection(zipCode)

    # Get the collection for the given zip code
    collection = weather[zipCode]

    # Get all existing dates
    existingDates = set(doc["date"] for doc in collection.find({}, {"date": 1}))
    newData = [doc for doc in data if doc["date"] not in existingDates]

    # If there's no new data to insert, return a message
    if not newData:
        return {"message": "No new weather data to insert."}

    # Insert the new data into the collection
    collection.insert_many(newData)
    return {"message": f"Inserted {len(newData)} new weather records."}


# Check if the collection (zip code) already exists
@router.get("/checkFutureWeatherCollection")
def checkFutureWeatherCollection(zipCode: str):
    return zipCode in weather.list_collection_names()

# Check the future weather for frost
@router.get("/checkFutureWeather")
def checkFutureWeather(zipCode: str):
    # Check if the collection exists
    if not checkFutureWeatherCollection(zipCode):  # Fixed: Call checkFutureWeatherCollection
        return {"error": "Future weather for this location not found"}

    # Get the collection for the given zip code
    collection = weather[zipCode]

    # Retrieve all documents from the collection
    data = list(collection.find({}, {"_id": 0}))

    # Check the minimum temperature for each day
    frost_days = []
    for record in data:
        if "min" in record and record["min"] <= 32:  # Assuming 32°F as the frost threshold
            frost_days.append(record["date"])

    # Get or create the frostDays collection
    frost_days_collection = weather["frostDays"]

    # Create or update the document for the given zipCode
    frost_days_collection.update_one(
        {"_id": zipCode},  # Use zipCode as the document ID
        {"$set": {"frostDays": frost_days}},  # Update the frostDays field
        upsert=True  # Insert the document if it doesn't exist
    )

    # Return a message based on whether frost days were found
    if frost_days:
        return {"message": f"Frost days for {zipCode} have been updated.", "frostDays": frost_days}
    else:
        return {"message": f"No frost days found for {zipCode}.", "frostDays": []}

# Get the frost days for future weather
@router.get("/getFutureFrostDays")
def getFutureFrostDays(zipCode: str):
    # Get the frostDays collection
    frost_days_collection = weather["frostDays"]

    # Try to find the document for the given zipCode
    doc = frost_days_collection.find_one({"_id": zipCode}, {"_id": 0})

    # If the document does not exist, check future weather and update the collection
    if not doc:
        if not checkFutureWeatherCollection(zipCode):
            return {"error": "No future weather data found for this location."}

        # Generate frost days by calling checkFutureWeather
        checkFutureWeather(zipCode)

        # Try to retrieve the document again
        doc = frost_days_collection.find_one({"_id": zipCode}, {"_id": 0})

        # If the document still doesn't exist, return an error
        if not doc:
            return {"error": "No frost days data found for this location."}

    # Return the frost days document
    return doc