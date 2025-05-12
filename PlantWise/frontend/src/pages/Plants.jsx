
// Description: Page for displaying plants based on type.
// Notes:
// File: Plants.jsx

import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import PlantTable from '../components/PlantTable'
import PlantMenu from '../components/PlantMenu'


const endpointMap = {
  fruits: 'fruits/getFruits',
  herbs: 'herbs/getHerbs',
  vegetables: 'vegetables/getVegetables',
}

function Plants() {
  const [plantType, setPlantType] = useState('fruits')
  const [plantData, setPlantData] = useState([])

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await fetch(`/api/${endpointMap[plantType]}`)
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

      <footer className="mt-12 text-sm text-center text-gray-500">
        <p>Powered by data from Bonnie Plants, GrowVeg Plant Growing Guides, The Old Farmer&apos;s Almanac and more.</p>
        <Link to="/sources" className="text-green-700 underline hover:text-green-900">
          → View all data sources
        </Link>
      </footer>

    </div>
  )
}

export default Plants
