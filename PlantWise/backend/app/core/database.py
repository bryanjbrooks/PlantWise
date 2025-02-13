### MongoDB Connection ###
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)

# Databases
weather = client["weather"]

# Database Collections
weatherData = weather["data"]