from fastapi import FastAPI
from app.routes.noaa import fetchStations
import asyncio

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    stations = await fetchStations()
    # await store_weather_data(weather_data)
    print("Weather data has been fetched!")

# @app.on_event("startup")
# async def startup_event():
#     # Fetch and store weather data when the app starts
#     weather_data = await fetch_noaa_weather()
#     await store_weather_data(weather_data)
#     print("Weather data has been fetched and stored in MongoDB.")

@app.get("/")
async def read_root():
    return {"message": "FastAPI + NOAA Weather Data Example"}

# # @app.get("/fetch_weather")
# async def fetch_and_store_weather():
#     weather_data = await fetch_noaa_weather()
#     await store_weather_data(weather_data)
#     return {"message": "Weather data fetched and stored."}
