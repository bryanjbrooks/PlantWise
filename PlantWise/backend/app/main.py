# Description: FastAPI routes for the PlantWise API.
# Notes:
# File: main.py

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

# Import the routers
# Import the routers
from app.core.climateZones import router as climateZonesRouter
from app.core.database import router as databaseRouter
from app.core.frostDates import router as frostDatesRouter
from app.core.fruits import router as fruitsRouter
from app.core.herbs import router as herbsRouter
from app.core.sources import router as sourcesRouter
from app.core.veg import router as vegRouter
from app.core.weatherHistory import router as weatherRouter
from app.core.futureWeather import router as futureRouter
from app.routes.geocodioClient import router as geocodioRouter
from app.routes.openWeatherClient import router as openWeatherRouter
from app.routes.visualCrossingClient import router as visualCrossingRouter

# Create the FastAPI app
app = FastAPI(
    title="PlantWise API",
    description="API for the PlantWise Project, handling database, climate zones, weather data, and planting guides and times for fruits, herbs and vegetables.",
    version="1.0.0",
    # Put the schema and docs under /api instead of root
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# Include the routers
apiRouter = APIRouter(prefix="/api")
apiRouter.include_router(climateZonesRouter, prefix="/climateZones", tags=["Climate Zones"])
apiRouter.include_router(databaseRouter, prefix="/database", tags=["Database"])
apiRouter.include_router(frostDatesRouter, prefix="/frostDates", tags=["Frost Dates"])
apiRouter.include_router(geocodioRouter, prefix="/geocodio", tags=["Geocodio"])
apiRouter.include_router(fruitsRouter, prefix="/fruits", tags=["Fruits"])
apiRouter.include_router(herbsRouter, prefix="/herbs", tags=["Herbs"])
apiRouter.include_router(openWeatherRouter, prefix="/openWeather", tags=["OpenWeather"])
apiRouter.include_router(sourcesRouter, prefix="/sources", tags=["Sources"])
apiRouter.include_router(vegRouter, prefix="/vegetables", tags=["Vegetables"])
apiRouter.include_router(visualCrossingRouter, prefix="/visualCrossing", tags=["Visual Crossing"])
apiRouter.include_router(weatherRouter, prefix="/weather", tags=["Weather"])

# Mount the /api router
app.include_router(apiRouter)

# Allow requests from the Vite server during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://plantwise.cc"
        "https://www.plantwise.cc"
        "http://localhost:5173",  # Vite dev server
        "http://127.0.0.1:8000",  # FastAPI local testing
        "http://localhost:8000"
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the PlantWise API!",
            "description": "API for the PlantWise Project",
            "features": "Handles database, climate zones, historical and future weather data, and planting guide and time routes for fruits, herbs and vegetables."
            }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

# @app.on_event("startup")
# async def startup_event():
#     # await store_weather_data(weather_data)
#     print("Weather data has been fetched!")