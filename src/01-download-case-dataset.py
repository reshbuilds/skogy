import config
import requests
import zipfile

# Download case dataset, and save it
url = 'https://geodpags.skogsstyrelsen.se/geodataport/data/sksAvverkAnm_gpkg.zip'
resp = requests.get(url)
save_path = config.zip_file_path
with open(save_path, 'wb') as f:
    f.write(resp.content)

# Extract the zip file
with zipfile.ZipFile(save_path, 'r') as zip_ref:
     zip_ref.extractall(config.file_loc)
