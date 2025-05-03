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
        - `climate_zones_by_2023_zip.csv` - Combined list of Alaska, Hawaii, Puerto Rico, and continental US zip codes and their climate zones
        - `hi_zipcode_2023.csv` - List of Hawaii zip codes and their climate zones in csv format
        - `pr_zipcode_2023.csv` - List of Puerto Rico zip codes and their climate zones
        - `us_zipcode_2023.csv` - List of continental US zip codes and their climate zones
      - `Plants/` - Contains JSON lists of planting times for various plants and their climate zones
        - `fruit_planting_times.json` - List of fruits and their planting times by climate zones
        - `herb_planting_times.json` - List of herbs and their planting times by climate zones
        - `nut_planting_times.json` - List of nuts and their planting times by climate zones
        - `vegetable_planting_times.json` - List of vegetables and their planting times by climate zones
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
          - `herbs.py` - Herb planting information DB
          - `keys.py` - Loads the API keys from the environment variables file
          - `lastFrost.py` - Last frost information DB
          - `vegetables.py` - Vegetable planting information DB
          - `weather.py` - Historical weather data DB
        - `models/` Machine learning models
          - `__init__.py` - Python package initializer
          - `autoARIMA.py` - AutoARIMA (Autoregressive Integrated Moving Average) model
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
        - `hardinessZoneMaps/` - USDA hardiness zone maps
          - `regions/` - USDA hardiness zone maps by region
            - `NC_reg_HS_300.png` - North Central U.S hardiness zone map
            - `NE_reg_HS_300.png` - North East U.S hardiness zone map
            - `NW_reg_HS_300.png` - North West U.S hardiness zone map
            - `SC_reg_HS_300.png` - South Central U.S hardiness zone map
            - `SE_reg_HS_300.png` - South East U.S hardiness zone map
            - `SW_reg_HS_300.png` - South West U.S hardiness zone map
          - `states` - USDA hardiness zone maps by state
            - `AK300.png` - Alaska hardiness zone map
            - `AL300.png` - Alabama hardiness zone map
            - `AR300.png` - Arkansas hardiness zone map
            - `AZ300.png` - Arizona hardiness zone map
            - `CA_N300.png` - Northern California hardiness zone map
            - `CA_S300.png` - Southern California hardiness zone map
            - `CO300.png` - Colorado hardiness zone map
            - `CT300.png` - Connecticut hardiness zone map
            - `DE300.png` - Delaware hardiness zone map
            - `FL300.png` - Florida hardiness zone map
            - `GA300.png` - Georgia hardiness zone map
            - `HI300.png` - Hawaii hardiness zone map
            - `IA300.png` - Iowa hardiness zone map
            - `ID300.png` - Idaho hardiness zone map
            - `IL300.png` - Illinois hardiness zone map
            - `IN300.png` - Indiana hardiness zone map
            - `KS300.png` - Kansas hardiness zone map
            - `KY300.png` - Kentucky hardiness zone map
            - `LA300.png` - Louisiana hardiness zone map
            - `MA300.png` - Massachusetts hardiness zone map
            - `MD_DC300.png` - Maryland and D.C. hardiness zone map
            - `ME300.png` - Maine hardiness zone map
            - `MI300.png` - Michigan hardiness zone map
            - `MN300.png` - Minnesota hardiness zone map
            - `MO300.png` - Missouri hardiness zone map
            - `MS300.png` - Mississippi hardiness zone map
            - `MT300.png` - Montana hardiness zone map
            - `NC300.png` - North Carolina hardiness zone map
            - `ND300.png` - North Dakota hardiness zone map
            - `NE300.png` - Nebraska hardiness zone map
            - `NH300.png` - New Hampshire hardiness zone map
            - `NJ300.png` - New Jersey hardiness zone map
            - `NM300.png` - New Mexico hardiness zone map
            - `NV300.png` - Nevada hardiness zone map
            - `NY300.png` - New York hardiness zone map
            - `OH300.png` - Ohio hardiness zone map
            - `OK300.png` - Oklahoma hardiness zone map
            - `OR300.png` - Oregon hardiness zone map
            - `PA300.png` - Pennsylvania hardiness zone map
            - `PR300.png` - Puerto Rico hardiness zone map
            - `SC300.png` - South Carolina hardiness zone map
            - `SD300.png` - South Dakota hardiness zone map
            - `TN300.png` - Tennessee hardiness zone map
            - `TX_E300.png` - Eastern Texas hardiness zone map
            - `TX_W300.png` - Western Texas hardiness zone map
            - `UT300.png` - Utah hardiness zone map
            - `VA300.png` - Virginia hardiness zone map
            - `VT300.png` - Vermont hardiness zone map
            - `WA300.png` - Washington hardiness zone map
            - `WI300.png` - Wisconsin hardiness zone map
            - `WV300.png` - West Virginia hardiness zone map
            - `WY300.png` - Wyoming hardiness zone map
          - `National_Map_HZ_36x24_300.png` - National hardiness zone map
        - `herbs/` - Herb Images
          - `Basil.jpeg` - Basil image
          - `Bay_Laurel.jpeg` - Bay Laurel image
          - `Borage.jpeg` - Borage image
          - `Chive.jpeg` - Chives image
          - `Cilantro.jpeg` - Cilantro image
          - `Dill.jpeg` - Dill image
          - `Fennel.jpeg` - Fennel image
          - `Ginger.jpeg` - Ginger image
          - `Horseradish.jpeg` - Horseradish image
          - `Lavender.jpeg` - Lavender image
          - `Lemon_Balm.jpeg` - Lemon Balm image
          - `Lemon_Grass.jpeg` - Lemon Thyme image
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
          - `PlantMenu.jsx` - Plant menu component
          - `PlantSelectorTable.jsx` - Plant selector table component
          - `PlantTable.jsx` - Plant table component
          - `ZipSearchForm.jsx` - Zip code search form component
        - `pages/` - Page components (home, about, etc.)
          - `__init__.js` - Page initializer
          - `Climate.jsx` - Climate page
          - `Geocoding.jsx` - Geocoding page
          - `Home.jsx` - Home page
          - `Plants.jsx` - Plants page
          - `PlantSelector.jsx` - Plant selector page
          - `Weather.jsx` - Weather page
        - `hooks/` - Custom hooks (useFetch, etc.)
          - `__init__.js` - Hook initializer
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


## 3. Languages & Tools Used
- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [Python](https://www.python.org/)
- [React](https://react.dev/)
- [Vite](https://vite.dev/)


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