import json
from pprint import pprint
from matplotlib import pyplot as plt
from PIL import Image
with open('eccentricity_dict.json', 'r') as source:
       eccentricity_dict = json.load(source)

values_list = [(key,val) for key, val in eccentricity_dict.items() if val != 'none found']
sorted_values_list = sorted(values_list, key=lambda item: item[1])
roundest_bird_pair = sorted_values_list[4]
roundest_bird_path= f"./{roundest_bird_pair[0]}"
print(roundest_bird_path)
print(roundest_bird_pair)
image = Image.open(roundest_bird_path).convert("RGB")
plt.imshow(image)
plt.show()