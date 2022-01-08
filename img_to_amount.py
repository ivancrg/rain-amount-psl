import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
import numpy as np
import csv

# returns the bin number that corresponds to the pixel's color
def color_to_hist(pxr, pxg, pxb):
    # ref = np.array([0, 32, 64, 128, 192, 224, 256])
    ref = np.array([0, 64, 128, 192, 256])

    for r in range(1, ref.size):
        for g in range(1, ref.size):
            for b in range(1, ref.size):
                if (ref[r - 1] <= pxr and pxr < ref[r]) and (ref[g - 1] <= pxg and pxg < ref[g]) and (ref[b - 1] <= pxb and pxb < ref[b]):
                    # print(f'r {pxr} g {pxg} b {pxb}: {(r - 1) * 16 + (g - 1) * 4 + (b - 1)}')
                    return (r - 1) * 16 + (g - 1) * 4 + (b - 1)

def get_histogram_frequencies(img):
    s_h = np.zeros(64) # 4^4

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    nimg = img.ravel()

    # print(img)
    # print(nimg)
    # print(nimg.shape[0])
    # print(np.arange(0, nimg.shape[0] - 3 + 1, 3))
    
    for i in np.arange(0, nimg.shape[0] - 3 + 1, 3):
        s_h[color_to_hist(nimg[i], nimg[i + 1], nimg[i + 2])] += 1


    # n = img.shape[0]
    # m = img.shape[1]

    # for i in range(0, n):
    #     for j in range(0, m):
    #         s_h[color_to_hist(s_h, img[i][j][0], img[i][j][1], img[i][j][2])] += 1
    
    return s_h


# reading histogram bin colors from csv and normalizing them
histogram_colors = []
histogram_file = open('histogram_colors.csv')
csvreader = csv.reader(histogram_file)
for row in csvreader:
    histogram_colors.append((float(row[0]) / 255.0, float(row[1]) / 255.0, float(row[2]) / 255.0))

# displaying the screenshot
fig = plt.figure()
img = cv2.imread('./s2.png')
#img = cv2.resize(img, (100, 100), interpolation=cv2.INTER_AREA)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_copy = img
r, g, b = cv2.split(img) # splitting pixels to r, g, b
plt.imshow(img)

# adding a subplot
fig = plt.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d")

# every pixel needs to be put at his location by RGB values
# every pixel's RGB values need to be normalized (0-255 -> 0-1)
# for facecolors parameter of matplotlib Scatter method
# facecolors parameter also has to be a list, not a NP array
pixel_colors = img.reshape((np.shape(img)[0] * np.shape(img)[1], 3)) # reshape (num_of_px, 3 (RGB))
norm = colors.Normalize(vmin=-1., vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()

# plotting 3D graph
axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("R")
axis.set_ylabel("G")
axis.set_zlabel("B")

# spectrum_histogram - array that stores histogram bin values across all colors
spectrum_histogram = get_histogram_frequencies(img_copy)

# plotting the histogram
fig, ax = plt.subplots(figsize=(8,4), facecolor='w')
ax.bar(range(1, 65), spectrum_histogram, color=histogram_colors)

plt.show()