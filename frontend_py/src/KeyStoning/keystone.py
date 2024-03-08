import cv2
import numpy as np


def main():
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

        # Calculate keystone correction
        X, Y = keystone_correction(
            np.mean([pts1[0][0], pts1[1][0], pts1[2][0], pts1[3][0]]),
            np.mean([pts1[0][1], pts1[1][1], pts1[2][1], pts1[3][1]]),
            pts1[0][0],
            pts1[0][1],
            pts1[1][0],
            pts1[1][1],
            pts1[2][0],
            pts1[2][1],
            pts1[3][0],
            pts1[3][1],
        )

        # Apply transformation matrix
        M = np.float32([[1, 0, X], [0, 1, Y]])
        keystone_corrected_frame = cv2.warpAffine(
            frame, M, (frame.shape[1], frame.shape[0])
        )

        # Display the frame
        cv2.imshow("Original Frame", frame)
        cv2.imshow("Keystone Corrected Frame", keystone_corrected_frame)

        if cv2.waitKey(1) == 27:
            break


def calculate_transformation_coefficients(x0, y0, x1, y1, x2, y2, x3, y3):
    delta_x0 = x0 - x2
    delta_x1 = x1 - x2
    delta_y0 = y0 - y2
    delta_y1 = y1 - y2

    sum_x = x1 + x3 - x0 - x2
    sum_y = y1 + y3 - y0 - y2

    denominator_gh = delta_x0 * delta_y1 - delta_x1 * delta_y0
    determinant_g = np.linalg.det([[sum_x, delta_x1], [sum_y, delta_y1]])
    determinant_h = np.linalg.det([[delta_x0, sum_x], [delta_y0, sum_y]])

    g = determinant_g / denominator_gh
    h = determinant_h / denominator_gh

    a = x2 - x1 + g * x2
    b = x3 - x1 + h * x3
    c = x1
    d = y2 - y1 + g * y2
    e = y3 - y1 + h * y3
    f = y1

    return a, b, c, d, e, f, g, h


def keystone_correction(
    x, y, x0, y0, x1, y1, x2, y2, x3, y3, resolution_width=1024, resolution_height=768
):
    a, b, c, d, e, f, g, h = calculate_transformation_coefficients(
        x0, y0, x1, y1, x2, y2, x3, y3
    )

    denominator = (h * x - g) * y + a * h - b * g

    u = ((e - f * h) * x + (c * h - b) * y + b * f - c * e) / denominator
    v = ((f * g - d) * x + (a - c * g) * y + c * d - a * f) / denominator

    X = u * resolution_width
    Y = v * resolution_height

    return X, Y


if __name__ == "__main__":
    main()
