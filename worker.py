import img_utils
import map_utils
import api

def get_liters_per_hour(phi, lam, zoom):
    x, y, z, area = map_utils.philamz_to_xyz(phi, lam, zoom)
    
    api.getImage("s.png", x, y, z)
    
    return img_utils.img_to_amount("s.png", area)

print(get_liters_per_hour(52.127610, 27.766357, 4))