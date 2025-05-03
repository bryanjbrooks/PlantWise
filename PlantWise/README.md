# PlantWise 🌱

## 🧱 Tech Stack

### 🖥️ Frontend
- **React.js** – Component-based UI for dynamic and responsive user experiences  
- **JavaScript + HTML** – Core web technologies for logic and structure  
- **Tailwind CSS** – Utility-first CSS framework for consistent and scalable styling  
- **Vite** – Fast development server and build tool with instant HMR (Hot Module Replacement)  
- **Node.js (development only)** – Powers the Vite dev server and manages frontend dependencies

---

### ⚙️ Backend
- **FastAPI (Python)** – High-performance asynchronous framework for API endpoints and backend logic  
- **HTTPX** – Async HTTP client used to fetch data from:
  - **OpenWeather** – Real-time and historical weather data  
  - **Visual Crossing** – Detailed weather and climate datasets  
- **Geocodio (Python module)** – Converts ZIP codes and addresses to geographic coordinates and provides metadata like county, state, and timezone  
- **Pydantic** – Used for data validation and model serialization  
- **pymongo** – Python MongoDB client for querying and updating the database

---

### 🗄️ Database
- **MongoDB** – NoSQL document database storing:
  - Planting guides by type
    - Fruits, Herbs, Vegetables
  - USDA Plant hardiness zone lookup by ZIP code
  - Historical and forecast weather data
  - Average frost dates and 
  - Sources and attribution for all plant data and imagery  
  - Other supporting metadata used throughout the application
