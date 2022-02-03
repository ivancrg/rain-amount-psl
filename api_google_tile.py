import requests
import cv2 as cv

# Downloads sattelite/terrain/map/hybrid
# image (map tile  (x, y) at zoom level z)
# it as image_name.png
# Display option - sattelite (s)
#                - hybrid (y)
#                - terrain (t)
#                - map (m)
def getImage(image_name, x, y, z, display_opt, width, height):
    if display_opt != 's' and display_opt != 'y' and display_opt != 't' and display_opt != 'm':
        return

    image_url = f"http://mt1.google.com/vt/lyrs={display_opt}&x={x}&y={y}&z={z}"
    print(image_url)

    image_data = requests.get(image_url).content

    with open(image_name, 'wb') as handler:
        handler.write(image_data)
    
    # Open and resize image
    image = cv.imread(image_name)
    dim = (width, height)
    image = cv.resize(image, dim, interpolation = cv.INTER_AREA)
    cv.imwrite(image_name, image)

# Testing
# getImage("tile.png", 17, 11, 5, "m", 150, 300)