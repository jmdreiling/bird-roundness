import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

id = "0bcdce9d-29bf-4c92-4f78-a994e10c4000"
generic = f"./images/{id}.jpg"

image = cv.imread(generic, cv.IMREAD_COLOR_BGR)
print("loaded image")
imageBlurred = cv.medianBlur(image, 5)
print("blurred")
cv.imshow("Blurred", imageBlurred)
cv.waitKey(0)
cv.destroyAllWindows()
## Hue might be helpful here.





# thresh_h = cv.(image_hsv[:, :, 0])

# thresh_s = threshold_otsu(image_hsv[:, :, 1])

# # mask the image to get determine which pixels with hue and saturation above their thresholds

# mask_h = image_hsv[:, :, 1] > thresh_h

# mask_s = image_hsv[:, :, 1] > thresh_s

# # combine the masks with an OR so any pixel above either threshold counts as foreground

# np_mask = np.logical_or(mask_h, mask_s)

# # apply morphological transforms

# for mt in self.morph_transform:

#     np_mask = mt(np_mask)

# return np_mask
image_hsv = cv.cvtColor(imageBlurred, cv.COLOR_RGB2HSV)
image_hsv = imageBlurred


# use Otsu's method to find the thresholds for hue and saturation
_, thresh_h = cv.threshold(image_hsv[:, :, 1],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
_, thresh_s = cv.threshold(image_hsv[:, :, 1],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# mask the image to get determine which pixels with hue and saturation above their thresholds
mask_h = image_hsv[:, :, 1] > thresh_h
# mask_s = image_hsv[:, :, 1] > thresh_s

# combine the masks with an OR so any pixel above either threshold counts as foreground
# np_mask = np.logical_or(mask_h, mask_s)

# apply morphological transforms
# for mt in self.morph_transform:
kernel = np.ones((3, 3), np.uint8)
thresholded = cv.morphologyEx(mask_h.astype(np.uint8), cv.MORPH_CLOSE, kernel)
# thresholded = 255-thresholded
plt.imshow(thresholded, cmap="gray")
plt.show()
print("THRESHOLDED")