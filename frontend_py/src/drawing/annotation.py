import os
import threading
import time

import cv2
import numpy as np
from flask import Flask, Response
from handtrackingmode import HandDetector

from slidel.gesture_detection.gesture_classifier import HandGestureClassifier

# Parameters
# TODO: Get image height and width dynamically
width, height = 1920, 1080
FolderPath = "Presentation"  # Directory in which Presentation Slides are kept
hs, ws = 120, 213

app = Flask(__name__)
# Cam_Setup


class CameraEvent:
    """An Event-like class that signals all active clients when a new frame is
    available.
    """

    def __init__(self):
        self.events = {}

    def wait(self):
        """Invoked from each client's thread to wait for the next frame."""
        ident = threading.get_ident()
        if ident not in self.events:
            # this is a new client
            # add an entry for it in the self.events dict
            # each entry has two elements, a threading.Event() and a timestamp
            self.events[ident] = [threading.Event(), time.time()]
        return self.events[ident][0].wait()

    def set(self):
        """Invoked by the camera thread when a new frame is available."""
        now = time.time()
        remove = None
        for ident, event in self.events.items():
            if not event[0].isSet():
                # if this client's event is not set, then set it
                # also update the last set timestamp to now
                event[0].set()
                event[1] = now
            else:
                # if the client's event is already set, it means the client
                # did not process a previous frame
                # if the event stays set for more than 5 seconds, then assume
                # the client is gone and remove it
                if now - event[1] > 5:
                    remove = ident
        if remove:
            del self.events[remove]

    def clear(self):
        """Invoked from each client's thread after a frame was processed."""
        self.events[threading.get_ident()][0].clear()


class BaseCamera:
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera
    event = CameraEvent()

    def __init__(self):
        """Start the background camera thread if it isn't running yet."""
        if BaseCamera.thread is None:
            BaseCamera.last_access = time.time()

            # start background frame thread
            BaseCamera.thread = threading.Thread(target=self._thread)
            BaseCamera.thread.start()

            # wait until first frame is available
            BaseCamera.event.wait()

    def get_frame(self):
        """Return the current camera frame."""
        BaseCamera.last_access = time.time()

        # wait for a signal from the camera thread
        BaseCamera.event.wait()
        BaseCamera.event.clear()

        return BaseCamera.frame

    @staticmethod
    def frames():
        """ "Generator that returns frames from the camera."""
        raise RuntimeError("Must be implemented by subclasses.")

    @classmethod
    def _thread(cls):
        """Camera background thread."""
        print("Starting camera thread.")
        frames_iterator = cls.frames()
        for frame in frames_iterator:
            BaseCamera.frame = frame
            BaseCamera.event.set()  # send signal to clients
            time.sleep(0)

            # if there hasn't been any clients asking for frames in
            # the last 60 seconds then stop the thread
            if time.time() - BaseCamera.last_access > 60:
                frames_iterator.close()
                print("Stopping camera thread due to inactivity.")
                break
        BaseCamera.thread = None


class Camera(BaseCamera):
    video_source = 0

    def __init__(self):
        if os.environ.get("OPENCV_CAMERA_SOURCE"):
            Camera.set_video_source(int(os.environ["OPENCV_CAMERA_SOURCE"]))
        super().__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():  # noqa C901
        cam = cv2.VideoCapture(Camera.video_source)

        # cam = cv2.VideoCapture(0)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, ws)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, hs)
        # sometimes depending on the webcam the above won't set
        webcam_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
        webcam_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Presentation_Slides -> Getting the list of the slide names and sorting them according to
        # their length [ length of the slide name ]
        # sorted_fuction
        pathSlides = sorted(os.listdir(FolderPath), key=len)
        # print(pathSlides)

        # Variables
        SlideNum = 0
        gesture_threshold = int(webcam_height * 0.65)
        button_pressed = False
        button_counter = 0
        button_delay = 30
        annotations = [[]]
        annotation_number = 0
        annotation_start = False

        # Hand_Detector
        # Here, detectionCon = the code will run if it is 80% of the oblect being a hand.
        detector = HandDetector(detectionCon=0.8, maxHands=1)
        hand_gesture_classifier = HandGestureClassifier()

        while True:  # noqa
            success, img = cam.read()
            # To flip the img 1= horizontal , 0= vertical ; but here right becomes left and vice versa.
            img = cv2.flip(img, 1)
            img = cv2.line(
                img,
                (0, gesture_threshold),
                (width, gesture_threshold),
                (100, 255, 205),
                10,
            )

            # Here FolderPath is the Project Directory
            pathFullSlides = os.path.join(FolderPath, pathSlides[SlideNum])
            SlideCurrent = cv2.imread(pathFullSlides)

            # cv2.flip( var, 1) + flipType = False == Perfectly flipped img.
            hands, img, hand_landmarks = detector.findHands(
                img, flipType=False
            )  # flipType = Flase it will nt flip the img. right will remain right and vice versa.
            if hand_landmarks:
                hand_sign_id = hand_gesture_classifier(img, hand_landmarks)

            if hands and button_pressed is False:
                hand = hands[0]
                fingers = detector.fingersUp(hand)
                cx, cy = hand["center"]
                # land_mark_list
                lm_list = hand["lmList"]

                # Constrain Region for pointer to be a small square on right side
                # np.interp(variable[fitting-size],[actual_size])
                width_margin = webcam_width * 0.1
                x_val = int(
                    np.interp(
                        lm_list[8][0],
                        [webcam_width // 2, webcam_width - width_margin],
                        [0, width],
                    )
                )
                height_margin = webcam_height * 0.2
                y_val = int(
                    np.interp(
                        lm_list[8][1],
                        [height_margin, webcam_height - height_margin],
                        [0, height],
                    )
                )
                index_finger = x_val, y_val

                if cy <= gesture_threshold:  # If hand is above the gesture_threshold
                    # Gesture-0 Left
                    if hand_sign_id == "prev" or fingers == [0, 0, 0, 0, 0]:
                        print("Left")

                        if SlideNum > 0:
                            button_pressed = True
                            annotations = [[]]
                            annotation_number = 0
                            annotation_start = False

                            SlideNum -= 1

                    # Gesture-1 Right
                    if hand_sign_id == "next" or fingers == [0, 0, 0, 0, 1]:
                        print("Right")
                        if SlideNum < len(pathSlides) - 1:
                            button_pressed = True
                            annotations = [[]]
                            annotation_number = 0
                            annotation_start = False

                            SlideNum += 1

                # Gesture-3 Pointer
                if hand_sign_id == "pointer" or fingers == [1, 1, 0, 0, 0]:
                    cv2.circle(SlideCurrent, index_finger, 12, (0, 0, 255), cv2.FILLED)

                # Gesture-4 Draw
                if hand_sign_id == "draw" or fingers == [0, 1, 0, 0, 0]:
                    if annotation_start is False:
                        annotation_start = True
                        annotation_number += 1
                        annotations.append([])
                    cv2.circle(SlideCurrent, index_finger, 12, (0, 0, 255), cv2.FILLED)
                    annotations[annotation_number].append(index_finger)
                else:
                    annotation_start = False

                # Gesture-5
                if hand_sign_id == "erase" or fingers == [0, 1, 1, 0, 0]:
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

            # cv2.namedWindow("Slides", cv2.WINDOW_NORMAL)
            cv2.imshow("Slides", SlideCurrent)
            # cv2.imshow("Image", img)

            Key = cv2.waitKey(1)
            if Key == ord("q"):
                break

            # slideMedium = cv2.resize(SlideCurrent, (720, 480))
            ret, buffer = cv2.imencode(".jpg", SlideCurrent)
            frame = buffer.tobytes()
            yield frame


def generate_frames(camera):
    """Video streaming generator function."""
    yield b"--frame\r\n"
    while True:
        frame = camera.get_frame()
        yield b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n--frame\r\n"


@app.route("/video_feed")
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(
        generate_frames(Camera()), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(host="localhost", port="5000")
