import os

import cv2
import numpy as np
from handtrackingmode import HandDetector

# Parameters
# TODO: Get image height and width dynamically
width, height = 1920, 1080
FolderPath = "Presentation"  # Directory in which Presentation Slides are kept
hs, ws = 120, 213

# Cam_Setup

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, ws)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, hs)
webcam_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
webcam_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Presentation_Slides -> Getting the list of the slide names and sorting them according to
# their length [ length of the slide name ]
# sorted_fuction
pathSlides = sorted(os.listdir(FolderPath), key=len)
# print(pathSlides)

# Variables
SlideNum = 0
gestureThreshold = 250
button_pressed = False
button_counter = 0
button_delay = 30
annotations = [[]]
annotation_number = 0
annotation_start = False

# Hand_Detector
# Here, detectionCon = the code will run if it is 80% of the oblect being a hand.
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:  # noqa
    success, img = cam.read()
    # To flip the img 1= horizontal , 0= vertical ; but here right becomes left and vice versa.
    img = cv2.flip(img, 1)
    img = cv2.line(
        img, (0, gestureThreshold), (width, gestureThreshold), (100, 255, 205), 10
    )

    # Here FolderPath is the Project Directory
    pathFullSlides = os.path.join(FolderPath, pathSlides[SlideNum])
    SlideCurrent = cv2.imread(pathFullSlides)

    # cv2.flip( var, 1) + flipType = False == Perfectly flipped img.
    hands, img = detector.findHands(
        img, flipType=False
    )  # flipType = Flase it will nt flip the img. right will remain right and vice versa.

    if hands and button_pressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand["center"]
        # land_mark_list
        lm_list = hand["lmList"]

        # Constrain Region for pointer to be a small square on right side
        # np.interp(variable[fitting-size],[actual_size])
        width_margin = webcam_width * 0.1
        x_val = int(np.interp(lm_list[8][0], [ webcam_width // 2, webcam_width - width_margin ], [0, width]))
        height_margin = webcam_height * 0.2
        y_val = int(np.interp(lm_list[8][1], [height_margin, webcam_height - height_margin], [0, height]))
        index_finger = x_val, y_val

        if cy <= gestureThreshold:  # If hand is above the gestureThreshold
            # Gesture-0 Left
            if fingers == [1, 0, 0, 0, 0]:
                print("Left")

                if SlideNum > 0:
                    button_pressed = True
                    annotations = [[]]
                    annotation_number = 0
                    annotation_start = False

                    SlideNum -= 1

            # Gesture-1 Right
            if fingers == [0, 0, 0, 0, 1]:
                print("Right")
                if SlideNum < len(pathSlides) - 1:
                    button_pressed = True
                    annotations = [[]]
                    annotation_number = 0
                    annotation_start = False

                    SlideNum += 1

        # Gesture-3 Pointer
        if fingers == [0, 1, 1, 0, 0]:
            cv2.circle(SlideCurrent, index_finger, 12, (0, 0, 255), cv2.FILLED)

        # Gesture-4 Draw
        if fingers == [0, 1, 0, 0, 0]:
            if annotation_start is False:
                annotation_start = True
                annotation_number += 1
                annotations.append([])
            cv2.circle(SlideCurrent, index_finger, 12, (0, 0, 255), cv2.FILLED)
            annotations[annotation_number].append(index_finger)
        else:
            annotation_start = False

        # Gesture-5
        if fingers == [0, 1, 1, 1, 1]:
            if annotations:
                annotations.pop(-1)
                annotation_number -= 1
                button_pressed = True

        # Gesture - 6
        # if fingers == [1,1,1,1,0]:

    # Button_Pressed itreation
    if button_pressed:
        button_counter += 1
        if button_counter > button_delay:
            button_counter = 0
            button_pressed = False

    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                cv2.line(
                    SlideCurrent,
                    annotations[i][j - 1],
                    annotations[i][j],
                    (0, 255, 0),
                    12,
                )

    # Adding WebCam Img to the Slide
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = SlideCurrent.shape
    SlideCurrent[0:hs, w - ws : w] = imgSmall

    cv2.namedWindow('Slides', cv2.WINDOW_NORMAL)
    cv2.imshow("Slides", SlideCurrent)
    cv2.imshow("Image", img)

    Key = cv2.waitKey(1)
    if Key == ord("q"):
        break
