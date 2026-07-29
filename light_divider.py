import json
import cv2 as cv
# Opening JSON file
with open('meta_dict.json') as json_file:
    meta_dict_raw = json.load(json_file)

meta_dict = dict(meta_dict_raw)
# ids = meta_dict.keys()
# print(ids)
# daytime_ids = []
# nighttime_ids = []
# for k,v in meta_dict.items():
#     [time,meridiem] = v.get('time_date').split(" ")[1:]
#     hour = int(time.split(":")[0])
#     if meridiem == "AM":
#         if hour >= 7 and hour< 12:
#             daytime_ids.append(k)
#         else:
#             nighttime_ids.append(k)
#     else:
#         if hour >= 12 or hour <8:
#             daytime_ids.append(k)
#             nighttime_ids.append(k)

# print(len(daytime_ids))
# print(len(nighttime_ids))

# for id in ids:
#     img = cv.imread(f"images/{id}.jpg")
#     if id in daytime_ids:
#         cv.imwrite(f"images_light_divided/day/{id}.jpg", img )
#     else:
#         cv.imwrite(f"images_light_divided/night/{id}.jpg", img )


id = "4f2e851b-450a-4d3d-2f9b-8cdc3fda6600"
print(meta_dict.get(id))

## okay relative timing and daylight will be changing, I just need to know by how much....
## "winter-y months", daylight is less
## "summer-y months", daylight is greater

## Could I just divide them by how colorful they are..... THAT MIGHT DO IT.
