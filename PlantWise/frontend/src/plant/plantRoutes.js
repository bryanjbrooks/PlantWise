// Description: Helper for building frontend URLs for plant detail pages

export function getPlantPath(type, name) {
  const safeName = encodeURIComponent(name);
  return `/plant/${type}/${safeName}`;
}