// Description: Select wanted plants and display them in a table.
// Notes:
// File: PlantSelectorTable.jsx

import { useEffect, useState } from 'react'

function PlantSelectorTable() {
  const [fruits, setFruits] = useState([])
  const [herbs, setHerbs] = useState([])
  const [vegetables, setVegetables] = useState([])
  const [selectedPlants, setSelectedPlants] = useState([])
  const [zone, setZone] = useState('')
  const [zip, setZip] = useState('')
  const [address, setAddress] = useState('')
  const [city, setCity] = useState('')
  const [frostDates, setFrostDates] = useState(null)

  useEffect(() => {
    async function fetchAll() {
      const fetchGroup = async (type, url) => {
        const res = await fetch(`http://localhost:8000/${url}`)
        const data = await res.json()
        const list = Array.isArray(data) ? data : Object.values(data).find(v => Array.isArray(v)) || []
        return list.map(item => ({ ...item, _type: type }))
      }
      setFruits(await fetchGroup('fruits', 'fruits/getFruits'))
      setHerbs(await fetchGroup('herbs', 'herbs/getHerbs'))
      setVegetables(await fetchGroup('vegetables', 'veg/getVegetables'))
    }

    fetchAll()
  }, [])

  const toggleSelection = (plantName) => {
    setSelectedPlants((prev) =>
      prev.includes(plantName)
        ? prev.filter((name) => name !== plantName)
        : [...prev, plantName]
    )
  }

  const getDisplayName = (plant) => plant.Fruit || plant.Herb || plant.Vegetable

  const handleZoneLookup = async () => {
    if (!zip && !address && !city) return alert("Please enter a ZIP code, address, or city")
  
    let resolvedZip = zip
  
    if (!resolvedZip && address) {
      const res = await fetch(`http://localhost:8000/geocodio/address?address=${encodeURIComponent(address)}`)
      const data = await res.json()
      resolvedZip = data.zipcode || ''
    } else if (!resolvedZip && city) {
      const res = await fetch(`http://localhost:8000/geocodio/city?city=${encodeURIComponent(city)}`)
      const data = await res.json()
      resolvedZip = data.zipcode || ''
    }
  
    if (!resolvedZip) return alert("Could not resolve ZIP code from input")
    setZip(resolvedZip)
  
    const zoneRes = await fetch(`http://localhost:8000/climateZones/getZone?zip=${resolvedZip}`)
    const zoneData = await zoneRes.json()
    setZone((zoneData.zone || '').replace(/[^\d]/g, ''))
  
    const frostRes = await fetch(`http://localhost:8000/frostDates/getAverageFrostDates?zipCode=${resolvedZip}`)
    const frostData = await frostRes.json()
  
    if (frostData.error) {
      const proceed = confirm("No average frost dates found. Would you like to fetch weather history and calculate them?")
      if (proceed) {
        const coordsRes = await fetch(`http://localhost:8000/geocodio/zipcode?zipcode=${resolvedZip}`)
        const coords = await coordsRes.json()
        await fetch(`http://localhost:8000/openWeather/historicalWeather?lat=${coords.latitude}&long=${coords.longitude}&zipCode=${resolvedZip}`)
        const newFrostRes = await fetch(`http://localhost:8000/frostDates/getAverageFrostDates?zipCode=${resolvedZip}`)
        const newFrostData = await newFrostRes.json()
        setFrostDates(newFrostData)
      }
    } else {
      // Set the frost dates to N/A if they are not found
      console.log('Setting frostDates:', frostData)
      setFrostDates(frostData)
    }
  }
  
  const allSelected = [...fruits, ...herbs, ...vegetables].filter((plant) =>
    selectedPlants.includes(getDisplayName(plant))
  )

  return (
    <div className="bg-white text-black p-4 rounded shadow">
      <h3 className="text-xl font-semibold mb-4 text-center">Select Plants You’re Interested In</h3>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
        <input
          type="text"
          value={address}
          onChange={(e) => setAddress(e.target.value)}
          placeholder="Enter address (optional)"
          className="border p-2 rounded text-black"
        />
        <input
          type="text"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          placeholder="Enter city (optional)"
          className="border p-2 rounded text-black"
        />
        <input
          type="text"
          value={zip}
          onChange={(e) => setZip(e.target.value)}
          placeholder="Enter ZIP code"
          className="border p-2 rounded text-black"
        />
        <div className="col-span-full flex justify-center">
          <button
            onClick={handleZoneLookup}
            className="bg-green-600 hover:bg-green-700 text-white text-base font-semibold px-4 py-2 rounded border border-green-700"
          >
            Lookup Frost Dates
          </button>
        </div>
        {zone && <div className="col-span-full text-center font-medium">Zone: {zone}</div>}
      </div>

      {console.log('Rendering frostDates:', frostDates)}
      {frostDates && (
        <div className="text-center mb-6">
          <p className="font-semibold">Average frost dates for {zip} using historical data from 2019-2024</p>
          <p>Last Spring Frost: {frostDates?.lastSpringFrost?.date ?? 'N/A'}</p>
          <p>First Fall Frost: {frostDates?.firstFallFrost?.date ?? 'N/A'}</p>
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <div>
          <label className="font-semibold block mb-1">Fruits</label>
          <select onChange={(e) => toggleSelection(e.target.value)} className="border p-2 rounded w-full">
            <option value="">Select a fruit</option>
            {fruits.map((f, idx) => (
              <option key={idx} value={getDisplayName(f)}>{getDisplayName(f)}</option>
            ))}
          </select>
        </div>
        <div>
          <label className="font-semibold block mb-1">Herbs</label>
          <select onChange={(e) => toggleSelection(e.target.value)} className="border p-2 rounded w-full">
            <option value="">Select a herb</option>
            {herbs.map((h, idx) => (
              <option key={idx} value={getDisplayName(h)}>{getDisplayName(h)}</option>
            ))}
          </select>
        </div>
        <div>
          <label className="font-semibold block mb-1">Vegetables</label>
          <select onChange={(e) => toggleSelection(e.target.value)} className="border p-2 rounded w-full">
            <option value="">Select a vegetable</option>
            {vegetables.map((v, idx) => (
              <option key={idx} value={getDisplayName(v)}>{getDisplayName(v)}</option>
            ))}
          </select>
        </div>
      </div>

      {allSelected.length > 0 && (
        <div className="overflow-x-auto">
          <table className="min-w-full border border-gray-300">
            <thead>
            <tr className="bg-green-100">
              <th className="px-4 py-2 border">Plant</th>
              {Object.keys(allSelected[0]).map((key) => (
                key !== '_type' && key !== 'Fruit' && key !== 'Herb' && key !== 'Vegetable' && (
                  <th key={key} className="px-4 py-2 border">
                    {key.replace(/_/g, ' ')}
                  </th>
                )
              ))}
            </tr>
            </thead>
            <tbody>
              {allSelected.map((plant, i) => (
                <tr key={i} className="even:bg-green-50">
                  <td className="px-4 py-2 border font-semibold">
                    {getDisplayName(plant)}
                  </td>
                  {Object.entries(plant).map(([key, val], j) => (
                    key !== '_type' && key !== 'Fruit' && key !== 'Herb' && key !== 'Vegetable' && (
                      <td key={j} className="px-4 py-2 border">
                        {Array.isArray(val) ? val.join(', ') : val}
                      </td>
                    )
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  )
}

export default PlantSelectorTable;
