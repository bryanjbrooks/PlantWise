// Description: Page for displaying climate zones
// Notes:
// File: ClimateTools.jsx

import { useState } from 'react'

function ClimateTools() {
  const [zip, setZip] = useState('')
  const [zone, setZone] = useState(null)
  const [trange, setTrange] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleLookup = async () => {
    if (!zip || zip.length !== 5) return alert("Please enter a valid 5-digit ZIP code")
    setLoading(true)

    try {
      const zoneRes = await fetch(`http://localhost:8000/climateZones/getZone?zip=${zip}`)
      const zoneData = await zoneRes.json()
      setZone(zoneData.zone || "Zone not found")
      setTrange(zoneData.trange || null)
    } catch (error) {
      console.error("Error fetching zone:", error)
      alert("Failed to fetch climate zone.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="p-6">
      <h2 className="text-3xl font-bold mb-4 text-center">Climate Zone Lookup</h2>
      <div className="max-w-md mx-auto">
        <label className="block font-semibold mb-1 text-lg">Enter zip code to find USDA hardiness zone</label>
        <input
          type="text"
          value={zip}
          onChange={(e) => setZip(e.target.value)}
          placeholder="Enter ZIP code"
          className="border p-2 w-full mb-4 text-lg"
        />
        <div className="flex justify-center mt-4">
          <button onClick={handleLookup} className="bg-green-600 text-white px-4 py-2 rounded text-lg">
            Lookup Climate Info
          </button>
        </div>

        <div className="text-lg text-center text-gray-600 mt-2">
          Not sure about your zone? You can also check the{' '}
          <a
            href="https://planthardiness.ars.usda.gov/"
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-600 underline hover:text-blue-800"
          >
            USDA Plant Hardiness Zone Map
          </a>.
        </div>
      </div>

      {loading && <p className="text-center mt-4 text-lg">Loading...</p>}

      {zone && (
        <div className="mt-6 bg-gray-100 p-6 rounded shadow">
          <h3 className="font-bold mb-4 text-2xl">USDA Hardiness Zone</h3>
          <p className="text-xl">
            Your ZIP code <span className="font-semibold">{zip}</span> is in zone{' '}
            <span className="font-bold text-green-700">{zone}</span>.
          </p>
          {trange && (
            <p className="text-lg mt-2">
              This zone typically experiences minimum winter temperatures ranging from <span className="font-semibold">{trange}&deg;F</span>.
            </p>
          )}
          <p className="mt-4 text-base">
            To visually verify your zone, visit the{' '}
            <a
              href="https://planthardiness.ars.usda.gov/"
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-600 underline hover:text-blue-800"
            >
              USDA Plant Hardiness Zone Map
            </a>.
          </p>
        </div>
      )}
      <footer className="mt-8 text-center text-base text-gray-600">
        <p>Data is derived from the PRISM Climate Group at Oregon State University</p> 
      </footer>
    </div>
  )
}

export default ClimateTools;