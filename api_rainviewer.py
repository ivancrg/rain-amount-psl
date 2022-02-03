from urllib.request import urlopen
import json
import requests

# Downloads radar image (map tile
# (x, y) at zoom level z) and saves
# it as image_name.png
def getImage(image_name, x, y, z):
    settings_url = "https://api.rainviewer.com/public/weather-maps.json"
    settings_response = urlopen(settings_url)
    settings = json.loads(settings_response.read())

    # UNIX tamestamp based on RainViewer data
    timestamp = settings['radar']['past'][5]['path']

    image_url = f"https://tilecache.rainviewer.com{timestamp}/512/{z}/{x}/{y}/1/0_0.png"
    print(image_url)

    # TESTING
    #image_url = "https://tilecache.rainviewer.com/v2/radar/1643832600/512/6/33/22/1/0_0.png"

    image_data = requests.get(image_url).content

    with open(image_name, 'wb') as handler:
        handler.write(image_data)