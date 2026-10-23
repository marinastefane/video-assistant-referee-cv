import numpy as np
import cv2

def ensure_shape_points(pts):
    arr = np.array(pts, dtype=np.float32)
    if arr.ndim == 1 and arr.size == 2:
        arr = arr.reshape(1,2)
    return arr

def draw_points(img, pts, color=(0,0,255), radius=5, label=None):
    for i, (x,y) in enumerate(pts):
        cv2.circle(img, (int(x),int(y)), radius, color, -1)
        if label:
            cv2.putText(img, f"{label}{i}", (int(x)+5, int(y)-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

def line_intersection(l1, l2):
    x1,y1,x2,y2 = l1
    x3,y3,x4,y4 = l2
    denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if abs(denom) < 1e-9:
        return None
    px = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4)) / denom
    py = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4 - y3*x4)) / denom
    return (px, py)

def bbox_bottom_center(box):
    x1,y1,x2,y2 = box
    cx = (x1 + x2) / 2.0
    return (cx, y2)

def normalize_homography_point(pt, H):
    x,y = pt
    vec = np.array([x,y,1.0], dtype=float)
    mapped = H.dot(vec)
    if abs(mapped[2]) < 1e-9:
        return None
    return (mapped[0]/mapped[2], mapped[1]/mapped[2])
