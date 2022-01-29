co = {"type": "Polygon", "coordinates": [
    [(14.414062500000007, 45.46013063792100),
     (14.414062500000007, 45.33670190996811),
     (14.589843750000000, 45.33670190996811),
     (14.589843750000000, 45.46013063792100)]]}
lon, lat = zip(*co['coordinates'][0])
from pyproj import Proj
pa = Proj("+proj=aea +lat_1=42.0 +lat2=47.0 +lon_0=14.5")

x, y = pa(lon, lat)
cop = {"type": "Polygon", "coordinates": [zip(x, y)]}
from shapely.geometry import shape
print(shape(cop).area / 1000000) # 268952044107.43506