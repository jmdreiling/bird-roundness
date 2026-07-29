from grounding_dino_SAM_funcs import torch, AutoModelForMaskGeneration, AutoProcessor,pipeline

detector_id = "IDEA-Research/grounding-dino-tiny"
device = "cuda" if torch.cuda.is_available() else "cpu"
detector_id = detector_id if detector_id is not None else "IDEA-Research/grounding-dino-tiny"
object_detector = pipeline(model=detector_id, task="zero-shot-object-detection", device=device)
## THIS LOADS WEIGHTS!
segmenter_id = "facebook/sam-vit-base"
device = "cuda" if torch.cuda.is_available() else "cpu"
segmenter_id = segmenter_id if segmenter_id is not None else "facebook/sam-vit-base"

segmentator = AutoModelForMaskGeneration.from_pretrained(segmenter_id).to(device)
processor = AutoProcessor.from_pretrained(segmenter_id)

