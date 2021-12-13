import numpy as np
import matplotlib.pyplot as plt

from common import get_data, do_folds

points = do_folds(*get_data(), stop_at_first=False)
pixels = np.zeros((max(p[1] for p in points) + 1,
                   max(p[0] for p in points) + 1))
for x, y in points:
    pixels[y][x] = 1
plt.axis('off')
plt.imshow(pixels, cmap='Greys')
plt.show()
