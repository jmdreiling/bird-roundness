import json
from pprint import pprint
from matplotlib import pyplot as plt
from PIL import Image
with open('eccentricity_dict.json', 'r') as source:
       eccentricity_dict = json.load(source)

values_list = [(key,val) for key, val in eccentricity_dict.items() if val != 'none found']
sorted_values_list = sorted(values_list, key=lambda item: item[1])
roundest_robin_pair = sorted_values_list[0]
roundest_robin_path= f"./{roundest_robin_pair[0]}"
print(roundest_robin_path)
image = Image.open(roundest_robin_path).convert("RGB")
plt.imshow(image)
plt.show()