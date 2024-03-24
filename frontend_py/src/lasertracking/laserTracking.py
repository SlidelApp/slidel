import os

import cv2 as cv
import numpy as np

cameraPath = "/dev/video0"
video = cv.VideoCapture()
video.open(cameraPath)

os.system(f"v4l2-ctl -d {cameraPath} -c gain_automatic=1")

whiteboard_size = (1920, 1080)

aruco_dict = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_50)
charuco_board = cv.aruco.CharucoBoard((8, 5), 0.04, 0.02, aruco_dict)
calibration_img = charuco_board.generateImage(whiteboard_size)

# detect the board for keystoning
charuco_detector = cv.aruco.CharucoDetector(charuco_board)
dest_corners, dest_IDs, dest_markers, dest_marker_IDs = charuco_detector.detectBoard(
    calibration_img
)

# sort the corners and ids so they match up
dest_IDs, dest_corners = zip(*sorted(zip(dest_IDs, dest_corners), key=lambda x: x[0]))
cv.namedWindow("camera", cv.WINDOW_NORMAL)

cv.namedWindow("whiteboard", cv.WINDOW_NORMAL)
cv.createTrackbar("brightness", "camera", 0, 255, lambda x: None)
cv.createTrackbar("threshold", "camera", 0, 255, lambda x: None)
# cv.namedWindow("camera", cv.WINDOW_NORMAL)
calibrating = True
H: np.ndarray = None

while calibrating:
    ret, frame = video.read()
    corners, ids, markers, marker_IDs = charuco_detector.detectBoard(frame)

    if ids is not None:
        cv.aruco.drawDetectedCornersCharuco(frame, corners, ids, (255, 0, 0))

    if ids is not None and len(ids) > 7:
        ids, corners = zip(*sorted(zip(ids, corners), key=lambda x: x[0]))
        workingDestCorners = [c for i, c in zip(dest_IDs, dest_corners) if i in ids]
        corners = np.array(corners)
        workingDestCorners = np.array(workingDestCorners)
        H, mask = cv.findHomography(corners, workingDestCorners)

    cv.imshow("camera", frame)
    cv.imshow("whiteboard", calibration_img)

    if cv.waitKey(1) == ord("q"):
        calibrating = False
        break
    if cv.waitKey(1) == ord("c"):
        if H is not None:
            calibrating = False
            break
        else:
            print("Calibration failed, not enough markers detected")
            continue

print("Calibration complete")

saved = np.full((whiteboard_size[1], whiteboard_size[0]), 255, dtype=np.uint8)
cv.createTrackbar("saving?", "whiteboard", 0, 1, lambda x: None)

while True:
    video.set(cv.CAP_PROP_BRIGHTNESS, cv.getTrackbarPos("brightness", "camera"))

    ret, frame = video.read()
    bw = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    _, bw = cv.threshold(
        bw, cv.getTrackbarPos("threshold", "camera"), 255, cv.THRESH_BINARY
    )

    render = cv.warpPerspective(bw, H, whiteboard_size)

    saved = cv.bitwise_and(saved, saved, mask=cv.bitwise_not(render))
    outline = np.full((whiteboard_size[1], whiteboard_size[0]), 0, dtype=np.uint8)
    cv.rectangle(outline, (0, 0, whiteboard_size[0], whiteboard_size[1]), 255, 25)
    outline = cv.warpPerspective(
        outline, H, frame.shape[:2][::-1], flags=cv.WARP_INVERSE_MAP
    )
    bw = bw + outline
    if cv.getTrackbarPos("saving?", "whiteboard") == 0:
        saved = np.full((whiteboard_size[1], whiteboard_size[0]), 255, dtype=np.uint8)

    cv.imshow("whiteboard", saved)
    cv.imshow("camera", bw)
    if cv.waitKey(1) == ord("q"):
        break

cv.destroyAllWindows()
video.release()
