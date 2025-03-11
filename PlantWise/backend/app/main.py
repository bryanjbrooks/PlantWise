# Description: Main FastAPI application file.
# Notes:
# File: main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import the routers
from app.core.climateZones import router as climateZonesRouter
from app.core.database import router as databaseRouter
from app.core.fruits import router as fruitsRouter
from app.core.herbs import router as herbsRouter
from app.core.lastFrost import router as lastFrostRouter
from app.core.veg import router as vegRouter
from app.core.weatherHistory import router as weatherRouter
from app.routes.geocodioClient import router as geocodioRouter
from app.routes.openWeatherClient import router as openWeatherRouter

# Create the FastAPI app
app = FastAPI(
    title="PlantWise API",
    description="API for the PlantWise Project, handling climate zones, weather data, and planting times for fruits, herbs and vegetables.",
    version="1.0.0"
)

# Include the routers
app.include_router(climateZonesRouter, prefix="/climateZones", tags=["Climate Zones"])
app.include_router(databaseRouter, prefix="/database", tags=["Database"])
app.include_router(fruitsRouter, prefix="/fruits", tags=["Fruits"])
app.include_router(herbsRouter, prefix="/herbs", tags=["Herbs"])
app.include_router(lastFrostRouter, prefix="/lastFrost", tags=["Last Frost"])
app.include_router(vegRouter, prefix="/veg", tags=["Vegetables"])
app.include_router(weatherRouter, prefix="/weather", tags=["Weather"])
app.include_router(geocodioRouter, prefix="/geocodio", tags=["Geocodio"])
app.include_router(openWeatherRouter, prefix="/openWeather", tags=["OpenWeather"])

# Allow requests from the Vite server during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the PlantWise API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

# @app.on_event("startup")
# async def startup_event():
#     # await store_weather_data(weather_data)
#     print("Weather data has been fetched!")

# @app.get("/")
# async def read_root():
#     return {"message": "FastAPI + NOAA Weather Data Example"}