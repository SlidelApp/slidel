import cv2 as cv
import numpy as np
import os
import handtrackingmodel as htm
width, height = 1280, 720

# Capture video from webcam
cap = cv.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Get the list of presentation images
folderPath = "Presentation"
pathImg = sorted(os.listdir(folderPath), key=len)   
print(pathImg)

# Variables
imgNum = 0
hs,ws = int(120*1), int(213*1) 
gestureThreadshold = 300
while True:
    success, img = cap.read()
    img = cv.flip(img, 1)
    pathFullImage = os.path.join(folderPath, pathImg[imgNum])
    imgCurrent = cv.imread(pathFullImage)

    # Adding webcam image in slide
    imgSmall = cv.resize(img, (ws, hs))
    h,w,_ = imgCurrent.shape
    imgCurrent[0:hs, 0:ws] = imgSmall

    handDetector = htm.HandDetector(detection_confidence=0.7,max_hands=1)
    img = handDetector.findHands(img)
    hands = img

    if hands.size > 0:
        hands = hands[0]
        fingers = handDetector.figersUp(hands)
        print(fingers)
        cv.line(img(0,gestureThreadshold), (width,gestureThreadshold), (0,0,255), 10)

    cv.imshow("Image", img)
    cv.imshow("Current Image", imgCurrent)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
