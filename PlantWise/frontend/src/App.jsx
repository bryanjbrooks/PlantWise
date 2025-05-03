// Description: Main entry point for the frontend application.
// Display the navigation bar and routes to different pages.
// Notes: 
// File: App.jsx

import { Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home'
import Plants from './pages/Plants'
import PlantSelector from './pages/PlantSelector'
// import Geocoding from './pages/Geocoding'
import ClimateTools from './pages/Climate'
import PlantPage from './pages/PlantPage' // <-- ADD this import

function App() {
  return (
    <div className="min-h-screen font-sans bg-gray-100 text-black">
      <nav className="flex gap-4 p-4 bg-green-200 text-green-900 font-bold justify-between">
        <div className="flex gap-4">
          <Link to="/">Home</Link>
          <Link to="/plants">Plants</Link>
          <Link to="/plant-selector">Plant Selector</Link>
          {/* <Link to="/geocoding">Geocoding</Link> */}
          <Link to="/climate">Climate</Link>
        </div>
        <div className="px-4 py-2 text-base font-bold">PlantWise</div>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/plants" element={<Plants />} />
        <Route path="/plant-selector" element={<PlantSelector />} />
        {/* <Route path="/geocoding" element={<Geocoding />} /> */}
        <Route path="/climate" element={<ClimateTools />} />
        
        {/* 🚀 New route for individual plant pages */}
        <Route path="/plant/:type/:name" element={<PlantPage />} />
      </Routes>
    </div>
  )
}

export default App;
