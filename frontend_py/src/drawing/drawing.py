import numpy as np
import cv2 as cv
from handtrackingmodel import *
import handtrackingmodel as htm

cap = cv.VideoCapture(0)
detector = htm.HandDetector(detection_confidence=0.85)
drawcolor = (0, 0, 255)
erasecolor = (0, 0, 0)
brushthickness = 15
xp, yp = 0, 0
imgcanvas = np.zeros((480, 640, 3), np.uint8)

while True:
    sucess, img = cap.read()
    img = cv.flip(img, 1)

    img = detector.findHands(img)
    lmlist = detector.findpositions(img,draw=False)

    if len(lmlist) != 0:
        # print(lmlist)
        x1, y1 = lmlist[8][1], lmlist[8][2]
        x2, y2 = lmlist[12][1], lmlist[12][2]

        fingers = detector.figersUp(lmlist)
        # print(fingers)

        if (
            fingers[1] == 0 
            and fingers[2] == 1 
            and fingers[3] == 0 
            and fingers[4] == 0 
            and fingers[0] == 0):
            
            if xp == 0 and yp == 0:
                xp, yp = x2, y2

            cv.line(img, (xp, yp), (x2, y2), drawcolor, brushthickness)
            cv.line(imgcanvas, (xp, yp), (x2, y2), drawcolor, brushthickness)
            xp, yp = x2, y2

        if (
            fingers[1] == 1
            and fingers[2] == 0
            and fingers[3] == 0
            and fingers[4] == 0
            and fingers[0] == 0
        ):
            
            cv.circle(img, (x1, y1), 15,drawcolor, cv.FILLED)

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            cv.line(img, (xp, yp), (x1, y1), drawcolor, brushthickness)
            cv.line(imgcanvas, (xp, yp), (x1, y1), drawcolor, brushthickness)
            xp, yp = x1, y1

    imggray = cv.cvtColor(imgcanvas, cv.COLOR_BGR2GRAY)
    _, imginv = cv.threshold(imggray, 50, 255, cv.THRESH_BINARY_INV)
    img = cv.bitwise_and(img, img, mask=imginv)
    img = cv.bitwise_or(img, imgcanvas)
    cv.imshow("Image", img)
    cv.imshow("Canvas", imgcanvas)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv.destroyAllWindows()
