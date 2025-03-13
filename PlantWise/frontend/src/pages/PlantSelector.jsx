// Description: Select wanted plants and display them in a table.
// Notes:
// File: PlantSelectorTable.jsx

import PlantSelectorTable from '../components/PlantSelectorTable';

function PlantSelector() {
  return (
    <div className="pt-12 w-full text-center">
      <h1 className="text-3xl font-bold mb-4">Browse All Plants</h1>
      <PlantSelectorTable />
      <footer className="mt-8 text-center text-base text-gray-600">
        <p>Data is derived from the following sources:</p> 
        <p>Geocodio</p>
        <p>OpenWeather</p>
        <p>The PRISM Climate Group at Oregon State University</p>
        <p>The Old Farmer&apos;s Almanac</p>
        <p>UC Master Gardener Program</p>
      </footer>
    </div>
  );
}

export default PlantSelector;