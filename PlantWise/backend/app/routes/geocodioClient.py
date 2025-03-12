# Description: Contains the connection to the Geocodio API and the GeocodioClient
# and all of the functions to get information about various locations.
# Notes:
# File: geocodioClient.py

# FOR TESTING PURPOSES ONLY
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Import the necessary modules
from app.core.keys import getGeocodioKey
import asyncio
from fastapi import APIRouter
from geocodio import GeocodioClient

# FastAPI Router
router = APIRouter()

# Geocodio API URL and Key
GEOCODIO_API_URL = "https://api.geocod.io/v1.7/geocode"
GEOCODIO_API_KEY = getGeocodioKey()

# Geocodio Client
client = GeocodioClient(GEOCODIO_API_KEY)

# Get the coordinates of an address
@router.get("/address")
async def getAddressCoordinates(address: str):
    location = client.geocode(address)
    
    # Extract some of the location data so we can use it for other purposes
    locationData = {
        "zipcode": location['results'][0]['address_components']["zip"],
        "latitude": location.coords[0],
        "longitude": location.coords[1]
    }
    return locationData

# Get the coordinates of a city
@router.get("/city")
async def getCityCoordinates(city: str):
    data = {
        "city": city
    }
    location = client.geocode(city)
    
    locationInfo = {
        "zipcode": location['results'][0]['address_components']["zip"],
        "latitude": location.coords[0],
        "longitude": location.coords[1]
    }
    return locationInfo

# Get the coordinates of a zipcode
@router.get("/zipcode")
async def getZipCoordinates(zipcode: str):
    data = {
        "postal_code": zipcode
    }
    location = client.geocode(data)
    
    # Extract some of the location data so we can use it for other purposes
    locationInfo = {
        "zipcode": zipcode,
        "latitude": location.coords["postal_code"][0],
        "longitude": location.coords["postal_code"][1]
    }
    return locationInfo

# FOR TESTING PURPOSES ONLY
# Test the Geocodio API connection and get the coordinates of a zip code and an address
async def main():
    add = await getAddressCoordinates("1301 Sheridan Ave, Chico CA 95926")
    print(f'Coordinates for 1301 Sheridan Ave, Chico CA 95926: {add}')
    city = await getCityCoordinates("Chico")
    print(f'Coordinates for Chico: {city}')
    zip = await getZipCoordinates("95926")
    print('Coordinates for 95926: {zip}')
    
if __name__ == "__main__":
    asyncio.run(main())