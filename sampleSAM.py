import torch
from transformers import SamModel, SamProcessor, pipeline
from utility import show_boxes_on_image, show_masks_on_image, show_masks_on_image_scoreless
from PIL import Image
from matplotlib import pyplot as plt
from setupSAM import processor, device, model
import torch



source = "images/00badf24-fb37-402d-5aeb-d2e80c8a4300.jpg"
raw_image = Image.open(source).convert("RGB")
# generator = pipeline("mask-generation", model="facebook/sam-vit-huge", device="cpu")
# outputs = generator(raw_image, points_per_batch=64)
# masks = outputs["masks"]
# show_masks_on_image_scoreless(raw_image, masks)
# inputs = processor(raw_image, return_tensors="pt").to(device)
# image_embeddings = model.get_image_embeddings(inputs["pixel_values"])

# input_boxes = [[[650, 200, 0, 500]]]

# show_boxes_on_image(raw_image, input_boxes[0]) 


inference_state = processor.set_image(raw_image)
# Prompt the model with text
output = processor.set_text_prompt(state=inference_state, prompt="bird")

# Get the masks, bounding boxes, and scores
masks, boxes, scores = output["masks"], output["boxes"], output["scores"]
show_masks_on_image(raw_image=raw_image, masks=masks, scores=scores)


