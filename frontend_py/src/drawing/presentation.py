import os

import cv2
import numpy as np
from handtrackingmode import HandDetector


class Presentation:
    def __init__(
        self, width=1280, height=720, folder_path="Presentation", hs=120, ws=213
    ):
        self.width = width
        self.height = height
        self.folder_path = folder_path
        self.hs = hs
        self.ws = ws

        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, self.ws)
        self.cam.set(4, self.hs)

        self.path_slides = sorted(os.listdir(self.folder_path), key=len)
        self.slide_num = 0
        self.gesture_threshold = 300
        self.button_pressed = False
        self.button_counter = 0
        self.button_delay = 30
        self.annotations = [[]]
        self.annotation_number = -1
        self.annotation_start = False

        self.detector = HandDetector(detectionCon=0.8, maxHands=1)

    def process_gestures(self, hands, img):
        if hands and self.button_pressed is False:
            hand = hands[0]
            fingers = self.detector.fingersUp(hand)
            cx, cy = hand["center"]
            lm_list = hand["lmList"]

            x_val = int(np.interp(lm_list[8][0], [0, self.width // 4], [0, self.width]))
            y_val = int(
                np.interp(lm_list[8][1], [0, self.height - 500], [0, self.height])
            )
            index_finger = x_val, y_val

            if cy <= self.gesture_threshold:
                if fingers == [1, 0, 0, 0, 0]:
                    print("Left")
                    if self.slide_num > 0:
                        self.button_pressed = True
                        self.annotations = [[]]
                        self.annotation_number = -1
                        self.annotation_start = False
                        self.slide_num -= 1

                if fingers == [0, 0, 0, 0, 1]:
                    print("Right")
                    if self.slide_num < len(self.path_slides) - 1:
                        self.button_pressed = True
                        self.annotations = [[]]
                        self.annotation_number = -1
                        self.annotation_start = False
                        self.slide_num += 1

            if fingers == [0, 1, 1, 0, 0]:
                cv2.circle(img, index_finger, 12, (0, 0, 255), cv2.FILLED)

            if fingers == [0, 1, 0, 0, 0]:
                if self.annotation_start is False:
                    self.annotation_start = True
                    self.annotation_number += 1
                    self.annotations.append([])
                cv2.circle(img, index_finger, 12, (0, 0, 255), cv2.FILLED)
                self.annotations[self.annotation_number].append(index_finger)
            else:
                self.annotation_start = False

            if fingers == [0, 1, 1, 1, 1]:
                if self.annotations:
                    self.annotations.pop(-1)
                    self.annotation_number -= 1
                    self.button_pressed = True

    def run(self):
        while True:
            success, img = self.cam.read()
            img = cv2.flip(img, 1)
            img = cv2.line(
                img,
                (0, self.gesture_threshold),
                (self.width, self.gesture_threshold),
                (100, 255, 205),
                10,
            )

            path_full_slides = os.path.join(
                self.folder_path, self.path_slides[self.slide_num]
            )
            slide_current = cv2.imread(path_full_slides)

            hands, img = self.detector.findHands(img, flipType=False)

            self.process_gestures(hands, img)

            if self.button_pressed:
                self.button_counter += 1
                if self.button_counter > self.button_delay:
                    self.button_counter = 0
                    self.button_pressed = False

            for i in range(len(self.annotations)):
                for j in range(len(self.annotations[i])):
                    if j != 0:
                        cv2.line(
                            slide_current,
                            self.annotations[i][j - 1],
                            self.annotations[i][j],
                            (0, 255, 0),
                            12,
                        )

            img_small = cv2.resize(img, (self.ws, self.hs))
            h, w, _ = slide_current.shape
            slide_current[0 : self.hs, w - self.ws : w] = img_small

            cv2.imshow("Slides", slide_current)
            cv2.imshow("Image", img)

            key = cv2.waitKey(1)
            if key == ord("q"):
                break


if __name__ == "__main__":
    presentation = Presentation()
    presentation.run()
