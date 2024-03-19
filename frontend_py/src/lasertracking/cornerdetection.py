import cv2
import numpy as np

class CornerDetection():

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
            cv2.circle(frame, (x,y), 5, (0, 0, 255), -1)
        return frame

    def tranformation_matrix(self, corners, frame):
        corners = []
        for i in corners:
            x, y = i.ravel()
            t = np.array([x, y])
            corners.append(t)
        return corners

    def process(self):
        vidcap = cv2.VideoCapture(1)
        success, frame = vidcap.read()
        while success:

            corners = self.detect_corners(frame, 4, 0.01, 10)
            frame = self.draw_corners(frame, corners)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        vidcap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    corner_detection = CornerDetection()
    corner_detection.process()
