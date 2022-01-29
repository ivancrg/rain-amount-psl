from os import write
import numpy as np

f = open("output_colors.csv", "a")

# ref = np.array([0, 32, 64, 128, 192, 224, 256])
ref = np.array([0, 64, 128, 192, 256])

for r in range(1, ref.size):
    for g in range(1, ref.size):
        for b in range(1, ref.size):
            f.write(f'{ref[r - 1] + (ref[r] - ref[r - 1]) / 2},{ref[g - 1] + (ref[g] - ref[g - 1]) / 2},{ref[b - 1] + (ref[b] - ref[b - 1]) / 2}\n')

# close the file
f.close()