import cv2
import os
from src.config import *
from src.player_detection import get_detector
from src.ball_detection import BallDetector
# from field_map import create_2d_map

INPUT_VIDEO = "input/r.mp4"
OUTPUT_VIDEO = "output/video_out.avi"
YOLO_MODEL_PATH = "models/yolov8s.pt"
os.makedirs("output", exist_ok=True)

# Carrega YOLO (jogadores + bola)
detector = get_detector(YOLO_MODEL_PATH, conf=0.35)
ball_detector = BallDetector(YOLO_MODEL_PATH, conf=0.35)

cap = cv2.VideoCapture(INPUT_VIDEO)

fps = cap.get(cv2.CAP_PROP_FPS) or 30
W = 960
H = 540

out = cv2.VideoWriter(
    OUTPUT_VIDEO,
    cv2.VideoWriter_fourcc(*"XVID"),
    fps,
    (W, H)
)

frame_idx = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Reduz resolução para acelerar tudo
    frame = cv2.resize(frame, (W, H))
    print(f"Gerando vídeo em: output/video_out.avi  ({W}x{H})")
    annotated = frame.copy()

    # detectar jogadores
    boxes = detector.detect(frame)

    for (x1, y1, x2, y2) in boxes:
        cv2.rectangle(
            annotated,
            (int(x1), int(y1)),
            (int(x2), int(y2)),
            (0, 255, 0),
            2
        )
        cv2.putText(annotated, "Jog", (int(x1), int(y1) - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # detectar bola
    ball_boxes = ball_detector.detect_ball(frame)
    ball_xy = None

    if ball_boxes:
        (bx1, by1, bx2, by2) = ball_boxes[0]
        cx = int((bx1 + bx2) / 2)
        cy = int((by1 + by2) / 2)
        ball_xy = (cx, cy)

        cv2.circle(annotated, (cx, cy), 8, (0, 140, 255), -1)
        cv2.putText(annotated, "Bola", (cx - 10, cy - 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 140, 255), 2)

    # bola fora
    if cx > W - 50 and cy > H - 50:
        cv2.putText(annotated, "BOLA FORA!", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)


    # SALVAR O FRAME NO VÍDEO
    out.write(annotated)
    cv2.imshow("VAR System - Monitor", annotated)
    frame_idx += 1
    if frame_idx % 30 == 0:
        print(f"Frame {frame_idx} processado...")

cap.release()
out.release()

print("\nProcessamento concluído.")
