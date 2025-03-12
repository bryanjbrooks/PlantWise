// Description: Page for displaying plants based on type.
// Notes:
// File: Plants.jsx

import { useEffect, useState, useMemo } from 'react'
import PlantMenu from '../components/PlantMenu'

function Plants() {
  const [plantType, setPlantType] = useState('fruits')
  const [plantData, setPlantData] = useState([])

  const endpointMap = useMemo(() => ({
    fruits: 'fruits/getFruits',
    herbs: 'herbs/getHerbs',
    vegetables: 'veg/getVegetables',
  }), [])

  useEffect(() => {
    async function fetchData() {
      const res = await fetch(`http://localhost:8000/${endpointMap[plantType]}`)
      const data = await res.json()

      // Handle both raw array and wrapped response
      if (Array.isArray(data)) {
        setPlantData(data)
      } else {
        const values = Object.values(data).find(val => Array.isArray(val))
        setPlantData(values || [])
      }
    }
    fetchData()
  }, [plantType, endpointMap])

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4 text-center">Browse Plants</h2>
      <PlantMenu selected={plantType} onSelect={setPlantType} />

      <div className="overflow-x-auto">
        <table className="min-w-full border border-gray-300">
          <thead>
            <tr className="bg-green-100">
              {plantData.length > 0 && Object.keys(plantData[0]).map((key) => (
                <th key={key} className="px-4 py-2 border">
                  {key.replace(/_/g, ' ')}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {plantData.map((item, index) => (
              <tr key={index} className="even:bg-green-50">
                {Object.values(item).map((val, i) => (
                  <td key={i} className="px-4 py-2 border">
                    {Array.isArray(val) ? val.join(', ') : val}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
        {plantData.length === 0 && <p className="text-center mt-4">No data available.</p>}
      </div>
      <footer className="mt-8 text-center text-base text-gray-600">
        <p>Data is derived from the following sources:</p>
        <p>The Old Farmer&apos;s Almanac</p>
        <p>UC Master Gardener Program</p>
      </footer>
    </div>
  )
}

export default Plants;
