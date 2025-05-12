// Description: Sources page with comprehensive image fallback for herbs and vegetables
// File: Sources.jsx

import { useEffect, useState } from 'react';

const tabNames = ['Hardiness Zone Maps', 'Plant Images', 'Planting Dates & Guides', 'Weather'];

const herbNames = [
  "basil", "bay leaf", "borage", "chive", "cilantro", "dill", "fennel", "ginger", "horseradish",
  "lavender", "lemon balm", "lemongrass", "marjoram", "mint", "oregano", "parsley", "rosemary",
  "sage", "tarragon", "thyme"
];

const vegetableNames = [
  "artichoke", "arugula", "asparagus", "avocado", "beet", "bock choy", "broccoli", "brussel sprouts",
  "cabbage", "carrot", "cauliflower", "celery", "chard", "chayote", "collards", "cucumber", "eggplant",
  "garlic", "green onion", "jicama", "kale", "kohlrabi", "leek", "lettuce", "mustard greens", "okra",
  "onion", "parsnip", "peas", "peppers", "potato", "pumpkin", "radicchio", "radish", "rhubarb", "rutabaga",
  "salsify", "shallot", "spinach", "sweet corn", "sweet potato", "tomatillo", "tomato", "turnip",
  "winter squash", "yam", "zucchini"
];

function Sources() {
  const [activeTab, setActiveTab] = useState(tabNames[0]);
  const [sources, setSources] = useState({
    'Hardiness Zone Maps': [],
    'Plant Images': [],
    'Planting Dates & Guides': [],
    'Weather': []
  });

  useEffect(() => {
    async function fetchAllSources() {
      try {
        const endpoints = {
          'Hardiness Zone Maps': 'sources/hardinessZones',
          'Plant Images': 'sources/plantImages',
          'Planting Dates & Guides': 'sources/plantingDatesGuides',
          'Weather': 'sources/weather'
        };

        const fetches = await Promise.all(
          Object.entries(endpoints).map(async ([key, url]) => {
            const res = await fetch(`/api/${url}`);
            const data = await res.json();
            return [key, data];
          })
        );

        setSources(Object.fromEntries(fetches));
      } catch (err) {
        console.error('Failed to load one or more source groups', err);
      }
    }

    fetchAllSources();
  }, []);

  const getLocalImagePath = (name, type) => {
    const fileName = name.replace(/\s+/g, '_') + '.jpeg';
    if (type === 'fruits' || type === 'herbs' || type === 'vegetables') {
      return `/${type}/${fileName}`;
    }

    const lower = name.toLowerCase();
    if (herbNames.some(h => lower.includes(h))) {
      return `/herbs/${fileName}`;
    } else if (vegetableNames.some(v => lower.includes(v))) {
      return `/vegetables/${fileName}`;
    } else {
      return `/fruits/${fileName}`;
    }
  };

  const renderSourceList = (category) => {
    const items = sources[category] || [];
    if (!items.length) return <p className="text-gray-600 italic">No sources found.</p>;

    if (category === 'Plant Images') {
      return (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {items.map((item, i) => {
            const localPath = getLocalImagePath(item.name, item.type);
            return (
              <div key={i} className="border rounded-lg shadow p-4 bg-white">
                <img src={localPath} alt={item.name} className="w-full h-40 object-cover rounded mb-2" />
                <h3 className="text-lg font-semibold">
                  <a href={item.image} target="_blank" rel="noopener noreferrer" className="text-blue-700 hover:underline">
                    {item.name}
                  </a>
                </h3>
                <p className="text-sm text-gray-600">{item.description}</p>
              </div>
            );
          })}
        </div>
      );
    }

    return (
      <ul className="space-y-4 mt-4">
        {items.map((src, i) => {
          const name = src.name || src.Name || 'Unnamed Source';
          const link = src.link || src.URL;
          const description = src.description || src.Source;
          const license = src.license || src.License;

          return (
            <li key={i} className="border-b pb-3">
              <p className="font-semibold">
                {link
                  ? <a href={link} target="_blank" rel="noopener noreferrer" className="text-blue-700 hover:underline">{name}</a>
                  : name}
              </p>
              {description && <p className="text-sm">{description}</p>}
              {license && <p className="text-xs text-gray-500">License: {license}</p>}
            </li>
          );
        })}
      </ul>
    );
  };

  return (
    <div className="max-w-6xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6 text-center">Data Sources</h1>
      <div className="flex gap-4 justify-center mb-6 flex-wrap">
        {tabNames.map((tab) => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={`px-4 py-2 border rounded-full text-sm font-semibold transition
              ${activeTab === tab ? 'bg-green-600 text-white' : 'bg-white text-green-800 border-green-600 hover:bg-green-100'}`}
          >
            {tab}
          </button>
        ))}
      </div>
      <div className="bg-white border rounded-lg p-4 shadow-sm">
        {renderSourceList(activeTab)}
      </div>
    </div>
  );
}

export default Sources;
