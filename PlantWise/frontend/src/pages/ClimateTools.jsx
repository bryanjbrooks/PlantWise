// Description: Page for displaying climate tools.
// Notes:
// File: ClimateTools.jsx

import { useState } from 'react'

function ClimateTools() {
  const [zip, setZip] = useState('')
  const [zone, setZone] = useState(null)
  const [coords, setCoords] = useState(null)
  const [weather, setWeather] = useState(null)
  const [frost, setFrost] = useState(null)

  const handleLookup = async () => {
    if (!zip || zip.length !== 5) return alert("Please enter a valid 5-digit ZIP code")

    const zoneRes = await fetch(`http://localhost:8000/climateZones/getZone?zip=${zip}`)
    const zoneData = await zoneRes.json()
    setZone(zoneData.zone)

    const coordRes = await fetch(`http://localhost:8000/geocodio/zipcode?zipcode=${zip}`)
    const coordData = await coordRes.json()
    setCoords(coordData)

    const weatherRes = await fetch(
      `http://localhost:8000/openWeather/historicalWeather?lat=${coordData.latitude}&long=${coordData.longitude}&zipCode=${zip}`
    )
    const weatherData = await weatherRes.json()
    setWeather(weatherData)

    const frostRes = await fetch(`http://localhost:8000/lastFrost/getAverageFrostDates?zipCode=${zip}`)
    const frostData = await frostRes.json()
    setFrost(frostData)
  }

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4 text-center">Climate Tools</h2>
      <div className="max-w-md mx-auto">
        <label className="block font-semibold mb-1">ZIP Code</label>
        <input
          type="text"
          value={zip}
          onChange={(e) => setZip(e.target.value)}
          placeholder="Enter ZIP code"
          className="border p-2 w-full mb-4"
        />
        <button onClick={handleLookup} className="bg-green-600 text-white px-4 py-2 rounded">
          Lookup Climate Info
        </button>
      </div>

      {zone && (
        <div className="mt-6 bg-gray-100 p-4 rounded shadow">
          <h3 className="font-bold mb-2">USDA Hardiness Zone</h3>
          <p>{zone}</p>
        </div>
      )}

      {coords && (
        <div className="mt-4 bg-gray-100 p-4 rounded shadow">
          <h3 className="font-bold mb-2">Coordinates</h3>
          <p>Latitude: {coords.latitude}</p>
          <p>Longitude: {coords.longitude}</p>
        </div>
      )}

      {frost && (
        <div className="mt-4 bg-gray-100 p-4 rounded shadow">
          <h3 className="font-bold mb-2">Average Frost Dates</h3>
          <p>Last Spring Frost: {frost.lastSpringFrost?.date || 'N/A'}</p>
          <p>First Fall Frost: {frost.firstFallFrost?.date || 'N/A'}</p>
        </div>
      )}

      {weather && (
        <div className="mt-4 bg-gray-100 p-4 rounded shadow">
          <h3 className="font-bold mb-2">Historical Weather Data</h3>
          <p>{weather}</p>
        </div>
      )}
    </div>
  )
}

export default ClimateTools;
