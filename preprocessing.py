import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import statistics as stats

def single_test(id, color):
    generic = f"./images/{id}.jpg"
    img = cv.imread(generic, cv.IMREAD_COLOR_BGR)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hues  = hsv[:,:,0]
    sat = hsv[:,:,1]
    val = hsv[:,:,2]
    flat_hues = hues.flatten()
    print(np.std(flat_hues))
    plt.hist(hues, color = color, alpha = .6)

day_id = "0bcdce9d-29bf-4c92-4f78-a994e10c4000" ## daytime image
night_id = "4f2e851b-450a-4d3d-2f9b-8cdc3fda6600"

single_test(night_id,  color = "black")
single_test(day_id, color = "green")
plt.show()

# hist_h = cv.calcHist([night_hues],[0],None,[256],[0,256])
#hist_s = cv2.calcHist([s],[0],None,[256],[0,256])
#hist_v = cv2.calcHist([v],[0],None,[256],[0,256])
# plt.plot(hist_h, color='r', label="hue")
# plt.show()
# lab = cv.cvtColor(image, cv.COLOR_RGB2LAB)
# a_channel = lab[:,:,1]
# th = cv.threshold(a_channel,127,255,cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
# masked = cv.bitwise_and(image, image, mask = th)    # contains dark background
# m1 = masked.copy()
# m1[th==0]=(255,255,255)
# m1_blurred = cv.medianBlur(m1, 13)
# gray = cv.cvtColor(m1_blurred, cv.COLOR_RGBA2GRAY)
# _, thresholded = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)
# plt.imshow(thresholded, cmap = "grey")
# plt.show()
