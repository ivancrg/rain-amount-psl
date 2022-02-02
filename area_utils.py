from pyproj import Geod

# Returns square polygon area based on given coordinates
# Result in m^2

def getArea(latmin, latmax, lonmin, lonmax):
    geod = Geod('+a=6378137 +f=0.0033528106647475126')

    # print(f"{latmin}, {lonmin}")
    # print(f"{latmin}, {lonmax}")
    # print(f"{latmax}, {lonmax}")
    # print(f"{latmax}, {lonmin}")

    lats = [latmin, latmin, latmax, latmax]
    lons = [lonmin, lonmax, lonmax, lonmin]

    poly_area, poly_perimeter = geod.polygon_area_perimeter(lons, lats)

    poly_area = abs(poly_area)

    #print("area: {} , perimeter: {}".format(poly_area, poly_perimeter))
    # print(poly_area)
    
    return poly_area

# Alternative code, sometimes didn't work

# co = {"type": "Polygon", "coordinates": [
#     [(45.089035564831015,  5.625000000000013),
#      (45.089035564831015, 11.249999999999993),
#      (48.922499263758255, 11.249999999999993),
#      (48.922499263758255,  5.62500000000001)]]}

#     #  45.089035564831015, 5.625000000000013, 48.922499263758255, 11.249999999999993
# lon, lat = zip(*co['coordinates'][0])
# from numpy import poly
# from pyproj import Proj
# pa = Proj("+proj=aea +lat_1=42.0 +lat2=47.0 +lon_0=10")

# x, y = pa(lon, lat)
# cop = {"type": "Polygon", "coordinates": [zip(x, y)]}
# from shapely.geometry import shape
# print(shape(cop).area / 1000000) # 268952044107.43506