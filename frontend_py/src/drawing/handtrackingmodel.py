import time

import cv2 as cv
import mediapipe as mp


class HandDetector:

    def __init__(
        self,
        mode=False,
        max_hands=2,
        model_complexity=1,
        detection_confidence=0.5,
        tracking_confidence=0.5,
    ):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence
        self.model_complexity = model_complexity

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode,
            self.max_hands,
            self.model_complexity,
            self.detection_confidence,
            self.tracking_confidence,
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.tipId = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGRA2RGB)
        self.result = self.hands.process(imgRGB)

        # print(result.multi_hand_landmarks)
        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, handLms, self.mpHands.HAND_CONNECTIONS
                    )

        return img

    def draw_landmarks(image, landmark_point):  # noqa C901

        if len(landmark_point) > 0:

            cv.line(
                image, tuple(landmark_point[2]), tuple(landmark_point[3]), (0, 0, 0), 6
            )
            cv.line(
                image,
                tuple(landmark_point[2]),
                tuple(landmark_point[3]),
                (255, 255, 255),
                2,
            )
            cv.line(
                image, tuple(landmark_point[3]), tuple(landmark_point[4]), (0, 0, 0), 6
            )
            cv.line(
                image,
                tuple(landmark_point[3]),
                tuple(landmark_point[4]),
                (255, 255, 255),
                2,
            )

            cv.line(
                image, tuple(landmark_point[5]), tuple(landmark_point[6]), (0, 0, 0), 6
            )
            cv.line(
                image,
                tuple(landmark_point[5]),
                tuple(landmark_point[6]),
                (255, 255, 255),
                2,
            )
            cv.line(
                image, tuple(landmark_point[6]), tuple(landmark_point[7]), (0, 0, 0), 6
            )
            cv.line(
                image,
                tuple(landmark_point[6]),
                tuple(landmark_point[7]),
                (255, 255, 255),
                2,
            )
            cv.line(
                image, tuple(landmark_point[7]), tuple(landmark_point[8]), (0, 0, 0), 6
            )
            cv.line(
                image,
                tuple(landmark_point[7]),
                tuple(landmark_point[8]),
                (255, 255, 255),
                2,
            )

            cv.line(
                image, tuple(landmark_point[9]), tuple(landmark_point[10]), (0, 0, 0), 6
            )
            cv.line(
                image,
                tuple(landmark_point[9]),
                tuple(landmark_point[10]),
                (255, 255, 255),
                2,
            )
            cv.line(
                image,
                tuple(landmark_point[10]),
                tuple(landmark_point[11]),
                (0, 0, 0),
                6,
            )
            cv.line(
                image,
                tuple(landmark_point[10]),
                tuple(landmark_point[11]),
                (255, 255, 255),
                2,
            )
            cv.line(
                image,
                tuple(landmark_point[11]),
                tuple(landmark_point[12]),
                (0, 0, 0),
                6,
            )
            cv.line(
                image,
                tuple(landmark_point[11]),
                tuple(landmark_point[12]),
                (255, 255, 255),
                2,
            )

            cv.line(
                image,
                tuple(landmark_point[13]),
                tuple(landmark_point[14]),
                (0, 0, 0),
                6,
            )
            cv.line(
                image,
                tuple(landmark_point[13]),
                tuple(landmark_point[14]),
                (255, 255, 255),
                2,
            )
            cv.line(
                image,
                tuple(landmark_point[14]),
                tuple(landmark_point[15]),
                (0, 0, 0),
                6,
            )
            cv.line(
                image,
                tuple(landmark_point[14]),
                tuple(landmark_point[15]),
                (255, 255, 255),
                2,
            )
            cv.line(
                image,
                tuple(landmark_point[15]),
                tuple(landmark_point[16]),
                (0, 0, 0),
                6,
            )
            cv.line(
                image,
                tuple(landmark_point[15]),
                tuple(landmark_point[16]),
                (255, 255, 255),
                2,
            )

            cv.line(
                image,
                tuple(landmark_point[17]),
                tuple(landmark_point[18]),
                (0, 0, 0),
                6,
            )
            cv.line(
                image,
                tuple(landmark_point[17]),
                tuple(landmark_point[18]),
                (255, 255, 255),
                2,
            )
            cv.line(
                image,
                tuple(landmark_point[18]),
                tuple(landmark_point[19]),
                (0, 0, 0),
                6,
            )
            cv.line(
                image,
                tuple(landmark_point[18]),
                tuple(landmark_point[19]),
                (255, 255, 255),
                2,
            )
            cv.line(
                image,
                tuple(landmark_point[19]),
                tuple(landmark_point[20]),
                (0, 0, 0),
                6,
            )
            cv.line(
                image,
                tuple(landmark_point[19]),
                tuple(landmark_point[20]),
                (255, 255, 255),
                2,
            )

            cv.line(
                image, tuple(landmark_point[0]), tuple(landmark_point[1]), (0, 0, 0), 6
            )
            cv.line(
                image,
                tuple(landmark_point[0]),
                tuple(landmark_point[1]),
                (255, 255, 255),
                2,
            )
            cv.line(
                image, tuple(landmark_point[1]), tuple(landmark_point[2]), (0, 0, 0), 6
            )
            cv.line(
                image,
                tuple(landmark_point[1]),
                tuple(landmark_point[2]),
                (255, 255, 255),
                2,
            )
            cv.line(
                image, tuple(landmark_point[2]), tuple(landmark_point[5]), (0, 0, 0), 6
            )
            cv.line(
                image,
                tuple(landmark_point[2]),
                tuple(landmark_point[5]),
                (255, 255, 255),
                2,
            )
            cv.line(
                image, tuple(landmark_point[5]), tuple(landmark_point[9]), (0, 0, 0), 6
            )
            cv.line(
                image,
                tuple(landmark_point[5]),
                tuple(landmark_point[9]),
                (255, 255, 255),
                2,
            )
            cv.line(
                image, tuple(landmark_point[9]), tuple(landmark_point[13]), (0, 0, 0), 6
            )
            cv.line(
                image,
                tuple(landmark_point[9]),
                tuple(landmark_point[13]),
                (255, 255, 255),
                2,
            )
            cv.line(
                image,
                tuple(landmark_point[13]),
                tuple(landmark_point[17]),
                (0, 0, 0),
                6,
            )
            cv.line(
                image,
                tuple(landmark_point[13]),
                tuple(landmark_point[17]),
                (255, 255, 255),
                2,
            )
            cv.line(
                image, tuple(landmark_point[17]), tuple(landmark_point[0]), (0, 0, 0), 6
            )
            cv.line(
                image,
                tuple(landmark_point[17]),
                tuple(landmark_point[0]),
                (255, 255, 255),
                2,
            )

        for index, landmark in enumerate(landmark_point):
            if index == 0:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 1:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 2:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 3:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 4:
                cv.circle(image, (landmark[0], landmark[1]), 8, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 8, (0, 0, 0), 1)
            if index == 5:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 6:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 7:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 8:
                cv.circle(image, (landmark[0], landmark[1]), 8, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 8, (0, 0, 0), 1)
            if index == 9:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 10:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 11:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 12:
                cv.circle(image, (landmark[0], landmark[1]), 8, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 8, (0, 0, 0), 1)
            if index == 13:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 14:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 15:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 16:
                cv.circle(image, (landmark[0], landmark[1]), 8, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 8, (0, 0, 0), 1)
            if index == 17:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 18:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 19:
                cv.circle(image, (landmark[0], landmark[1]), 5, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 5, (0, 0, 0), 1)
            if index == 20:
                cv.circle(image, (landmark[0], landmark[1]), 8, (255, 255, 255), -1)
                cv.circle(image, (landmark[0], landmark[1]), 8, (0, 0, 0), 1)

        return image

    def findpositions(self, img, handNo=0, draw=True):

        lmList = []
        if self.result.multi_hand_landmarks:
            myhand = self.result.multi_hand_landmarks[handNo]

            for Id, lm in enumerate(myhand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                lmList.append([Id, cx, cy])

        return lmList

    def figersUp(self, lmlist):
        fingers = []

        if lmlist[self.tipId[0]][1] > lmlist[self.tipId[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if lmlist[self.tipId[id]][2] < lmlist[self.tipId[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers


def main():
    pTime = 0
    cTime = 0
    cap = cv.VideoCapture(0)
    detector = HandDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlst = detector.findpositions(img)
        print(lmlst)
        # img = detector.draw_landmarks(img, lmlst)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv.putText(
            img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_TRIPLEX, 3, (255, 0, 255), 3
        )

        cv.imshow("Hand Tracking", img)
        cv.waitKey(1) & 0xFF == ord("q")


if __name__ == "__main__":
    main()
