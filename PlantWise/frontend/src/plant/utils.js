// Description: Utility for building API endpoint URLs for individual plants

export function getPlantEndpoint(type, name) {
  const safeName = encodeURIComponent(name);
  switch (type) {
    case 'fruit':
      return `/fruits/getFruit?name=${safeName}`;
    case 'vegetable':
      return `/veg/getVegetable?name=${safeName}`;
    case 'herb':
      return `/herbs/getHerb?name=${safeName}`;
    default:
      throw new Error(`Unknown plant type: ${type}`);
  }
}

export function getImagePath(plantData) {
  const name =
    plantData.Fruit || plantData.Vegetable || plantData.Herb || plantData.Nut || 'default';
  const type = plantData.Fruit
    ? 'fruits'
    : plantData.Vegetable
    ? 'vegetables'
    : plantData.Herb
    ? 'herbs'
    : plantData.Nut
    ? 'nuts'
    : 'unknown';

  // Replace spaces with underscores but keep title casing, and use .jpeg
  const fileName = name.replace(/\s+/g, '_') + '.jpeg';
  return `/${type}/${fileName}`;
}