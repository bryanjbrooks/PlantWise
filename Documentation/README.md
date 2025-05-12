# Documentation
Documentation and references for the project

## Table of Contents
1. [File Structure](#1-project-file-structure)
2. [License References](#2-license-references)
3. [Languages & Tools](#3-languages--tools-used)
4. [Modules & Libraries](#4-modules--libraries)
    1. [Fixing Vulnerabilities](#41-fixing-vulnerabilities)
    2. [Py-Geocodio](#42-py-geocodio)
    3. [PyMongo](#43-pymongo)
    4. [FastAPI](#44-fastapi)
    5. [MongoDB](#45-mongodb)
    6. [React](#46-react)
    7. [Vite](#47-vite)
    8. [Tailwind CSS](#48-tailwind-css)
5. [How to Run](#5-how-to-run)
    1. [Requirements](#51-requirements)
    2. [Creating a Python virtual environment](#52-creating-a-python-virtual-environment)
    3. [Starting the virtual environment for FastAPI](#53-starting-the-virtual-environment-for-fastapi)
    4. [Starting the FastAPI server](#54-starting-the-fastapi-server)
    5. [Starting the React frontend](#55-starting-the-react-frontend)


## 1. Project File Structure
- `/` - The root of the GitHub repository.
  - `Documentation/` - Contains documentation for the project
    - `Licenses/` - Contains copies of the licenses for the libraries, modules, and tools used
      - `Darts-License.md` - License for the Darts library
      - `NodeJS-License.md` - License for Node.js
      - `OpenWeather.md` - License for the OpenWeather API
      - `Py-Geocodio-License.md` - License for the Py-Geocodio library
      - `React-License.md` - License for React
      - `Tailwind-License.md` - License for Tailwind CSS
      - `Vite-License.md` - License for Vite
    - `Lists/` - Contains lists of climate zones and plants used in the database
      - `ClimateZones/` - Lists of climate zones by zip code from the PRISM Climate Group at Oregon State University
        - `ak_zipcode_2023.csv` - List of Alaska zip codes and their climate zones in csv format
        - `climate_zones_by_2023_zip.csv` - Combined list of Alaska, Hawaii, Puerto Rico, and continental US zip codes and their climate zones in csv format
        - `hi_zipcode_2023.csv` - List of Hawaii zip codes and their climate zones in csv format
        - `pr_zipcode_2023.csv` - List of Puerto Rico zip codes and their climate zones in csv format
        - `us_zipcode_2023.csv` - List of continental US zip codes and their climate zones in csv format
        - `USClimateZones.json` - List of all US (AK, HI, PR, continental US) zip codes and their climate zones in json format
      - `Plants/` - Contains JSON lists of planting times for various plants and their climate zones
        - `fruit_planting_guides.json` - List of fruits and their planting guides
        - `herb_planting_guides.json` - List of herbs and their planting guides
        - `vegetable_planting_guides.json` - List of vegetables and their planting guides
      - `Sources/` - Contains the sources used for the various plants
        - `fruit_sources.json` - List of sources for fruits and their planting times
        - `herb_sources.json` - List of sources for herbs and their planting times
        - `nut_sources.json` - List of sources for nuts and their planting times
        - `vegetable_sources.json` - List of sources for vegetables and their planting times
    - `LICENSES.md` - Contains a list of the licenses for the libraries, modules and tools used
    - `README.md` - This file
  - `PlantWise/` - The main project directory
    - `backend/` - FastAPI backend
      - `app/`
        - `core/` - Configs and utilities
          - `__init__.py` - Python package initializer
          - `climateZones.py` - Climate zone data DB
          - `database.py` - MongoDB connection
          - `frostDates.py` - Frost date information DB
          - `fruits.py` - Fruit planting information DB
          - `futureWeather.py` - Future weather data DB
          - `herbs.py` - Herb planting information DB
          - `keys.py` - Loads the API keys from the environment variables file
          - `sources.py` - Project sources DB
          - `veg.py` - Vegetable planting information DB
          - `weatherHistory.py` - Historical weather data DB
        - `models/` Machine learning models
          - `__init__.py` - Python package initializer
          - `autoARIMA.py` - AutoARIMA (Automatic Autoregressive Integrated Moving Average) model
          - `linearRegression.py` - Linear regression model
          - `N-BEATS.py` - N-BEATS (Neural Basis Expansion Analysis Time Series Forecasting) model
          - `TBAST.py` - TBATS (Trigonometric, Box-Cox, ARMA (Autoregressive Moving Average) Errors Trend, Seasonal Components) model
        - `routes/` - API routes
          - `__init__.py` - Python package initializer
          - `geocodioClient.py` - Geocodio API routes
          - `noaa.py` - NOAA API routes
          - `openWeatherClient.py` - OpenWeather API routes
          - `visualCrossingClient.py` - Visual Crossing API routes          
        - `__init__.py` - Python package initializer
        - `main.py` - FastAPI entry point
      - `tests/` - Backend tests
        - `__init__.py` - Python package initializer
      - `requirements.txt` - A list of required python backend dependencies
    - `frontend/` - React frontend
      - `public/` - Static assets (images, etc.)
        - `fruits/` - Fruit Images
          - `Apple.jpeg` - Apple image
          - `Apricot.jpeg` - Apricot image
          - `Banana.jpeg` - Banana image
          - `Blackberry.jpeg` - Blackberry image
          - `Blood_Orange.jpeg` - Blood Orange image
          - `Blueberry.jpeg` - Blueberry image
          - `Boysenberry.jpeg` - Boysenberry image
          - `Cantaloupe.jpeg` - Cantaloupe image
          - `Cherry.jpeg` - Cherry image
          - `Cranberry.jpeg` - Cranberry image
          - `Currant.jpeg` - Currant image
          - `Dragon_Fruit.jpeg` - Dragon fruit image
          - `Elderberry.jpeg` - Elderberry image
          - `Fig.jpeg` - Fig image
          - `Goji_Berry.jpeg` - Goji Berry image
          - `Gooseberry.jpeg` - Gooseberry image
          - `Grape.jpeg` - Grape image
          - `Grapefruit.jpeg` - Grapefruit image
          - `Guava.jpeg` - Guava image
          - `Honeydew.jpeg` - Honeydew image
          - `Jackfruit.jpeg` - Jackfruit image
          - `Kiwi.jpeg` - Kiwi image
          - `Lemon.jpeg` - Lemon image
          - `Lime.jpeg` - Lime image
          - `Mango.jpeg` - Mango image
          - `Nectarine.jpeg` - Nectarine image
          - `Orange.jpeg` - Orange image
          - `Peach.jpeg` - Peach image
          - `Pear.jpeg` - Pear image
          - `Persimmon.jpeg` - Persimmon image
          - `Pineapple.jpeg` - Pineapple image
          - `Plum.jpeg` - Plum image
          - `Pomegranate.jpeg` - Pomegranate image
          - `Prickly_Pear.jpeg` - Prickly Pear image
          - `Raspberry.jpeg` - Raspberry image
          - `Strawberry.jpeg` - Strawberry image
          - `Tangerine.jpeg` - Tangerine image
          - `Watermelon.jpeg` - Watermelon image
        - `hardinessZoneMaps/` - USDA hardiness zone maps
          - `regions/` - USDA hardiness zone maps by region
            - `NC.png` - North Central U.S hardiness zone map
            - `NE.png` - North East U.S hardiness zone map
            - `NW.png` - North West U.S hardiness zone map
            - `SC.png` - South Central U.S hardiness zone map
            - `SE.png` - South East U.S hardiness zone map
            - `SW.png` - South West U.S hardiness zone map
          - `states` - USDA hardiness zone maps by state
            - `AK.png` - Alaska hardiness zone map
            - `AL.png` - Alabama hardiness zone map
            - `AR.png` - Arkansas hardiness zone map
            - `AZ.png` - Arizona hardiness zone map
            - `CA_N.png` - Northern California hardiness zone map
            - `CA_S.png` - Southern California hardiness zone map
            - `CO.png` - Colorado hardiness zone map
            - `CT.png` - Connecticut hardiness zone map
            - `DE.png` - Delaware hardiness zone map
            - `FL.png` - Florida hardiness zone map
            - `GA.png` - Georgia hardiness zone map
            - `HI.png` - Hawaii hardiness zone map
            - `IA.png` - Iowa hardiness zone map
            - `ID.png` - Idaho hardiness zone map
            - `IL.png` - Illinois hardiness zone map
            - `IN.png` - Indiana hardiness zone map
            - `KS.png` - Kansas hardiness zone map
            - `KY.png` - Kentucky hardiness zone map
            - `LA.png` - Louisiana hardiness zone map
            - `MA.png` - Massachusetts hardiness zone map
            - `MD_DC.png` - Maryland and D.C. hardiness zone map
            - `ME.png` - Maine hardiness zone map
            - `MI.png` - Michigan hardiness zone map
            - `MN.png` - Minnesota hardiness zone map
            - `MO.png` - Missouri hardiness zone map
            - `MS.png` - Mississippi hardiness zone map
            - `MT.png` - Montana hardiness zone map
            - `NC.png` - North Carolina hardiness zone map
            - `ND.png` - North Dakota hardiness zone map
            - `NE.png` - Nebraska hardiness zone map
            - `NH.png` - New Hampshire hardiness zone map
            - `NJ.png` - New Jersey hardiness zone map
            - `NM.png` - New Mexico hardiness zone map
            - `NV.png` - Nevada hardiness zone map
            - `NY.png` - New York hardiness zone map
            - `OH.png` - Ohio hardiness zone map
            - `OK.png` - Oklahoma hardiness zone map
            - `OR.png` - Oregon hardiness zone map
            - `PA.png` - Pennsylvania hardiness zone map
            - `PR.png` - Puerto Rico hardiness zone map
            - `SC.png` - South Carolina hardiness zone map
            - `SD.png` - South Dakota hardiness zone map
            - `TN.png` - Tennessee hardiness zone map
            - `TX_E.png` - Eastern Texas hardiness zone map
            - `TX_W.png` - Western Texas hardiness zone map
            - `UT.png` - Utah hardiness zone map
            - `VA.png` - Virginia hardiness zone map
            - `VT.png` - Vermont hardiness zone map
            - `WA.png` - Washington hardiness zone map
            - `WI.png` - Wisconsin hardiness zone map
            - `WV.png` - West Virginia hardiness zone map
            - `WY.png` - Wyoming hardiness zone map
          - `National.png` - National hardiness zone map
        - `herbs/` - Herb Images
          - `Basil.jpeg` - Basil image
          - `Bay_Leaf.jpeg` - Bay Laurel image
          - `Borage.jpeg` - Borage image
          - `Chive.jpeg` - Chives image
          - `Cilantro.jpeg` - Cilantro image
          - `Dill.jpeg` - Dill image
          - `Fennel.jpeg` - Fennel image
          - `Ginger.jpeg` - Ginger image
          - `Horseradish.jpeg` - Horseradish image
          - `Lavender.jpeg` - Lavender image
          - `Lemon_Balm.jpeg` - Lemon Balm image
          - `Lemongrass.jpeg` - Lemon Thyme image
          - `Marjoram.jpeg` - Marjoram image
          - `Mint.jpeg` - Mint image
          - `Oregano.jpeg` - Oregano image
          - `Parsley.jpeg` - Parsley image
          - `Rosemary.jpeg` - Rosemary image
          - `Sage.jpeg` - Sage image
          - `Tarragon.jpeg` - Tarragon image
          - `Thyme.jpeg` - Thyme image
        - `vegetables/` - Vegetable Images
          - `Artichoke.jpeg` - Artichoke image
          - `Arugula.jpeg` - Arugula image
          - `Asparagus.jpeg` - Asparagus image
          - `Avocado.jpeg` - Avocado image
          - `Beet.jpeg` - Beet image
          - `Bock_Choy.jpeg` - Bok Choy image
          - `Broccoli.jpeg` - Broccoli image
          - `Brussel_Sprouts.jpeg` - Brussel Sprouts image
          - `Cabbage.jpeg` - Cabbage image
          - `Carrot.jpeg` - Carrot image
          - `Cauliflower.jpeg` - Cauliflower image
          - `Celery.jpeg` - Celery image
          - `Chard.jpeg` - Chard image
          - `Chayote.jpeg` - Chayote image
          - `Collards.jpeg` - Collards image
          - `Cucumber.jpeg` - Cucumber image
          - `Eggplant.jpeg` - Eggplant image
          - `Garlic.jpeg` - Garlic image
          - `Green_Onion.jpeg` - Green Onion image
          - `Jicama.jpeg` - Jicama image
          - `Kale.jpeg` - Kale image
          - `Kohlrabi.jpeg` - Kohlrabi image
          - `Leek.jpeg` - Leek image
          - `Lettuce.jpeg` - Lettuce image
          - `Mustard_Greens.jpeg` - Mustard Greens image
          - `Okra.jpeg` - Okra image
          - `Onion.jpeg` - Onion image
          - `Parsnip.jpeg` - Parsnip image
          - `Peas.jpeg` - Peas image
          - `Peppers.jpeg` - Peppers image
          - `Potato.jpeg` - Potato image
          - `Pumpkin.jpeg` - Pumpkin image
          - `Radicchio.jpeg` - Radicchio image
          - `Radish.jpeg` - Radish image
          - `Rhubarb.jpeg` - Rhubarb image
          - `Rutabaga.jpeg` - Rutabaga image
          - `Salsify.jpeg` - Salsify image
          - `Shallot.jpeg` - Shallot image
          - `Spinach.jpeg` - Spinach image
          - `Sweet_Corn.jpeg` - Sweet Corn image
          - `Sweet_Potato.jpeg` - Sweet Potato image
          - `Tomatillo.jpeg` - Tomatillo image
          - `Tomato.jpeg` - Tomato image
          - `Turnip.jpeg` - Turnip image
          - `Winter_Squash.jpeg` - Winter Squash image
          - `Yam.jpeg` - Yam image
          - `Zucchini.jpeg` - Zucchini image
      - `src/` - Source files for the frontend
        - `components/` - Reusable UI components (buttons, cards, etc.)
          - `__init__.js` - Component initializer
          - `PlantGuide.jsx` - Plant guide component
          - `PlantMenu.jsx` - Plant menu component
          - `PlantSelectorTable.jsx` - Plant selector table component
          - `PlantTable.jsx` - Plant table component
          - `ZipSearchForm.jsx` - Zip code search form component
        - `hooks/` - Custom hooks (useFetch, etc.)
          - `__init__.js` - Hook initializer
        - `pages/` - Page components (home, about, etc.)
          - `__init__.js` - Page initializer
          - `Climate.jsx` - Climate page
          - `Geocoding.jsx` - Geocoding page
          - `Home.jsx` - Home page
          - `PlantPage.jsx` - Plant page
          - `Plants.jsx` - Plants page
          - `PlantSelector.jsx` - Plant selector page
          - `Sources.jsx` - Sources page
          - `Weather.jsx` - Weather page
        - `plant/` - Plant routes and utils
          - `__init__.js` - Plant initializer
          - `plantRoutes.js` - Plant routes
          - `plantUtils.js` - Plant utils
        - `App.css` - CSS for the app
        - `App.jsx` - Main React component
        - `index.css` - Global CSS
        - `main.jsx` - Main entry point
      - `eslint.config.js` - ESLint configuration
      - `package-lock.json` - Lock file for npm packages
      - `package.json` - Node.js package configuration
      - `tailwind.config.js` - Tailwind CSS configuration
      - `vite.config.js` - Vite configuration
    - `README.md` - README for the project
  - `.gitignore` - A list of files and directories to ignore in the repository
  - `LICENSE` - The license for this project
  - `README.md` - Main README for the repository


## 2. License References
According to the terms and conditions of the various licenses, the following references must be included in the project:
- [Licenses](LICENSES.md)


## 3. Languages & Tools
- [Darts](https://unit8co.github.io/darts/)
- [Geocodio API](https://www.geocod.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [OpenWeather API](https://openweathermap.org/api)
- [Node.js](https://nodejs.org/)
- [Python](https://www.python.org/)
- [React](https://react.dev/)
- [Vite](https://vite.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Visual Crossing API](https://www.visualcrossing.com/weather-api)


## 4. Modules & Libraries
- Most of the libraries used in this project are listed below. The links will take you to the GitHub, or the webpage for each library

### 4.1. Fixing Vulnerabilities
You may encounter a similar notice when installing packages:
```bash
4 vulnerabilities (1 high, 3 critical)

To address issues that do not require attention, run:
  npm audit fix

To address all issues (including breaking changes), run:
  npm audit fix --force
```
To fix the vulnerabilities, run the following command in the root of the project directory:
```bash
npm audit fix --force
```

### 4.2. Py-Geocodio
- [Py-Geocodio](https://github.com/bennylope/pygeocodio)
  - Py-Geocodio is a Python wrapper for the Geocodio API.

### 4.3. PyMongo
- [PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/get-started/)
  - PyMongo is a Python package that you can use to connect to and communicate with MongoDB.

### 4.4. FastAPI
- [FastAPI](https://fastapi.tiangolo.com/)
  - FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
  - FastAPI is built on top of Starlette for the web parts and Pydantic for the data parts.

### 4.5. MongoDB
- [MongoDB](https://www.mongodb.com/)
  - MongoDB is a document database with the scalability and flexibility that you want with the querying and indexing that you need.
  - MongoDB is a NoSQL database that uses JSON-like documents with optional schemas.

### 4.6. React
- [React](https://react.dev/)
  - React is a JavaScript library for building user interfaces.
  - React is a declarative, efficient, and flexible JavaScript library for building user interfaces.
  - React allows you to compose complex UIs from small and isolated pieces of code called “components.”

### 4.7. Vite
- [Vite](https://vite.dev/)
  - Vite is a next-generation, front-end tool that focuses on speed and performance.
  - Vite is a build tool that aims to provide a faster and leaner development experience for modern web projects.
  - Vite is a fast, lightweight, and highly extensible build tool that is designed to be easy to use and configure.

### 4.8. Tailwind CSS
- [Tailwind CSS](https://tailwindcss.com/)
  - Tailwind CSS is a utility-first CSS framework for creating custom designs without having to leave your HTML.
  - Tailwind CSS is a utility-first CSS framework that provides low-level utility classes to build custom designs.

## 5. How to Run
- This is some information on how to run the project.

### 5.1. Requirements
- To run the project, you will need to have the following installed:
  - [MongoDB](https://www.mongodb.com/)
  - [Node.js](https://nodejs.org/)
  - [Python](https://www.python.org/)
  - [React](https://react.dev/)
  - [Vite](https://vite.dev/)
  - See [requirements.txt](/PlantWise/backend/requirements.txt) for Python dependencies
  - See [package.json](/PlantWise/frontend/package.json) for Node.js dependencies

### 5.2. Creating a Python virtual environment
- To create a Python virtual environment, run the following command in the backend folder of the project directory:
```bash
python -m venv .venv
```

### 5.3. Starting the virtual environment for FastAPI
- To start the virtual environment for FastAPI, run the following command in the `\PlantWise\backend` project directory:
```bash
.venv\Scripts\activate
```

### 5.4. Starting the FastAPI server
- To start the FastAPI server in dev mode, run the following command in the `\PlantWise\backend\app` project directory:
```bash
fastapi dev main.py
```

- To start the FastAPI server in production mode, run the following command in the `\PlantWise\backend\app` project directory:
```bash
fastapi run main.py
```

### 5.5. Starting the React frontend
- To start the React frontend, run the following command in the `\PlantWise\frontend` project directory:
```bash
npm run dev
```