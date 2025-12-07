import geopandas as gpd

world = gpd.read_file("ne_10m_admin_0_countries.shp")

# Add a 'visited' flag for visited countries
visited_iso_a3 = {
    "KHM",
    "CHN",
    "GEO",
    "IDN",
    "JPN",
    "MYS",
    "PHL",
    "SGP",
    "KOR",
    "THA",
    "UZB",
    "VNM",
    "CAN",
    "USA",
    "BRA",
    "AUT",
    "CZE",
    "FRA",
    "DEU",
    "GRC",
    "HUN",
    "ITA",
    "PRT",
    "ESP",
    "CHE",
    "VAT",
    "AUS",
    "NZL",
    "BRN",
}  # replace with your visited countries

iso_col = "ADM0_A3"

# simpler: if iso present
if iso_col in world.columns:
    world['visited'] = world[iso_col].apply(lambda x: x in visited_iso_a3)
else:
    world['visited'] = False

# Save to GeoJSON for D3 to consume
out_geojson = "countries_with_visited.geojson"
world.to_file(out_geojson, driver="GeoJSON")
print(f"Wrote {out_geojson} — openable by D3/TopoJSON/GeoJSON tools.")