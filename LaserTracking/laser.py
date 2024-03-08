import sys
import argparse
import cv2
import numpy as np


class LaserTracker(object):

    def __init__(
        self,
        cam_width=640,
        cam_height=480,
        hue_min=20,
        hue_max=160,
        sat_min=100,
        sat_max=255,
        val_min=200,
        val_max=256,
        display_thresholds=False,
    ):

        self.cam_width = cam_width
        self.cam_height = cam_height
        self.hue_min = hue_min
        self.hue_max = hue_max
        self.sat_min = sat_min
        self.sat_max = sat_max
        self.val_min = val_min
        self.val_max = val_max
        self.display_thresholds = display_thresholds

        self.capture = None
        self.channels = {
            "hue": None,
            "saturation": None,
            "value": None,
            "laser": None,
        }

        self.previous_position = None
        self.trail = np.zeros((self.cam_height, self.cam_width, 3), np.uint8)

    def create_and_position_window(self, name, xpos, ypos):
        cv2.namedWindow(name)
        cv2.resizeWindow(name, self.cam_width, self.cam_height)
        cv2.moveWindow(name, xpos, ypos)

    def setup_camera_capture(self, device_num=0):
        try:
            device = int(device_num)
            sys.stdout.write(f"Using Camera Device: {device}\n")
        except (IndexError, ValueError):
            device = 0
            sys.stderr.write("Invalid Device. Using default device 0\n")

        self.capture = cv2.VideoCapture(device)
        if not self.capture.isOpened():
            sys.stderr.write("Failed to Open Capture device. Quitting.\n")
            sys.exit(1)

        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.cam_width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.cam_height)
        return self.capture

    def handle_quit(self, delay=10):
        key = cv2.waitKey(delay)
        c = chr(key & 255)
        if c in ["c", "C"]:
            self.trail = np.zeros((self.cam_height, self.cam_width, 3), np.uint8)
        if c in ["q", "Q", chr(27)]:
            sys.exit(0)

    def threshold_image(self, channel):
        if channel == "hue":
            minimum = self.hue_min
            maximum = self.hue_max
        elif channel == "saturation":
            minimum = self.sat_min
            maximum = self.sat_max
        elif channel == "value":
            minimum = self.val_min
            maximum = self.val_max

        (t, tmp) = cv2.threshold(
            self.channels[channel], maximum, 0, cv2.THRESH_TOZERO_INV
        )
        (t, self.channels[channel]) = cv2.threshold(
            tmp, minimum, 255, cv2.THRESH_BINARY
        )

        if channel == "hue":
            self.channels["hue"] = cv2.bitwise_not(self.channels["hue"])

    def track(self, frame, mask):
        center = None
        contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[
            -2
        ]

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            moments = cv2.moments(c)
            if moments["m00"] > 0:
                center = int(moments["m10"] / moments["m00"]), int(
                    moments["m01"] / moments["m00"]
                )
            else:
                center = int(x), int(y)

            if radius > 10:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
                if self.previous_position:
                    cv2.line(
                        self.trail, self.previous_position, center, (255, 255, 255), 2
                    )

        cv2.add(self.trail, frame, frame)
        self.previous_position = center

    def detect(self, frame):
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_img)
        self.channels["hue"] = h
        self.channels["saturation"] = s
        self.channels["value"] = v

        self.threshold_image("hue")
        self.threshold_image("saturation")
        self.threshold_image("value")

        self.channels["laser"] = cv2.bitwise_and(
            self.channels["hue"], self.channels["value"]
        )
        self.channels["laser"] = cv2.bitwise_and(
            self.channels["saturation"], self.channels["laser"]
        )

        hsv_image = cv2.merge(
            [self.channels["hue"], self.channels["saturation"], self.channels["value"]]
        )
        self.track(frame, self.channels["laser"])

        return hsv_image
