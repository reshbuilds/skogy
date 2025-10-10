import config
import requests

# Download case dataset, and save it
url = 'https://geodpags.skogsstyrelsen.se/geodataport/data/sksAvverkAnm_gpkg.zip'
resp = requests.get(url)
save_path = config.file_path
with open(save_path, 'wb') as f:
    f.write(resp.content)
