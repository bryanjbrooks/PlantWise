// Description: Dynamic route page for individual plant details.
// File: PlantPage.jsx

import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import PlantGuide from '../components/PlantGuide';

function PlantPage() {
  const { type, name } = useParams(); // type = 'fruits', name = 'Apple'
  const [plantData, setPlantData] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchPlant() {
      try {
        const routeMap = {
          fruits: 'getFruit',
          vegetables: 'getVegetable',
          herbs: 'getHerb',
          nuts: 'getNut'
        };

        const endpoint = `/api/${type}/${routeMap[type]}?name=${encodeURIComponent(name)}`;
        console.log('🔍 Fetching from:', endpoint);

        const res = await fetch(endpoint);
        if (!res.ok) throw new Error(`Error fetching plant: ${res.statusText}`);
        const data = await res.json();

        if (!data || data.error) throw new Error(data.error || 'Plant not found');
        setPlantData(data);
      } catch (err) {
        console.error(err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchPlant();
  }, [type, name]);

  if (loading) return <p className="text-center mt-6">Loading...</p>;
  if (error) return <p className="text-center mt-6 text-red-600">Error: {error}</p>;
  if (!plantData) return <p className="text-center mt-6">No data available for this plant.</p>;

  return (
    <div className="p-6">
      <PlantGuide plantData={plantData} />
    </div>
  );
}

export default PlantPage;