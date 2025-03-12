// Description: Home page for the PlantWise frontend application.
// Notes:
// File: Home.jsx

import PlantSelectorTable from '../components/PlantSelectorTable'

function Home() {
  return (
    <div className="pt-12 w-full text-center">
      <h1 className="text-3xl font-bold mb-4">Welcome to PlantWise 🌱</h1>
      <p className="text-lg mb-2">
        Helping you make smart planting decisions based on past and future weather.
      </p>
      <p className="text-md mb-6">
        Use the navigation above to view a list of all plants by type.
      </p>

      <PlantSelectorTable />
    </div>
  )
}

export default Home;