import asyncio
from datetime import datetime, timedelta
from fastapi import APIRouter
import httpx
import math

# FOR TESTING PURPOSES ONLY
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# from app.core.database import weatherData
from app.core.keys import getNOAAKey

# FastAPI Router
router = APIRouter()

# NOAA NCEI API URL, Key & Header
NOAA_NCEI_API_URL = "https://www.ncdc.noaa.gov/cdo-web/api/v2/"
API_KEY = getNOAAKey()
header = {"token": API_KEY}

# Endpoints for NOAA API
datasets = "datasets"
dataCategories = "datacategories"
datatypes = "datatypes"
locationCategories = "locationcategories"
locations = "locations"
stations = "stations"
datas = "data"

# Function to calculate distance between two coordinates
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c  # Distance in kilometers
    return distance

# Function to fetch daily weather data from NOAA
@router.get("/searchNOAAweather")
# Asynchronous function to search for a station based on latitude and longitude
async def searchStation(latitude, longitude):
    searchUrl = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/stations'
    searchParams = {
        'latitude': latitude,
        'longitude': longitude,
        'limit': 1  # Limit to the closest station
    }
    headers = {
        'token': API_KEY
    }

    async with httpx.AsyncClient() as client:
        try:
            searchResponse = await client.get(searchUrl, params=searchParams, headers=headers, timeout=20.0)
            searchResponse.raise_for_status()  # Raise an exception for HTTP errors
        except httpx.RequestError as exc:
            print(f"An error occurred while requesting {exc.request.url!r}.")
            return None
        except httpx.HTTPStatusError as exc:
            print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
            return None

    stationData = searchResponse.json()
    print(f"Station search response: {stationData}")  # Log the response

    if 'results' in stationData and stationData['results']:
        station = stationData['results'][0]
        stationId = station['id']  # Get the station ID from the results
        stationLat = station['latitude']
        stationLon = station['longitude']
        distance = calculate_distance(latitude, longitude, stationLat, stationLon)
        print(f"Found station {stationId} at ({stationLat}, {stationLon}), distance: {distance} km")
        if distance <= 80:  # Check if the station is within 80 kilometers of the requested location
            return stationId
        else:
            print("Station is too far from the requested location.")
            return None
    else:
        print("No station found for this location.")
        return None

# Asynchronous function to get temperature data for a given station ID
async def getTemperatureData(stationId, startDate, endDate):
    dataUrl = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'

    dataParams = {
        'datasetid': 'GHCND',  # Daily Summaries dataset
        'stationid': stationId,
        'datatypeid': 'TMAX,TMIN',  # Max and Min temperatures
        'startdate': startDate,
        'enddate': endDate,
        'units': 'imperial',  # or 'imperial' if you prefer Fahrenheit
        'limit': 1000  # Adjust the limit if necessary
    }

    headers = {
        'token': API_KEY
    }

    async with httpx.AsyncClient() as client:
        try:
            dataResponse = await client.get(dataUrl, params=dataParams, headers=headers, timeout=20.0)
            dataResponse.raise_for_status()  # Raise an exception for HTTP errors
        except httpx.RequestError as exc:
            print(f"An error occurred while requesting {exc.request.url!r}.")
            return None
        except httpx.HTTPStatusError as exc:
            print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
            return None

    data = dataResponse.json()
    print(f"Temperature data response: {data}")  # Log the response

    if 'results' in data and data['results']:
        return data
    else:
        print("No temperature data found.")
        return None

# Main asynchronous function to get temperature data for a specific location (latitude and longitude)
async def getTemperatureForLocation(latitude, longitude):
    # Step 1: Search for the station ID
    stationId = await searchStation(latitude, longitude)

    if stationId:
        # Step 2: Calculate the date range for the last year
        endDate = datetime.today().strftime('%Y-%m-%d')
        startDate = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')

        # Step 3: Get the temperature data for the station
        data = await getTemperatureData(stationId, startDate, endDate)

        if data:
            print("Temperature Data:")
            print(data)  # Process or store the data as needed
        else:
            print("No temperature data found.")
            # Try searching for nearby locations with an expanded radius
            for radius in range(1, 6):  # Expand the search radius from 1 to 5 degrees
                nearby_locations = [
                    (latitude + radius * 0.1, longitude),
                    (latitude - radius * 0.1, longitude),
                    (latitude, longitude + radius * 0.1),
                    (latitude, longitude - radius * 0.1)
                ]
                for lat, lon in nearby_locations:
                    print(f"Trying nearby location: Latitude = {lat}, Longitude = {lon}")
                    stationId = await searchStation(lat, lon)
                    if stationId:
                        data = await getTemperatureData(stationId, startDate, endDate)
                        if data:
                            print("Temperature Data for nearby location:")
                            print(data)  # Process or store the data as needed
                            return
                        await asyncio.sleep(0.2)  # Wait for 200 milliseconds between requests
            print("No temperature data found for nearby locations either.")
    else:
        print("Station ID not found.")

# Main function to run the test
async def main():
    stationID = "GHCND:USC00041715"
    print(f"Fetching temperature data for station: {stationID}")
    data = await getTemperatureData(stationID, '2025-01-01', '2025-01-31')
    print(data)

# Run the main function
if __name__ == '__main__':
    asyncio.run(main())