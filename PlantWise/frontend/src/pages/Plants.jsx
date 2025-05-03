
// Description: Page for displaying plants based on type.
// Notes:
// File: Plants.jsx

import { useEffect, useState } from 'react'
import PlantTable from '../components/PlantTable'
import PlantMenu from '../components/PlantMenu'

const endpointMap = {
  fruits: 'fruits/getFruits',
  herbs: 'herbs/getHerbs',
  vegetables: 'veg/getVegetables',
}

function Plants() {
  const [plantType, setPlantType] = useState('fruits')
  const [plantData, setPlantData] = useState([])

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await fetch(`http://localhost:8000/${endpointMap[plantType]}`)
        const data = await res.json()
        if (Array.isArray(data)) {
          setPlantData(data)
        } else {
          const values = Object.values(data).find(val => Array.isArray(val))
          setPlantData(values || [])
        }
      } catch (err) {
        console.error('Failed to fetch plant data:', err)
        setPlantData([])
      }
    }

    fetchData()
  }, [plantType])

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4 text-center">Browse Plants</h2>
      <PlantMenu selected={plantType} onSelect={setPlantType} />

      {plantData.length > 0 ? (
        <PlantTable type={plantType} plants={plantData} />
      ) : (
        <p className="text-center mt-4">No data available.</p>
      )}

      
      <footer className="mt-8 text-center text-base text-gray-600">
        <p>Data is derived from the following sources:</p>
        <p>Bonnie Plants</p>
        <p>GrowVeg Plant Growing Guides</p>
        <p>The Old Farmer&apos;s Almanac</p>
        <p>Urban Farmer Growing Guides</p>
        <p>UCANR - California Master Gardener Handbook, Second Edition</p>
        <p>UCANR - UC Master Gardener Program</p>
      </footer>

    </div>
  )
}

export default Plants
