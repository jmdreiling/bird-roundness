import json
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# Opening JSON file
with open('meta_dict.json') as json_file:
    meta_dict_raw = json.load(json_file)

meta_dict = dict(meta_dict_raw)
ids = list(meta_dict.keys())
for id in ids:
    generic = f"./images/{id}.jpg"
    img = cv.imread(generic, cv.IMREAD_COLOR_BGR)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hues  = hsv[:,:,0]
    sat = hsv[:,:,1]
    val = hsv[:,:,2]
    flat_hues = hues.flatten()
    if np.std(flat_hues) < 30:
        cv.imwrite(f"./images_light/night/{id}.jpg", img)
    else:
        cv.imwrite(f"./images_light/day/{id}.jpg", img)