import { useState } from 'react'

function Geocoding() {
  const [address, setAddress] = useState('')
  const [city, setCity] = useState('')
  const [zipcode, setZipcode] = useState('')
  const [result, setResult] = useState(null)

  const handleSearch = async (type) => {
    let endpoint = ''
    let param = ''

    if (type === 'address') {
      endpoint = 'address'
      param = address
    } else if (type === 'city') {
      endpoint = 'city'
      param = city
    } else if (type === 'zipcode') {
      endpoint = 'zipcode'
      param = zipcode
    }

    const res = await fetch(`http://localhost:8000/api/geocodio/${endpoint}?${type}=${encodeURIComponent(param)}`)
    const data = await res.json()
    setResult(data)
  }

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4 text-center">Geocoding Search</h2>

      <div className="grid gap-4 max-w-xl mx-auto">
        <div>
          <label className="block font-semibold mb-1">Street Address</label>
          <input
            type="text"
            value={address}
            onChange={(e) => setAddress(e.target.value)}
            placeholder="400 W 1st St, Chico, CA"
            className="border p-2 w-full"
          />
          <button
            onClick={() => handleSearch('address')}
            className="mt-2 bg-blue-600 text-white px-4 py-2 rounded"
          >
            Search Address
          </button>
        </div>

        <div>
          <label className="block font-semibold mb-1">City</label>
          <input
            type="text"
            value={city}
            onChange={(e) => setCity(e.target.value)}
            placeholder="Chico"
            className="border p-2 w-full"
          />
          <button
            onClick={() => handleSearch('city')}
            className="mt-2 bg-blue-600 text-white px-4 py-2 rounded"
          >
            Search City
          </button>
        </div>

        <div>
          <label className="block font-semibold mb-1">ZIP Code</label>
          <input
            type="text"
            value={zipcode}
            onChange={(e) => setZipcode(e.target.value)}
            placeholder="95929"
            className="border p-2 w-full"
          />
          <button
            onClick={() => handleSearch('zipcode')}
            className="mt-2 bg-blue-600 text-white px-4 py-2 rounded"
          >
            Search ZIP
          </button>
        </div>
      </div>

      {result && (
        <div className="mt-6 bg-gray-100 p-4 rounded shadow max-w-md mx-auto">
          <h3 className="font-bold mb-2">Geocoding Result:</h3>
          <p><strong>Latitude:</strong> {result.latitude}</p>
          <p><strong>Longitude:</strong> {result.longitude}</p>
          <p><strong>ZIP Code:</strong> {result.zipcode}</p>
        </div>
      )}
    </div>
  )
}

export default Geocoding;