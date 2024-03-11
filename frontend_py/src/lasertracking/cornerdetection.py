import cv2
import numpy as np

class CornerDetection():
    def __init__(self):
        self.vidcap = cv2.VideoCapture(0)


    def detect_corners(self, frame, max_corners, quality_level, min_distance):
    
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect the corners in the frame
        corners = cv2.goodFeaturesToTrack(
                gray, maxCorners=max_corners, qualityLevel=quality_level, minDistance=min_distance
            )

        corners = np.int0(corners)
        
        return corners
    
    def draw_corners(self, frame, corners):
        for i in corners:
            x, y = i.ravel()
            cv2.circle(frame, (x, y), 3, 255, -1)
        return frame
    

