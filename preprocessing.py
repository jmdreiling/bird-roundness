import cv2 as cv
import numpy as np

id = "0a3e933f-8961-4091-418d-2b99cb77ab00"
generic = f"./images/{id}.jpg"

image = cv.imread(generic, cv.IMREAD_COLOR_RGB)
print("loaded image")
imageBlurred = cv.medianBlur(image, 3)
print("blurred")
gray = cv.cvtColor(imageBlurred, cv.COLOR_RGBA2GRAY)
print('grayed')
detector = cv.SimpleBlobDetector_create()
_, thresholded = cv.threshold(gray, 170, 255, cv.THRESH_BINARY)
keypoints = detector.detect(thresholded)
# Draw blobs as red circles
output = cv.drawKeypoints(thresholded, keypoints, np.array([]), (0, 0, 255),
                           cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show the output
cv.imshow("Blobs Detected", output)
cv.waitKey(0)
cv.destroyAllWindows()