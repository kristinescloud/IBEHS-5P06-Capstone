from ultralytics import YOLO

# Load a model
#model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8s.pt")  # load a pretrained model (recommended for training)

# Use the model
#model.train(data="coco128.yaml", epochs=3)  # train the model
#metrics = model.val()  # evaluate model performance on the validation set
results = model.predict("ultralytics/customer.jpg")  # predict on an image
#results = model.predict(source="0", show= True)
path = model.export(format="onnx")  # export the model to ONNX format
print(results)