import map_utils
import api

x, y, z, area = map_utils.philamz_to_xyz(43, -15, 6)

api.getImage(x, y, z)

print(x, y, z, area)