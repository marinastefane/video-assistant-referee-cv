# Configurações gerais do projeto
import numpy as np

# Dimensões reais do campo (metros)
FIELD_WIDTH_M = 105.0
FIELD_HEIGHT_M = 68.0

# HSV para relva
HSV_LOWER_GREEN = np.array([35, 40, 30], dtype=np.uint8)
HSV_UPPER_GREEN = np.array([90, 255, 255], dtype=np.uint8)

# Morfologia
MORPH_KERNEL_SIZE = (31, 31)

# Hough
HOUGH_RHO = 1
HOUGH_THETA = np.deg2rad(1)
HOUGH_THRESHOLD = 120
HOUGH_MIN_LINE_LENGTH = 80
HOUGH_MAX_LINE_GAP = 12

# YOLO
YOLO_MODEL_PATH = "models/yolov8s.pt"

# Saídas
OUT_VIDEO = "output/video_out.mp4"
OUT_CSV = "output/players_positions.csv"
