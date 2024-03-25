import cv2
import numpy as np

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput


# Initialize the camera
camera = Picamera2()
capture_config = camera.create_video_configuration()
camera.configure(capture_config)
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = camera.capture_array()
# Allow the camera to warm up
time.sleep(0.1)

# Capture frames from the camera
while not key == ord("q"):
    camera.start_preview(Preview.QTGL)
    image = frame.array
    height, width = image.shape[:2]

    # Prepare the frame for YOLO (resizing and normalization)
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)

    # Set the blob as input to the YOLO network
    net.setInput(blob)

    # Run the YOLO inference
    detections = net.forward(output_layers)

    # Process the detections (e.g., draw bounding boxes, filter by confidence)
    for detection in detections:
        # Each detection includes the object class, confidence, and bounding box coordinates
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:  # Use a confidence threshold
            # Scale bounding box back to the size of the image
            box = detection[0:4] * np.array([width, height, width, height])
            (centerX, centerY, w, h) = box.astype("int")

            # Draw the bounding box on the image
            x = int(centerX - (w / 2))
            y = int(centerY - (h / 2))
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the processed image
    cv2.imshow("Image", image)
    key = cv2.waitKey(1) & 0xFF

    # Clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    
    # Break the loop if 'q' is pressed
    # if key == ord("q"):
		# break
		# camera.stop_preview()
		# camera.stop()
