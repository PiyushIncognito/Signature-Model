import numpy as np
import cv2

# This code is used for simplest form of signature detection code

# Load image and HSV color threshold
image = cv2.imread('1.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([90, 38, 0])
upper = np.array([145, 255, 255])
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)
result[mask==0] = (255, 255, 255)

# Find contours on extracted mask, combine boxes, and extract ROI
cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = np.concatenate(cnts)
x,y,w,h = cv2.boundingRect(cnts)
cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
ROI = result[y:y+h, x:x+w]

# cv2.imshow('result', result)
# cv2.imshow('mask', mask)
# cv2.imshow('image', image)
# cv2.imshow('ROI', ROI)
path = "***/ GIVE THE FOLDER PATH TO SAVE THE IMAGES /***"

cv2.imwrite(path + "\result.jpg", result)
cv2.imwrite(path + "\mask.jpg", mask)
cv2.imwrite(path + "\image.jpg", image)
cv2.imwrite(path + "\ROI.jpg", ROI)

# cv2.waitKey()