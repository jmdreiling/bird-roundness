from extraneous.utility import show_boxes_on_image, show_masks_on_image
from PIL import Image

raw_image = Image.open("images/00badf24-fb37-402d-5aeb-d2e80c8a4300.jpg").convert("RGB")

input_boxes = [[[650, 200, 0, 500]]]

show_boxes_on_image(raw_image, input_boxes[0])  