import cv2 as cv
import handtrackingmodel as htm
import numpy as np
from handtrackingmodel import *


class HandDrawing:
    def __init__(self):
        self.cap = cv.VideoCapture(0)
        self.detector = htm.HandDetector(detection_confidence=0.85)
        self.drawcolor = (0, 0, 255)
        self.erasecolor = (0, 0, 0)
        self.brushthickness = 15
        self.xp, self.yp = 0, 0
        self.imgcanvas = np.zeros((480, 640, 3), np.uint8)

    def draw(self):
        while True:
            sucess, img = self.cap.read()
            img = cv.flip(img, 1)

            img = self.detector.findHands(img)
            lmlist = self.detector.findpositions(img, draw=False)

            if len(lmlist) != 0:
                x1, y1 = lmlist[8][1], lmlist[8][2]
                x2, y2 = lmlist[12][1], lmlist[12][2]

                fingers = self.detector.figersUp(lmlist)

                if (
                    fingers[1] == 0
                    and fingers[2] == 1
                    and fingers[3] == 0
                    and fingers[4] == 0
                    and fingers[0] == 0
                ):

                    if self.xp == 0 and self.yp == 0:
                        self.xp, self.yp = x2, y2

                    cv.line(
                        img,
                        (self.xp, self.yp),
                        (x2, y2),
                        self.drawcolor,
                        self.brushthickness,
                    )
                    cv.line(
                        self.imgcanvas,
                        (self.xp, self.yp),
                        (x2, y2),
                        self.drawcolor,
                        self.brushthickness,
                    )
                    self.xp, self.yp = x2, y2

                if (
                    fingers[1] == 1
                    and fingers[2] == 0
                    and fingers[3] == 0
                    and fingers[4] == 0
                    and fingers[0] == 0
                ):

                    cv.circle(img, (x1, y1), 15, self.drawcolor, cv.FILLED)

                    if self.xp == 0 and self.yp == 0:
                        self.xp, self.yp = x1, y1

                    cv.line(
                        img,
                        (self.xp, self.yp),
                        (x1, y1),
                        self.drawcolor,
                        self.brushthickness,
                    )
                    cv.line(
                        self.imgcanvas,
                        (self.xp, self.yp),
                        (x1, y1),
                        self.drawcolor,
                        self.brushthickness,
                    )
                    self.xp, self.yp = x1, y1

            imggray = cv.cvtColor(self.imgcanvas, cv.COLOR_BGR2GRAY)
            _, imginv = cv.threshold(imggray, 50, 255, cv.THRESH_BINARY_INV)
            img = cv.bitwise_and(img, img, mask=imginv)
            img = cv.bitwise_or(img, self.imgcanvas)
            cv.imshow("Image", img)
            cv.imshow("Canvas", self.imgcanvas)

            if cv.waitKey(1) & 0xFF == ord("q"):
                break

        self.cap.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    handDrawing = HandDrawing()
    handDrawing.draw()
