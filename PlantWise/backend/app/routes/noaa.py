import httpx
from datetime import datetime
from app.core.database import weatherData
from app.core.keys import get_noaa_key

NOAA_API_URL = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data"
API_KEY = get_noaa_key()

async def fetchStations():
    headers = {"token": API_KEY}
    
    response = httpx.get(NOAA_API_URL, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        stations = data['results']
        print(stations)
        return stations

# # Function to fetch daily weather data from NOAA
# async def fetch_noaa_weather():
#     headers = {"token": API_KEY}
    
#     # Example parameters for a daily weather query (modify as needed)
#     params = {
#         "datasetid": "GHCND",  # Daily climate data
#         "datatypeid": "TMIN",  # Example: Minimum temperature
#         "stationid": "GHCND:USW00023193",  # Station ID (e.g., New York Central Park)
#         "startdate": "2023-01-01",
#         "enddate": "2023-01-10",
#     }

#     async with httpx.AsyncClient() as client:
#         response = await client.get(NOAA_API_URL, headers=headers, params=params)

#         # Check if the response status is successful
#         print(f"Response Status Code: {response.status_code}")
#         print(f"Raw Response Text: {response.text[:500]}")  # Print first 500 characters of response

#         # If response is not JSON, handle it
#         if response.status_code == 200:
#             try:
#                 data = response.json()  # Try to parse the JSON response
#                 print("Parsed JSON Response:", data)

#                 if 'results' in data:
#                     return data['results']
#                 else:
#                     print(f"Error: 'results' not found in response data: {data}")
#                     raise KeyError("'results' key not found in the response")
#             except ValueError:
#                 print("Response is not JSON format, it might be HTML or something else.")
#                 print("Full Raw Response:", response.text)
#                 raise Exception("Error: Unable to decode response as JSON.")
#         else:
#             print(f"Request failed with status code: {response.status_code}")
#             print(f"Full Response Text: {response.text}")
#             raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")

# # Function to store the fetched weather data in MongoDB
# async def store_weather_data(weather_data):
#     for record in weather_data:
#         record['timestamp'] = datetime.now()
#         await weatherData.insert_one(record)
