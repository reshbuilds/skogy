
import config
import geopandas as gpd
import zipfile

file_path = config.file_path

# Read the spatial data in geopackage     
gdf = gpd.read_file(file_path,layer=None)
print(gdf.info())

