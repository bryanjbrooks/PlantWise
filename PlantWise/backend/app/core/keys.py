# Description: File to load API keys from a .env file
# Notes: 
# File: keys.py

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Functions to get the API keys
def getGeocodioKey():
    return os.getenv("GEOCODIO_API_KEY")

def getNOAAKey():
    return os.getenv("NOAA_API_KEY")

def getOpenWeatherKey():
    return os.getenv("OPENWEATHER_API_KEY")

def getOpenWeatherKey2():
    return os.getenv("OPENWEATHER_API_KEY2")

def getVisualCrossingKey():
    return os.getenv("VISUAL_CROSSING_API_KEY")