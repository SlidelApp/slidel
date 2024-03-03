import cv2
import numpy as np


# Function to detect laser pointer position
def detect_laser(frame):
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range of red color in HSV
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize laser position
    laser_pos = None

    # If contours are found
    if contours:
        # Get the largest contour (assumed to be the laser pointer)
        largest_contour = max(contours, key=cv2.contourArea)

        # Get the centroid of the contour
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            laser_pos = (cx, cy)

    return laser_pos


# Main function
def main():
    # Open webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read frame from webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Detect laser pointer position
        laser_pos = detect_laser(frame)

        # If laser pointer is detected, draw a circle at its position
        if laser_pos:
            cv2.circle(frame, laser_pos, 5, (0, 255, 0), -1)

        # Display the frame
        cv2.imshow("Laser Detection", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
