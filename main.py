from pathlib import Path
from grounding_dino_SAM_funcs import grounded_segmentation, fit_ellipse_mask, get_eccentricity
from transformer_loading import segmentator, processor, object_detector
from tqdm import tqdm
import json
p = Path(".")
list_images = sorted((p.glob('images_light/day/*.jpg')))
shortened_list = [str(l) for l in list_images[:10]]
str_list =[str(l) for l in list_images]

mask_dictionary = {}

for image in tqdm(str_list):
    image_array, detections = grounded_segmentation(
    image=image,
    labels=["bird"],
    polygon_refinement=True,
    segmentator=segmentator,
    processor=processor,
    object_detector=object_detector)
    if detections == "none found":
        mask_dictionary.update({image: "none found"})
    else:
        mask_dictionary.update({image: detections})


eccentricity_dict = {}
for key, value in mask_dictionary.items():
    if value == "none found":
        eccentricity_dict.update({key:value})
    else:
        mask_copy = value[0].mask.copy()
        minEllipse = fit_ellipse_mask(mask_copy=mask_copy)
        for ellipse in minEllipse:
            e = get_eccentricity(ellipse)
            print(e)
        eccentricity_dict.update({key:e})

with open("eccentricity_dict.json", "w") as file: 
        json.dump(eccentricity_dict, file)
