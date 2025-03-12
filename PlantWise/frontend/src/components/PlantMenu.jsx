// Description: Menu for the PlantWise frontend application.
// Notes:
// File: PlantMenu.jsx

import PropTypes from 'prop-types'

function PlantMenu({ selected, onSelect }) {
  const options = ["fruits", "herbs", "vegetables"]

  return (
    <div className="flex justify-center gap-4 my-4">
      {options.map((type) => (
        <button
          key={type}
          onClick={() => onSelect(type)}
          className={`px-4 py-2 rounded shadow-md font-semibold capitalize transition
            ${selected === type ? 'bg-green-600 text-white' : 'bg-gray-200 text-gray-800'}`}
        >
          {type}
        </button>
      ))}
    </div>
  )
}

PlantMenu.propTypes = {
  selected: PropTypes.string.isRequired,
  onSelect: PropTypes.func.isRequired
}

export default PlantMenu;