import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

id = "0bcdce9d-29bf-4c92-4f78-a994e10c4000"
generic = f"./images/{id}.jpg"

image = cv.imread(generic, cv.IMREAD_COLOR_BGR)
print("loaded image")
lab = cv.cvtColor(image, cv.COLOR_RGB2LAB)
a_channel = lab[:,:,1]
th = cv.threshold(a_channel,127,255,cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
masked = cv.bitwise_and(image, image, mask = th)    # contains dark background
m1 = masked.copy()
m1[th==0]=(255,255,255)
m1_blurred = cv.medianBlur(m1, 13)
gray = cv.cvtColor(m1_blurred, cv.COLOR_RGBA2GRAY)
_, thresholded = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)
plt.imshow(thresholded, cmap = "grey")
plt.show()
