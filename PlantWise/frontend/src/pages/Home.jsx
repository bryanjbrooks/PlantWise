// Description: Home page for the PlantWise frontend application.
// Notes:
// File: Home.jsx

import PlantSelectorTable from '../components/PlantSelectorTable'

function Home() {
  return (
    <div className="pt-12 w-full text-center">
      <h1 className="text-3xl font-bold mb-4">Welcome to PlantWise 🌱</h1>
      <p className="text-2xl mb-2">
        Helping you make smart planting decisions based on past and future weather.
      </p>
      <p className="text-2xl mb-6">
        Use the navigation above to view a list of all plants by type, create a custom list of plants, and find your climate zone
      </p>
      {/* <footer className="mt-8 text-center text-base text-gray-600">
        <p>Data is derived from the following sources:</p> 
        <p>Geocodio</p>
        <p>OpenWeather</p>
        <p>The PRISM Climate Group at Oregon State University</p>
        <p>The Old Farmer&apos;s Almanac</p>
        <p>UC Master Gardener Program</p>
      </footer> */}
    </div>
  )
}

export default Home;