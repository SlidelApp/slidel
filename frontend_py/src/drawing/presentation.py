import cv2 as cv
import numpy as np
import os
import handtrackingmode as htm

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
annotations = []


while True:
    success, img = cap.read()
    img = cv.flip(img, 1)
    pathFullImage = os.path.join(folderPath, pathImg[imgNum])
    imgCurrent = cv.imread(pathFullImage)

    # Adding webcam image in slide
    imgSmall = cv.resize(img, (ws, hs))
    h,w,_ = imgCurrent.shape
    imgCurrent[0:hs, 0:ws] = imgSmall

    handDetector = htm.HandDetector(detectionCon =0.7,maxHands=1)
    img = handDetector.findHands(img)
    hands = img
    fingers = handDetector.fingersUp(hands)

    if hands.size > 0:
        hands = hands[0]
        fingers = handDetector.fingersUp(hands)
        lmlst = hands["lmList"]
        indexFinger = lmlst[8][0], lmlst[8][1]
        print(fingers)

        xVal = int(np.interp(lmlst[8][0], [width // 2, width], [0, width]))
        yVal = int(np.interp(lmlst[8][1], [150, height - 150], [0, height]))
        indexFinger = xVal, yVal

        if (
            fingers[1] == 0
            and fingers[2] == 1
            and fingers[3] == 0
            and fingers[4] == 0
            and fingers[0] == 0
        ):
            cv.circle(img, indexFinger, 15, (0,0,255), cv.FILLED)
            annotations.append(indexFinger)
    


    for i, annotations in enumerate(annotations):
        cv.line(img, annotations[i-1], annotations[i], (0,0,255), 15)
    cv.imshow("Image", img)
    cv.imshow("Current Image", imgCurrent)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
