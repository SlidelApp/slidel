import cv2 as cv
import numpy as np

width, height = 1280, 720

# Capture video from webcam
cap = cv.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

while True:
    success, img = cap.read()
    cv.imshow("Image", img)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

