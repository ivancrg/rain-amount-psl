import cv2 as cv
import numpy as np
import math

# Threshold used during RGB comparisons
THRESHOLD = 20

# Loading CSV data for converting RGB to dbZ
DATA = np.loadtxt('./dZzavg_color_CPo.csv', comments='%', delimiter=',', encoding='utf8', skiprows=1)
dbZRGB = DATA[1:, :]

# Converting dbZ value to meters
# (standard is mm, but area is in m^2)
def dbz_to_mph(dbz):
    # Converting dbZ to mm/h
    mmph = ((10 ** (dbz / 10)) / (200)) ** (5 / 8)

    # Converting to m/h
    mph = mmph / 1000

    return mph

# For color comparison purposes
def rgb_diff(r1, g1, b1, r2, g2, b2):
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

# Converting pixel's RGB to
# meters of rain
def rgb_to_mph(r, g, b):
    if r == 0 and g == 0 and b == 0:
        return 0

    # Initializing to something small, something big
    dbz = -100
    rgb_difference = 500

    for i in range(len(dbZRGB)):
        ith_rgb_diff = rgb_diff(r, g, b, dbZRGB[i][1], dbZRGB[i][2], dbZRGB[i][3])
        
        if rgb_difference > ith_rgb_diff:
            rgb_difference = ith_rgb_diff
            dbz = dbZRGB[i][0]

    if rgb_difference < THRESHOLD:
        return dbz_to_mph(dbz)
    
    return 0

def img_to_amount(img_name, area):
    img = cv.imread(img_name)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Resize image
    # dim = (1920, 1080) # resize width, resize height
    # img = cv.resize(img, dim, interpolation = cv.INTER_AREA)

    # Reshaping the image
    img_px_cnt = img.shape[0] * img.shape[1]
    img = img.reshape(-1, 3)

    # Ordering found colors (not necessary,
    # but maybe for presentation purposes?)
    unique, counts = np.unique(img, axis=0, return_counts=True)
    unique_counts = sorted(zip(unique, counts), key=lambda x : x[1], reverse=True)

    # Liters of rainfall per hour
    liters_per_hour = 0
    
    # Looping over found colors
    for uc in unique_counts:
        # Percentage of color in image
        percentage = uc[1] / img_px_cnt * 100

        # Adding color's 'contribution' to lph
        liters_per_hour += percentage / 100 * area * rgb_to_mph(uc[0][0], uc[0][1], uc[0][2])

        # print(f'{uc[0]}\t{uc[1]}\t{round(percentage, 2)}%')
    
    return liters_per_hour