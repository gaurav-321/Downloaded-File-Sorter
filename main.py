import os
import math
import numpy as np

import cv2

img_loc = [os.path.join("wallpapers", x) for x in os.listdir("wallpapers")]
for img in img_loc:
    frame = cv2.imread(img)
    avg_color_per_row = np.average(frame, axis=0)
    vg_color = np.average(avg_color_per_row, axis=0)
    b, g, r = vg_color
    luma = math.sqrt(0.299 * r ^ 2 + 0.587 * g ^ 2 + 0.114 * b ^ 2)
    print(luma)
