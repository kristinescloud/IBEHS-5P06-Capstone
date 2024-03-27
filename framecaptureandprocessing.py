import cv2
import numpy as np
import keyboard
import time
from ultralytics import YOLO
import torch
import utils

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from PIL import Image as IM

##make this a thread

# Initialize the camera
camera = Picamera2(0)
capture_config = camera.create_video_configuration()
camera.configure(capture_config)
camera.resolution = (640, 480)
camera.framerate = 5

# Initialize the CalculateDepth class object
cd = CalculateDepth()

# Allow the camera to warm up
time.sleep(0.1)

camera.start()
#rawCapture = camera.capture_array()
#print(rawCapture)

# Capture frames from the camera
while True:
    print("test")
    #camera.start_preview(Preview.QTGL)
    rawCapture = camera.capture_array()
    image = rawCapture[:,:,:3]
    height, width = image.shape[:2]
    
    model = YOLO('yolov8n.pt')

# Perform inference on an image
    results = model(image, stream=True)
    detections = results

    # Process the detections (e.g., draw bounding boxes, filter by confidence)
    for detection in detections:
        print(f"detection starts here: {detection} the type is {type(detection)}")
        # Each detection includes the object class, confidence, and bounding box coordinates
        scores = detection.boxes.conf
        print(f"scores starts here: {scores} the type is {type(scores)}")
        class_id = np.argmax(scores[0])
        print(f"classid starts here: {class_id} the type is {type(class_id)}")
        confidence = scores[class_id]
        if confidence > 0.3:  # Use a confidence threshold
            # Scale bounding box back to the size of the image
            #box = detection.boxes.data.numpy() * np.array([width, height, width, height])
            boxes = detection.boxes
            #print(f"BOX starts here: {box} the type is {type(box)}")
            for box in boxes:
                ## add code to specify type of object that we want to analyze - conditional to filter out objects we don't care about"
                box_class = box.cls.numpy()[0]
                print("This box is a ", box_class) # for testing

                if cd.object_widths.get(box_class) == not None: # added to filter out some of YOLOs object classes
                    print("box is: ", box.xywh.numpy())
                    #print('Box '+str(box.id)+'\t Position: '+ str(box.xywhn.tolist()[0][0:2])+'\t Dimensions: '+ str(box.xywhn.tolist()[0][2:4]))
                    centerX = box.xywh.numpy().tolist()[0][0]
                    centerY = box.xywh.numpy().tolist()[0][1]
                    w = int(box.xywh.numpy().tolist()[0][2])
                    h = int(box.xywh.numpy().tolist()[0][3])                
                    # Draw the bounding box on the image
                    x = int(centerX - (w / 2))
                    y = int(centerY - (h / 2))
                    print(type(image))
                    print(image.shape)
                    depth = cd.calculate_depth(box_class, w)
                    cv2.rectangle(rawCapture, (x, y), (x + w, y + h), (0, 0, 0), 5)
                    label = 'Depth: '+ str(depth)+'  Position: ('+ str(x) + ', '+ str(y)+')  Dimensions: '+ str(w) + ', '+ str(h)+')'
                    cv2.putText(rawCapture, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                    # ~ cv2.rectangle(rawCapture, (10,10), (50,50), (0, 0, 0), 10)
    # ~ # Display the processed image
    cv2.imshow("Image", rawCapture)
    key = cv2.waitKey(1) & 0xFF
