import cv2
import numpy as np
from config import HSV_LOWER_GREEN, HSV_UPPER_GREEN, MORPH_KERNEL_SIZE

KERNEL = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, MORPH_KERNEL_SIZE)

def detect_field_mask(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, HSV_LOWER_GREEN, HSV_UPPER_GREEN)

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, KERNEL)

    return mask

def apply_mask(frame, mask):
    return cv2.bitwise_and(frame, frame, mask=mask)
