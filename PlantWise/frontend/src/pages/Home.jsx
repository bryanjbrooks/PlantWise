// Description: Home page for the PlantWise frontend application.
// Notes:
// File: Home.jsx

// import PlantSelectorTable from '../components/PlantSelectorTable'

import { Link } from 'react-router-dom'

function Home() {
  return (
    <div className="pt-12 w-full text-center">
      <h1 className="text-4xl font-bold mb-2 text-green-700">Welcome to PlantWise 🌱</h1>
      <p className="text-xl text-gray-700 mb-6 max-w-2xl mx-auto">
        Make smart planting decisions with personalized guides powered by real climate data and historical weather.
      </p>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto mb-10">
        <Link to="/plants" className="bg-white shadow-lg p-6 rounded-xl hover:shadow-2xl transition text-left border border-green-200">
          <h2 className="text-2xl font-semibold text-green-800 mb-2">Browse Plants</h2>
          <p className="text-gray-600">Explore all fruits, herbs, and vegetables available in the database.</p>
        </Link>

        <Link to="/plant-selector" className="bg-white shadow-lg p-6 rounded-xl hover:shadow-2xl transition text-left border border-green-200">
          <h2 className="text-2xl font-semibold text-green-800 mb-2">Build Your Garden</h2>
          <p className="text-gray-600">Select plants you want to grow and see if they match your local climate zone.</p>
        </Link>

        <Link to="/climate" className="bg-white shadow-lg p-6 rounded-xl hover:shadow-2xl transition text-left border border-green-200">
          <h2 className="text-2xl font-semibold text-green-800 mb-2">Find Your Zone</h2>
          <p className="text-gray-600">Look up your USDA climate zone and average frost dates using your ZIP code.</p>
        </Link>
      </div>

      <footer className="mt-12 text-sm text-gray-500">
        <p>Powered by data from Geocodio, OpenWeather, Visual Crossing, PRISM Climate Group, and more.</p>
        <Link to="/sources" className="text-green-700 underline hover:text-green-900">
          View all data sources →
        </Link>
      </footer>
    </div>
  )
}

export default Home
