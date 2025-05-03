
// Description: Displays a full planting guide with all fields in logical order.
// File: PlantGuide.jsx

import PropTypes from 'prop-types';
import { getImagePath } from '../plant/utils';

function PlantGuide({ plantData }) {
  if (!plantData) return <div className="text-center mt-10">No data available.</div>;

  const displayName = plantData.Fruit || plantData.Vegetable || plantData.Herb || plantData.Nut || 'Plant';
  const zones = Array.isArray(plantData.Zones) ? plantData.Zones.join(', ') : 'N/A';

  const formatList = (list) => Array.isArray(list) ? list.join(', ') : 'N/A';
  const formatBool = (val) => val === true ? 'Yes' : val === false ? 'No' : 'N/A';

  return (
    <div className="max-w-6xl mx-auto p-6 text-black">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-start">
        {/* Left Column: Overview */}
        <div>
          <h1 className="text-4xl font-bold mb-1">{displayName}</h1>
          <p className="text-xl italic text-gray-600 mb-6">{plantData.Scientific_Name || 'N/A'}</p>

          <section className="mb-4">
            <h2 className="text-xl font-semibold">Zones</h2>
            <p>{zones}</p>
          </section>

          <section className="mb-4">
            <h2 className="text-xl font-semibold">Temperature</h2>
            <p><strong>Range:</strong> {plantData.Temperature_Range || 'N/A'}</p>
            <p><strong>Min:</strong> {plantData.Minimum_Temperature_Tolerance || 'N/A'} | <strong>Max:</strong> {plantData.Maximum_Temperature_Tolerance || 'N/A'}</p>
            <p><strong>Frost Sensitive:</strong> {formatBool(plantData.Frost_Sensitive)}</p>
          </section>

          <section className="mb-4">
            <h2 className="text-xl font-semibold">Planting Times</h2>
            <p><strong>Spring:</strong> {formatList(plantData.Planting_Time_Spring)}</p>
            <p><strong>Summer:</strong> {formatList(plantData.Planting_Time_Summer)}</p>
            <p><strong>Fall:</strong> {formatList(plantData.Planting_Time_Fall)}</p>
            <p><strong>Winter:</strong> {formatList(plantData.Planting_Time_Winter)}</p>
          </section>

          <section className="mb-4">
            <h2 className="text-xl font-semibold">Harvest Times</h2>
            <p><strong>Spring:</strong> {formatList(plantData.Harvest_Time_Spring)}</p>
            <p><strong>Summer:</strong> {formatList(plantData.Harvest_Time_Summer)}</p>
            <p><strong>Fall:</strong> {formatList(plantData.Harvest_Time_Fall)}</p>
            <p><strong>Winter:</strong> {formatList(plantData.Harvest_Time_Winter)}</p>
          </section>

          <section className="mb-4">
            <h2 className="text-xl font-semibold">Growth Info</h2>
            <p><strong>Maturity Time:</strong> {plantData.Maturity_Time || 'N/A'}</p>
            <p><strong>Germination Time:</strong> {plantData.Germination_Time || 'N/A'}</p>
            <p><strong>Pollination:</strong> {plantData.Pollination || 'N/A'}</p>
          </section>

          <section className="mb-4">
            <h2 className="text-xl font-semibold">Spacing</h2>
            <p><strong>Between Plants:</strong> {plantData.Spacing_Between_Plants || 'N/A'}</p>
            <p><strong>Between Rows:</strong> {plantData.Spacing_Between_Rows || 'N/A'}</p>
          </section>
        </div>

        {/* Right Column: Image + Details */}
        <div className="text-center">
          <img
            src={getImagePath(plantData)}
            onError={(e) => { e.target.onerror = null; e.target.src = '/default.jpg'; }}
            alt={displayName}
            className="w-full max-w-md h-auto object-cover rounded-2xl shadow-lg mx-auto"
          />

          <div className="mt-6 text-left">
            <section className="mb-4">
              <h2 className="text-xl font-semibold">Soil & Light</h2>
              <p><strong>Soil Type:</strong> {plantData.Soil_Type || 'N/A'}</p>
              <p><strong>Soil pH:</strong> {plantData.Soil_pH || 'N/A'}</p>
              <p><strong>Light Requirements:</strong> {plantData.Light_Requirements || 'N/A'}</p>
              <p><strong>Sun Exposure:</strong> {plantData.Sun_Exposure || 'N/A'}</p>
              <p><strong>Watering Needs:</strong> {plantData.Watering_Needs || 'N/A'}</p>
              <p><strong>Fertilizer Needs:</strong> {plantData.Fertilizer_Needs || 'N/A'}</p>
              <p><strong>Pruning Needs:</strong> {plantData.Pruning_Needs || 'N/A'}</p>
            </section>

            <section className="mb-4">
              <h2 className="text-xl font-semibold">Pests & Disease</h2>
              <p><strong>Pest Management:</strong> {plantData.Pest_Management || 'N/A'}</p>
              <p><strong>Common Pests:</strong> {formatList(plantData.Common_Pests)}</p>
              <p><strong>Disease Management:</strong> {plantData.Disease_Management || 'N/A'}</p>
              <p><strong>Common Diseases:</strong> {formatList(plantData.Common_Diseases)}</p>
            </section>

            <section className="mb-4">
              <h2 className="text-xl font-semibold">Companions & Regions</h2>
              <p><strong>Companion Plants:</strong> {formatList(plantData.Companion_Plants)}</p>
              <p><strong>Regional Tips:</strong></p>
              <ul className="list-disc ml-5">
                {plantData.Regional_Tips ? Object.entries(plantData.Regional_Tips).map(([region, tip], i) => (
                  <li key={i}><strong>{region}:</strong> {tip}</li>
                )) : <li>N/A</li>}
              </ul>
            </section>

            <section>
              <h2 className="text-xl font-semibold">Special Instructions</h2>
              <p>{plantData.Special_Instructions || 'N/A'}</p>
            </section>
          </div>
        </div>
      </div>
    </div>
  );
}

PlantGuide.propTypes = {
  plantData: PropTypes.object.isRequired,
};

export default PlantGuide;
