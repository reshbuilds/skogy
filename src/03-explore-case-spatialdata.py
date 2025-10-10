
import config
import geopandas as gpd

file_path = config.file_path

# Read the spatial data in geopackage database file    
gdf = gpd.read_file(file_path,layer=None)
print(gdf.info())

