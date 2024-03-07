from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Perform inference on an image
results = model('/Users/kristizzle/Desktop/IBEHS-5P06-Capstone/YOLO/ultralytics/person.mp4', stream=True)

# Extract bounding boxes, classes, names, and confidences
## boxes = results[0].boxes.xyxy.tolist()
## classes = results[0].boxes.cls.tolist()
## names = results[0].names
## confidences = results[0].boxes.conf.tolist()

for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    for box in boxes:
        print('Box '+str(box.id)+'\t XYWH '+ str(box.xywh))
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification output
    #result.show()  # display to screen
    #result.save(filename='result.jpg')  # save to disk

## for box in boxes:
    ## print('Box {} is {} in xywh format', box.id, box.xywh)