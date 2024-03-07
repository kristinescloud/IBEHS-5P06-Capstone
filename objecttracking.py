from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load an official detection model
## model = YOLO('yolov8n-seg.pt')  # load an official segmentation model
## model = YOLO('path/to/best.pt')  # load a custom model

# Track with the model
results = model.track(source='/Users/kristizzle/Desktop/IBEHS-5P06-Capstone/YOLO/ultralytics/person.mp4', show=True)
## results = model.track(source=0, show=True, tracker="bytetrack.yaml")