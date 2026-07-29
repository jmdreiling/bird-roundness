from pathlib import Path
from grounding_dino_SAM_funcs import grounded_segmentation, fit_ellipse_mask, get_eccentricity
from transformer_loading import segmentator, processor, object_detector
from tqdm import tqdm
import json
p = Path(".")
list_images = sorted((p.glob('organized_data/day/*.jpg')))
shortened_list = [str(l) for l in list_images[:10]]
str_list =[str(l) for l in list_images]

with open('eccentricity_dict.json', 'r') as source:
       json_dict = json.load(source)

e_keys = json_dict.keys()
print(e_keys)
subset= [entry for entry in str_list if entry not in e_keys]

eccentricity_dict = {}

for image in tqdm(subset):
    image_array, detections = grounded_segmentation(
    image=image,
    labels=["bird"],
    polygon_refinement=True,
    segmentator=segmentator,
    processor=processor,
    object_detector=object_detector)
    if detections == "none found":
        eccentricity_dict.update({image: "none found"})
        with open("eccentricity_dict.json", "w") as file: 
                    json.dump(eccentricity_dict, file)
    else:
        mask_copy = detections[0].mask.copy()
        minEllipse = fit_ellipse_mask(mask_copy=mask_copy)
        for ellipse in minEllipse:
            e = get_eccentricity(ellipse)
            eccentricity_dict.update({image:e})
        with open("eccentricity_dict.json", "w") as file: 
            json.dump(eccentricity_dict, file)
        
with open("eccentricity_dict.json", "w") as file: 
    json.dump(eccentricity_dict, file)

