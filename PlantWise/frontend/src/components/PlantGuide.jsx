// Description: Template for displaying planting guide information for a single plant (fruit, herb, vegetable)
// File: PlantGuide.jsx
// Notes: This component is used to display detailed information about a specific plant, including its growth requirements, care instructions, and companion planting information.

import PropTypes from 'prop-types';
import { getImagePath } from '../plant/utils';

function PlantGuide({ plantData }) {
  if (!plantData) {
    return <div className="text-center mt-10">No data available.</div>;
  }

  return (
    <div className="max-w-4xl mx-auto p-6">
      {/* Plant Image */}
      <div className="flex justify-center mb-6">
        {/* Replace 'plantImageURL' with actual image URL if available */}
        <img
          src={getImagePath(plantData)}
          onError={(e) => {
            e.target.onerror = null;
            e.target.src = '/default.jpg'; // fallback if image is missing
          }}
          alt={plantData.Fruit || plantData.Vegetable || plantData.Herb || 'Plant Image'}
          className="w-64 h-64 object-cover rounded-2xl shadow-md"
        />
      </div>

      {/* Plant Basic Info */}
      <h1 className="text-4xl font-bold mb-2">
        {plantData.Fruit || plantData.Vegetable || plantData.Herb || 'Plant Name'}
      </h1>
      <p className="text-xl text-gray-600 italic mb-6">{plantData.Scientific_Name}</p>

      {/* Zones */}
      <div className="mb-4">
        <h2 className="text-2xl font-semibold mb-2">USDA Zones</h2>
        <p>{plantData.Zones && plantData.Zones.length > 0 ? plantData.Zones.join(', ') : 'Not specified'}</p>
      </div>

      {/* Planting Seasons and Times */}
      <div className="mb-4">
        <h2 className="text-2xl font-semibold mb-2">Planting Seasons</h2>
        <ul className="list-disc list-inside">
          {plantData.Planting_Season_Spring && (
            <li>Spring: {plantData.Planting_Time_Spring?.join(', ') || 'Time not specified'}</li>
          )}
          {plantData.Planting_Season_Summer && (
            <li>Summer: {plantData.Planting_Time_Summer?.join(', ') || 'Time not specified'}</li>
          )}
          {plantData.Planting_Season_Fall && (
            <li>Fall: {plantData.Planting_Time_Fall?.join(', ') || 'Time not specified'}</li>
          )}
          {plantData.Planting_Season_Winter && (
            <li>Winter: {plantData.Planting_Time_Winter?.join(', ') || 'Time not specified'}</li>
          )}
        </ul>
      </div>

      {/* Growth Info */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
        <div>
          <h2 className="text-2xl font-semibold mb-2">Growth Information</h2>
          <ul className="list-inside">
            <li><strong>Maturity Time:</strong> {plantData.Maturity_Time || 'N/A'}</li>
            <li><strong>Germination Time:</strong> {plantData.Germination_Time || 'N/A'}</li>
            <li><strong>Temperature Range:</strong> {plantData.Temperature_Range || 'N/A'}</li>
            <li><strong>Minimum Temperature Tolerance:</strong> {plantData.Minimum_Temperature_Tolerance || 'N/A'}</li>
            <li><strong>Maximum Temperature Tolerance:</strong> {plantData.Maximum_Temperature_Tolerance || 'N/A'}</li>
            <li><strong>Frost Sensitive:</strong> {plantData.Frost_Sensitive ? 'Yes' : 'No'}</li>
          </ul>
        </div>

        {/* Care Info */}
        <div>
          <h2 className="text-2xl font-semibold mb-2">Care Requirements</h2>
          <ul className="list-inside">
            <li><strong>Light Requirements:</strong> {plantData.Light_Requirements || 'N/A'}</li>
            <li><strong>Sun Exposure:</strong> {plantData.Sun_Exposure || 'N/A'}</li>
            <li><strong>Watering Needs:</strong> {plantData.Watering_Needs || 'N/A'}</li>
            <li><strong>Fertilizer Needs:</strong> {plantData.Fertilizer_Needs || 'N/A'}</li>
            <li><strong>Pruning Needs:</strong> {plantData.Pruning_Needs || 'N/A'}</li>
          </ul>
        </div>
      </div>

      {/* Soil and Pollination Info */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
        <div>
          <h2 className="text-2xl font-semibold mb-2">Soil Requirements</h2>
          <ul className="list-inside">
            <li><strong>Soil Type:</strong> {plantData.Soil_Type || 'N/A'}</li>
            <li><strong>Soil pH:</strong> {plantData.Soil_pH || 'N/A'}</li>
          </ul>
        </div>
        <div>
          <h2 className="text-2xl font-semibold mb-2">Pollination</h2>
          <p>{plantData.Pollination || 'N/A'}</p>
        </div>
      </div>

      {/* Companion Plants */}
      <div className="mb-6">
        <h2 className="text-2xl font-semibold mb-2">Companion Plants</h2>
        <p>{plantData.Companion_Plants?.join(', ') || 'Not specified'}</p>
      </div>

      {/* Pest and Disease Management */}
      <div className="mb-6">
        <h2 className="text-2xl font-semibold mb-2">Pest and Disease Management</h2>
        <ul className="list-inside">
          <li><strong>Pest Management:</strong> {plantData.Pest_Management || 'N/A'}</li>
          <li><strong>Common Pests:</strong> {plantData.Common_Pests?.join(', ') || 'N/A'}</li>
          <li><strong>Disease Management:</strong> {plantData.Disease_Management || 'N/A'}</li>
          <li><strong>Common Diseases:</strong> {plantData.Common_Diseases?.join(', ') || 'N/A'}</li>
        </ul>
      </div>

      {/* Regional Tips */}
      <div className="mb-6">
        <h2 className="text-2xl font-semibold mb-2">Regional Planting Tips</h2>
        {plantData.Regional_Tips && Object.keys(plantData.Regional_Tips).length > 0 ? (
          <ul className="list-disc list-inside">
            {Object.entries(plantData.Regional_Tips).map(([region, tip]) => (
              <li key={region}><strong>{region}:</strong> {tip}</li>
            ))}
          </ul>
        ) : (
          <p>No regional tips available.</p>
        )}
      </div>

      {/* Special Instructions */}
      <div className="mb-6">
        <h2 className="text-2xl font-semibold mb-2">Special Instructions</h2>
        <p>{plantData.Special_Instructions || 'None'}</p>
      </div>
    </div>
  );
}

PlantGuide.propTypes = {
  plantData: PropTypes.object,
};

export default PlantGuide;
