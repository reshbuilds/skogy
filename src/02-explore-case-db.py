
import config
import geopandas as gpd
import sqlite3

file_path = config.file_path

# Read the geopackage database file
con = sqlite3.connect(file_path)
cur = con.cursor()
res = cur.execute("SELECT name FROM sqlite_master")
tables = res.fetchall()
print(tables)
