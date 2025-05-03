// Description: Displays a table of one plant type
// File: PlantTable.jsx

import PropTypes from 'prop-types';
import { useNavigate } from 'react-router-dom';
import { getPlantPath } from '../plant/plantRoutes';

function PlantTable({ type, plants }) {
  const navigate = useNavigate();

  const getDisplayName = (plant) =>
    plant.Fruit || plant.Vegetable || plant.Herb || 'Unknown';

  return (
    <div className="overflow-x-auto my-8">
      <h2 className="text-2xl font-semibold mb-2 capitalize">{type}</h2>
      <table className="min-w-full border border-gray-300">
        <thead className="bg-green-100">
          <tr>
            <th className="px-4 py-2 border">Name</th>
            <th className="px-4 py-2 border">Zones</th>
            <th className="px-4 py-2 border">Planting Time Spring</th>
            <th className="px-4 py-2 border">Planting Time Summer</th>
            <th className="px-4 py-2 border">Planting Time Fall</th>
            <th className="px-4 py-2 border">Planting Time Winter</th>
            <th className="px-4 py-2 border">Temperature Range</th>
            <th className="px-4 py-2 border">Minimum Temperature Tolerance</th>
            <th className="px-4 py-2 border">Maximum Temperature Tolerance</th>
            <th className="px-4 py-2 border">Frost Sensitive</th>
          </tr>
        </thead>
        <tbody>
          {plants.map((plant, i) => (
            <tr
              key={i}
              role="button"
              tabIndex={0}
              onClick={() => navigate(getPlantPath(type, getDisplayName(plant)))}
              onKeyDown={(e) => e.key === "Enter" && navigate(getPlantPath(type, getDisplayName(plant)))}
              className="cursor-pointer hover:bg-green-100 even:bg-green-50 transition"
            >
              <td className="px-4 py-2 border font-semibold">{getDisplayName(plant)}</td>
              <td className="px-4 py-2 border">{plant.Zones?.join(', ')}</td>
              <td className="px-4 py-2 border">{plant.Planting_Time_Spring?.join(', ') ?? 'Not in Season'}</td>
              <td className="px-4 py-2 border">{plant.Planting_Time_Summer?.join(', ') ?? 'Not in Season'}</td>
              <td className="px-4 py-2 border">{plant.Planting_Time_Fall?.join(', ') ?? 'Not in Season'}</td>
              <td className="px-4 py-2 border">{plant.Planting_Time_Winter?.join(', ') ?? 'Not in Season'}</td>
              <td className="px-4 py-2 border">{plant.Temperature_Range ?? 'No Data Available'}</td>
              <td className="px-4 py-2 border">{plant.Minimum_Temperature_Tolerance ?? 'No Data Available'}</td>
              <td className="px-4 py-2 border">{plant.Maximum_Temperature_Tolerance ?? 'No Data Available'}</td>
              <td className="px-4 py-2 border">{plant.Frost_Sensitive === true ? "Yes" : plant.Frost_Sensitive === false ? "No" : "No Data Available"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

PlantTable.propTypes = {
  type: PropTypes.string.isRequired,
  plants: PropTypes.arrayOf(PropTypes.object).isRequired,
};

export default PlantTable;
