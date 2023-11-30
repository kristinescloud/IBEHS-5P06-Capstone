import cv2
import urllib.request
import json
import pprint

camera_id = 0
delay = 1
window_name = 'OpenCV Barcode'

bd = cv2.barcode.BarcodeDetector()
cap = cv2.VideoCapture(camera_id)

barcodes = dict()
maxfreq = -1
api_key = "q3y9hoyobzs2mwr6boi9ewqphylmv8"

while sum(barcodes.values()) < 50:
    ret, frame = cap.read()

    if ret:
        ret_bc, decoded_info, decode_type, points = bd.detectAndDecodeWithType(frame)
        if ret_bc:
            frame = cv2.polylines(frame, points.astype(int), True, (0, 255, 0), 3)
            for s, p in zip(decoded_info, points):
                if s:
                    if barcodes.get(s, 0) == 0:
                        barcodes.update({s: 1})
                    else:
                        barcodes[s] = barcodes.get(s, 0) + 1
                    print(s)
                    frame = cv2.putText(frame, s, p[1].astype(int),
                                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)

for key in barcodes:
    if barcodes[key] > maxfreq:
        maxfreq = barcodes[key]
        maxfreqkey = key

detectedbarcode = maxfreqkey

print("The decoded barcode number is "+detectedbarcode)

url = "https://api.barcodelookup.com/v3/products?barcode="+detectedbarcode+"&formatted=y&key="+api_key
print(url,"\n")

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

barcode = data["products"][0]["barcode_number"]
print ("Barcode Number: ", barcode)
title = data["products"][0]["title"]
print ("Title: ", title)
brand = data["products"][0]["brand"]
print ("Brand: ", brand)
description = data["products"][0]["description"]
print ("Description: ", description)
manufacturer = data["products"][0]["manufacturer"]
print ("Manufacturer: ", manufacturer)
ingredients = data["products"][0]["ingredients"]
print ("Ingredients: ", ingredients)
nutrition_facts = data["products"][0]["nutrition_facts"]
print ("Nutrition Facts: ", nutrition_facts, "\n")

print ("Entire Response:")
pprint.pprint(data)
