import cv2 as cv
img = cv.imread("/Users/kristizzle/Desktop/IBEHS-5P06-Capstone/gocart--name-in-dev/Screenshot 2023-10-23 at 3.50.49 PM.png")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window