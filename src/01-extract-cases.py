
import config
import geopandas as gpd
import zipfile

zip_path = config.file_path
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    for file_info in zip_ref.infolist():
        if file_info.filename.endswith('.gpkg'):
            geopkg_in_zip_path = f"zip://{zip_path}!{file_info.filename}"
            break

# Read the spatial data in geopackage     
gdf = gpd.read_file(geopkg_in_zip_path,layer=None)
print(gdf.info())

