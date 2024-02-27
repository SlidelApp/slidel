import cv2
import numpy as np

vidcap = cv2.VideoCapture("VID_20240226_123808.mp4")
success, image = vidcap.read()

while success:
    success, image = vidcap.read()
    frame = cv2.resize(image, (720, 480))
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    # Detect the corners
    corners = cv2.goodFeaturesToTrack(gray, 4, 0.01, 10)
    corners = np.int0(corners)

    # Specify the coordinates of the 4 corners of the trapezoid
    pts1 = []
    for corner in corners:
        x, y = corner.ravel()
        t = (x, y)
        pts1.append(t)

    cv2.circle(frame, pts1[0], 5, (0, 0, 255), -1)
    cv2.circle(frame, pts1[1], 5, (0, 0, 255), -1)
    cv2.circle(frame, pts1[2], 5, (0, 0, 255), -1)
    cv2.circle(frame, pts1[3], 5, (0, 0, 255), -1)

    pts1 = np.float32(pts1)
    pts2 = np.float32([[0, 0], [720, 0], [720, 480], [0, 480]])

    # Compute the perspective transform matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    transformed = cv2.warpPerspective(frame, matrix, (720, 480))

    cv2.imshow("Original Frame", frame)
    cv2.imshow("Transformed Frame", transformed)

    if cv2.waitKey(1) == 27:
        break
