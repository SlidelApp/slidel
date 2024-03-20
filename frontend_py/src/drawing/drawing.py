import numpy as np
import cv2 as cv
from handtrackingmodel import *
import handtrackingmodel as htm

cap = cv.VideoCapture(0)
detector = htm.HandDetector(detection_confidence=0.85)

while True:
    sucess, img = cap.read()
    img = cv.flip(img, 1)
    
    img = detector.findHands(img)
    lmlist = detector.findpositions(img,draw=False)

    if lmlist != 0:
        print(lmlist)
        x1, y1 = lmlist[8][1:]


    cv.imshow("Image", img)
     

    if cv.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv.destroyAllWindows()
