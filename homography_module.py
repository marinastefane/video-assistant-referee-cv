import numpy as np
import cv2
from config import FIELD_WIDTH_M, FIELD_HEIGHT_M
from utils import ensure_shape_points

def build_default_field_plane():
    return np.float32([
        [0.0, 0.0],
        [FIELD_WIDTH_M, 0.0],
        [FIELD_WIDTH_M, FIELD_HEIGHT_M],
        [0.0, FIELD_HEIGHT_M]
    ])

def estimate_homography(image_pts, field_pts):
    img = ensure_shape_points(image_pts)
    fld = ensure_shape_points(field_pts)
    H, mask = cv2.findHomography(img, fld, cv2.RANSAC, 5.0)
    return H, mask
