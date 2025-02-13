# Documentation
Documentation and references for the project

## Table of Contents
1. [File Structure](#1-project-file-structure)
2. [License References](#2-license-references)
3. [Languages & Tools](#3-languages--tools-used)
4. [Modules & Libraries](#4-modules--libraries)
    1. [Fixing Vulnerabilities](#41-fixing-vulnerabilities)
    2. 
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
    - `LICENSES.md` - Contains a list of the licenses for the libraries, modules and tools used
    - `README.md` - This file
  - `PlantWise/` - The main project directory
    - `backend/` - FastAPI backend
      - `app/`
        - `core/` - Configs and utilities
          - `__init__.py` - Python package initializer
          - `config.py` - Env variables & settings
          - `database.py` - Database connection
        - `models/` MongoDB models (schemas)
          - `__init__.py` - Python package initializer
        - `routes/` - API routes
          - `__init__.py` - Python package initializer
          - `noaa.py` - NOAA API routes
          - `nws.py` - NWS API routes
        - `services/` - Business logic (database queries, ML integration, etc.)
          - `__init__.py` - Python package initializer
        - `__init__.py` - Python package initializer
        - `main.py` - FastAPI entry point
      - `tests/` - Backend tests
        - `__init__.py` - Python package initializer
      - `requirements.txt` - A list of required python backend dependencies
    - `frontend/` - React frontend
      - `public/` - Static assets (images, etc.)
      - `src/` - Source files for the frontend
        - `api/` - API calls (fetchData, etc.)
          <!-- - `__init__.js` - Service initializer -->
        - `components/` - Reusable UI components (buttons, cards, etc.)
          <!-- - `__init__.js` - Component initializer -->
        - `pages/` - Page components (home, about, etc.)
          <!-- - `__init__.js` - Page initializer -->
        - `hooks/` - Custom hooks (useFetch, etc.)
          <!-- - `__init__.js` - Hook initializer -->
        - `App.css` - CSS for the app
        - `App.jsx` - Main React component
        - `index.css` - Global CSS
        - `main.jsx` - Main entry point
      - `eslint.config.js` - ESLint configuration
      - `package-lock.json` - Lock file for npm packages
      - `package.json` - Node.js package configuration
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


## 5. How to Run
- This is some information on how to run the project.

### 5.1. Requirements


### 5.2. Creating a Python virtual environment
- To create a Python virtual environment, run the following command in the root of the project directory:
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