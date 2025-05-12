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

  const getRecommendedPlantingDate = (plant, lastSpringFrost, userZone) => {
    const zones = plant.Zones || []
    if (!zones.includes(Number(userZone))) return 'Not Recommended'

    const plantingMonths = plant.Planting_Time_Spring || []
    if (!lastSpringFrost?.date || plantingMonths.length === 0) return 'Not in Season'

    const frostDate = new Date(lastSpringFrost.date)
    const frostMonthIndex = frostDate.getMonth()
    const frostDay = frostDate.getDate()

    const months = [
      "January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"
    ]

    for (let m of plantingMonths) {
      const normalized = m.trim()
      const plantingIndex = months.indexOf(normalized)
      if (plantingIndex >= frostMonthIndex) {
        return `~ ${normalized} ${frostDay}`
      }
    }

    return `~ ${plantingMonths[0]} ${frostDay}`
  }

  const getRecommendedFallPlantingDate = (plant, firstFallFrost, userZone) => {
    const zones = plant.Zones || []
    if (!zones.includes(Number(userZone))) return 'Not Recommended'

    const plantingMonths = plant.Planting_Time_Fall || []
    if (!firstFallFrost?.date || plantingMonths.length === 0) return 'Not in Season'

    const frostDate = new Date(firstFallFrost.date)
    frostDate.setDate(frostDate.getDate() - 49) // 7 weeks before frost
    const frostDay = frostDate.getDate()
    const months = [
      "January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"
    ]
    const month = months[frostDate.getMonth()]
    return `~ ${month} ${frostDay}`
  }

  useEffect(() => {
    async function fetchAll() {
      const fetchGroup = async (type, url) => {
        const res = await fetch(`/api/${url}`)
        const data = await res.json()
        const list = Array.isArray(data) ? data : Object.values(data).find(v => Array.isArray(v)) || []
        return list.map(item => ({ ...item, _type: type }))
      }

      setFruits(await fetchGroup('fruits', 'fruits/getFruits'))
      setHerbs(await fetchGroup('herbs', 'herbs/getHerbs'))
      setVegetables(await fetchGroup('vegetables', 'vegetables/getVegetables'))
    }

    fetchAll()
  }, [])

  // Clear zone and frost dates when address, city, or zip changes
  useEffect(() => {
  setZone('')
  setFrostDates(null)
}, [address, city, zip])

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
      const res = await fetch(`/api/geocodio/address?address=${encodeURIComponent(address)}`)
      const data = await res.json()
      resolvedZip = data.zipcode || ''
    } else if (!resolvedZip && city) {
      const res = await fetch(`/api/geocodio/city?city=${encodeURIComponent(city)}`)
      const data = await res.json()
      resolvedZip = data.zipcode || ''
    }

    if (!resolvedZip) return alert("Could not resolve ZIP code from input")
    setZip(resolvedZip)

    const zoneRes = await fetch(`/api/climateZones/getZone?zip=${resolvedZip}`)
    const zoneData = await zoneRes.json()
    setZone((zoneData.zone || '').replace(/[^\d]/g, ''))

    let frostRes = await fetch(`/api/frostDates/getAverageFrostDates?zipCode=${resolvedZip}`)
    let frostData = await frostRes.json()

    if (frostData?.error || !frostData?.lastSpringFrost) {
      alert("No frost dates found. Fetching historical weather to calculate...")

      const coordsRes = await fetch(`/api/geocodio/zipcode?zipcode=${resolvedZip}`)
      const coords = await coordsRes.json()

      await fetch(`/api/visualCrossing/historicalWeather?lat=${coords.latitude}&long=${coords.longitude}&zipCode=${resolvedZip}`)

      frostRes = await fetch(`/api/frostDates/getAverageFrostDates?zipCode=${resolvedZip}`)
      frostData = await frostRes.json()
    }

    if (frostData?.lastSpringFrost) {
      setFrostDates(frostData)
    } else {
      alert("Unable to calculate frost dates. Please try again later.")
    }
  }

  const allSelected = [...fruits, ...herbs, ...vegetables].filter((plant) =>
    selectedPlants.includes(getDisplayName(plant))
  )

  return (
    <div className="bg-white text-black p-4 rounded shadow">
      <h3 className="text-xl font-semibold mb-4 text-center">Select Plants You’re Interested In</h3>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
        <input type="text" value={address} onChange={(e) => setAddress(e.target.value)} placeholder="Enter address (optional)" className="border p-2 rounded text-black" />
        <input type="text" value={city} onChange={(e) => setCity(e.target.value)} placeholder="Enter city (optional)" className="border p-2 rounded text-black" />
        <input type="text" value={zip} onChange={(e) => setZip(e.target.value)} placeholder="Enter ZIP code" className="border p-2 rounded text-black" />
        <div className="col-span-full flex justify-center">
          <button onClick={handleZoneLookup} className="bg-green-600 hover:bg-green-700 text-white text-base font-semibold px-4 py-2 rounded border border-green-700">
            Lookup Frost Dates
          </button>
        </div>
        {zone && <div className="col-span-full text-center font-medium">Zone: {zone}</div>}
      </div>

      {!frostDates && (
        <div className="text-center text-red-600 font-semibold mb-4">
          Please look up your frost dates before selecting plants.
        </div>
      )}

      {frostDates && (
        <div className="text-center mb-6">
          <p className="font-semibold">Average frost dates for {zip} using historical data from 1995-Present</p>
          <p>Last Spring Frost: {frostDates?.lastSpringFrost?.date ?? 'N/A'}</p>
          <p>First Fall Frost: {frostDates?.firstFallFrost?.date ?? 'N/A'}</p>
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <div>
          <label className="font-semibold block mb-1">Fruits</label>
          <select onChange={(e) => toggleSelection(e.target.value)} disabled={!frostDates} className="border p-2 rounded w-full disabled:opacity-50">
            <option value="">Select a fruit</option>
            {fruits.map((f, idx) => (
              <option key={idx} value={getDisplayName(f)}>{getDisplayName(f)}</option>
            ))}
          </select>
        </div>
        <div>
          <label className="font-semibold block mb-1">Herbs</label>
          <select onChange={(e) => toggleSelection(e.target.value)} disabled={!frostDates} className="border p-2 rounded w-full disabled:opacity-50">
            <option value="">Select a herb</option>
            {herbs.map((h, idx) => (
              <option key={idx} value={getDisplayName(h)}>{getDisplayName(h)}</option>
            ))}
          </select>
        </div>
        <div>
          <label className="font-semibold block mb-1">Vegetables</label>
          <select onChange={(e) => toggleSelection(e.target.value)} disabled={!frostDates} className="border p-2 rounded w-full disabled:opacity-50">
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
                <th className="px-4 py-2 border">Zones</th>
                <th className="px-4 py-2 border">Planting Time Spring</th>
                <th className="px-4 py-2 border">Planting Time Summer</th>
                <th className="px-4 py-2 border">Planting Time Fall</th>
                <th className="px-4 py-2 border">Planting Time Winter</th>
                <th className="px-4 py-2 border">Temperature Range</th>
                <th className="px-4 py-2 border">Min Temp Tolerance</th>
                <th className="px-4 py-2 border">Max Temp Tolerance</th>
                <th className="px-4 py-2 border">Frost Sensitive</th>
                <th className="px-4 py-2 border">Recommended Spring Planting Date</th>
                <th className="px-4 py-2 border">Recommended Fall Planting Date</th>
              </tr>
            </thead>
            <tbody>
              {allSelected.map((plant, i) => (
                <tr key={i} className="even:bg-green-50">
                  <td className="px-4 py-2 border font-semibold">{getDisplayName(plant)}</td>
                  <td className="px-4 py-2 border text-center">{plant.Zones?.join(', ') ?? 'N/A'}</td>
                  <td className="px-4 py-2 border text-center">{plant.Planting_Time_Spring?.join(', ') ?? 'Not in Season'}</td>
                  <td className="px-4 py-2 border text-center">{plant.Planting_Time_Summer?.join(', ') ?? 'Not in Season'}</td>
                  <td className="px-4 py-2 border text-center">{plant.Planting_Time_Fall?.join(', ') ?? 'Not in Season'}</td>
                  <td className="px-4 py-2 border text-center">{plant.Planting_Time_Winter?.join(', ') ?? 'Not in Season'}</td>
                  <td className="px-4 py-2 border text-center">{plant.Temperature_Range ?? 'N/A'}</td>
                  <td className="px-4 py-2 border text-center">{plant.Minimum_Temperature_Tolerance ?? 'N/A'}</td>
                  <td className="px-4 py-2 border text-center">{plant.Maximum_Temperature_Tolerance ?? 'N/A'}</td>
                  <td className="px-4 py-2 border text-center">{plant.Frost_Sensitive ? 'Yes' : 'No'}</td>
                  <td className="px-4 py-2 border text-center">{getRecommendedPlantingDate(plant, frostDates?.lastSpringFrost, zone)}</td>
                  <td className="px-4 py-2 border text-center">{getRecommendedFallPlantingDate(plant, frostDates?.firstFallFrost, zone)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  )
}

export default PlantSelectorTable
