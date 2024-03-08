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
