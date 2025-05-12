// Description: Page for displaying climate zones
// Notes:
// File: ClimateTools.jsx

import { useState } from 'react'
import { Link } from 'react-router-dom'

function ClimateTools() {
  const [zip, setZip] = useState('')
  const [zone, setZone] = useState(null)
  const [trange, setTrange] = useState(null)
  const [loading, setLoading] = useState(false)
  const [selectedRegion, setSelectedRegion] = useState('')
  const [selectedState, setSelectedState] = useState('')

  const handleLookup = async () => {
    if (!zip || zip.length !== 5) return alert("Please enter a valid 5-digit ZIP code")
    setLoading(true)

    try {
      const zoneRes = await fetch(`/api/climateZones/getZone?zip=${zip}`)
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
      </div>

      {loading && <p className="text-center mt-4 text-lg">Loading...</p>}

      {zone && (
        <div className="mt-6 bg-gray-100 p-6 rounded shadow">
          <h3 className="font-bold mb-4 text-2xl text-center">USDA Hardiness Zone</h3>
          <p className="text-xl text-center">
            Your ZIP code <span className="font-semibold">{zip}</span> is in zone{' '}
            <span className="font-bold text-green-700">{zone}</span>.
          </p>
          {trange && (
            <p className="text-lg text-center mt-2">
              This zone typically experiences minimum winter temperatures ranging from <span className="font-semibold">{trange}&deg;F</span>.
            </p>
          )}
        </div>
      )}

      <div className="mt-8 text-center">
        <h3 className="text-2xl font-bold mb-4">USDA Hardiness Zone Map</h3>
        <img
          src="/hardinessZoneMaps/National.png"
          alt="USDA Plant Hardiness Zone Map"
          className="mx-auto rounded shadow-lg w-full max-w-8xl"
        />
        <p className="mt-2 text-sm text-gray-600">
          Source: USDA Agricultural Research Service
        </p>

        <div className="mt-10 flex flex-col md:flex-row md:justify-center gap-10">
          <div className="text-center">
            <h3 className="text-xl font-semibold mb-2">View by Region</h3>
            <select
              value={selectedRegion}
              onChange={(e) => setSelectedRegion(e.target.value)}
              className="border p-2 rounded w-64 text-center"
            >
              <option value="">Select Region</option>
              <option value="NC">North Central</option>
              <option value="NE">Northeast</option>
              <option value="NW">Northwest</option>
              <option value="SC">South Central</option>
              <option value="SE">Southeast</option>
              <option value="SW">Southwest</option>
            </select>

            {selectedRegion && (
              <div className="mt-6">
                <img
                  src={`/hardinessZoneMaps/regions/${selectedRegion}.png`}
                  alt={`${selectedRegion} zone map`}
                  className="mx-auto rounded shadow-md w-full max-w-5xl"
                />
                <p className="mt-2 text-sm text-gray-600">Map for {selectedRegion.replace(/_/g, ' ')}</p>
              </div>
            )}
          </div>

          <div className="text-center">
            <h3 className="text-xl font-semibold mb-2">View by State</h3>
            <select
              value={selectedState}
              onChange={(e) => setSelectedState(e.target.value)}
              className="border p-2 rounded w-64 text-center"
            >
              <option value="">Select State</option>
              <option value="AL">Alabama</option>
              <option value="AK">Alaska</option>
              <option value="AZ">Arizona</option>
              <option value="AR">Arkansas</option>
              <option value="CA_N">California - North</option>
              <option value="CA_S">California - South</option>
              <option value="CO">Colorado</option>
              <option value="CT">Connecticut</option>
              <option value="DE">Delaware</option>
              <option value="FL">Florida</option>
              <option value="GA">Georgia</option>
              <option value="HI">Hawaii</option>
              <option value="ID">Idaho</option>
              <option value="IL">Illinois</option>
              <option value="IN">Indiana</option>
              <option value="IA">Iowa</option>
              <option value="KS">Kansas</option>
              <option value="KY">Kentucky</option>
              <option value="LA">Louisiana</option>
              <option value="ME">Maine</option>
              <option value="MD_DC">Maryland & D.C.</option>
              <option value="MA">Massachusetts</option>
              <option value="MI">Michigan</option>
              <option value="MN">Minnesota</option>
              <option value="MS">Mississippi</option>
              <option value="MO">Missouri</option>
              <option value="MT">Montana</option>
              <option value="NE">Nebraska</option>
              <option value="NV">Nevada</option>
              <option value="NH">New Hampshire</option>
              <option value="NJ">New Jersey</option>
              <option value="NM">New Mexico</option>
              <option value="NY">New York</option>
              <option value="NC">North Carolina</option>
              <option value="ND">North Dakota</option>
              <option value="OH">Ohio</option>
              <option value="OK">Oklahoma</option>
              <option value="OR">Oregon</option>
              <option value="PA">Pennsylvania</option>
              <option value="RI">Rhode Island</option>
              <option value="PR">Puerto Rico</option>
              <option value="SC">South Carolina</option>
              <option value="SD">South Dakota</option>
              <option value="TN">Tennessee</option>
              <option value="TX_E">Texas - East</option>
              <option value="TX_W">Texas - West</option>
              <option value="UT">Utah</option>
              <option value="VT">Vermont</option>
              <option value="VA">Virginia</option>
              <option value="WA">Washington</option>
              <option value="WV">West Virginia</option>
              <option value="WI">Wisconsin</option>
              <option value="WY">Wyoming</option>
            </select>

            {selectedState && (
              <div className="mt-6">
                <img
                  src={`/hardinessZoneMaps/states/${selectedState}.png`}
                  alt={`${selectedState} zone map`}
                  className="mx-auto rounded shadow-md w-full max-w-5xl"
                />
                <p className="mt-2 text-sm text-gray-600">Map for {selectedState.replace(/-/g, ' ')}</p>
              </div>
            )}
          </div>
        </div>
      </div>

      <footer className="mt-12 text-sm text-center text-gray-500">
        <p>Powered by data from the PRISM Climate Group and USDA Agricultural Research Service</p>
        <Link to="/sources" className="text-green-700 underline hover:text-green-900">
          → View all data sources
        </Link>
      </footer>
    </div>
  )
}

export default ClimateTools;