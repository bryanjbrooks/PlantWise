// Description: Select wanted plants and display them in a table.
// Notes:
// File: PlantSelectorTable.jsx

import PlantSelectorTable from '../components/PlantSelectorTable';
import { Link } from 'react-router-dom'

function PlantSelector() {
  return (
    <div className="pt-12 w-full text-center">
      <h1 className="text-3xl font-bold mb-4">Browse All Plants</h1>
      <PlantSelectorTable />
      <footer className="mt-12 text-sm text-center text-gray-500">
        <p>Powered by data from Bonnie Plants, Geocodio, The Old Farmer&apos;s Almanac, OpenWeather, Visual Crossing and more.</p>
        <Link to="/sources" className="text-green-700 underline hover:text-green-900">
          → View all data sources 
        </Link>
      </footer>
    </div>
  );
}

export default PlantSelector;