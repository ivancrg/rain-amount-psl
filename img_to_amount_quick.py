import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import PIL

img = cv.imread("s2.png")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# resize image
# dim = (1920, 1080)
#img = cv.resize(img, dim, interpolation = cv.INTER_AREA)

print(f'Image shape: {img.shape}')

img_px_cnt = img.shape[0] * img.shape[1]
print(f'Image pixel count: {img_px_cnt}')

img = img.reshape(-1, 3)

unique, counts = np.unique(img, axis=0, return_counts=True)

# print(unique.shape)
# print(unique)
# print(counts.shape)
# print(counts)

unique_counts = sorted(zip(unique, counts), key=lambda x : x[1], reverse=True)

for uc in unique_counts:
    percentage = uc[1] / img_px_cnt * 100
    print(f'{uc[0]}\t{uc[1]}\t{round(percentage, 2)}%')
    
    if percentage < 1: break