import cv2
import numpy as np
from ultralytics import YOLO

class BallDetector:
    def __init__(self, model_path="yolov8s.pt", conf=0.25):
        self.model = YOLO(model_path)
        self.conf = conf

    def detect_ball(self, frame):
        
        # primeiro tentar yolo 
        results = self.model(frame, imgsz=640, conf=self.conf, verbose=False)[0]
        for box in results.boxes:
            cls = int(box.cls.cpu().numpy()[0])
            if cls == 32:  # sports ball
                x1, y1, x2, y2 = box.xyxy.cpu().numpy()[0]
                return [(x1, y1, x2, y2)]

        # tentar detecção por cor (bola branca)
        blurred_frame = cv2.GaussianBlur(frame, (7, 7), 0) # filtro gaussiano
        
        hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

        # intervalo de branco
        lower = np.array([0, 0, 160], np.uint8)
        upper = np.array([180, 80, 255], np.uint8)
        mask = cv2.inRange(hsv, lower, upper)


        # tentar pelos contronos
        cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        candidates = []
        for c in cnts:
            area = cv2.contourArea(c)
            if 20 < area < 500:  # área ideal pra bola pequena
                x, y, w0, h0 = cv2.boundingRect(c)
                candidates.append((x, y, x + w0, y + h0))

        if candidates:
            candidates.sort(key=lambda x: x[-1], reverse=True)
            
            # Retorna apenas as coordenadas (x, y, x2, y2) do melhor candidato
            best_candidate = candidates[0]
            return [(best_candidate[0], best_candidate[1], best_candidate[2], best_candidate[3])]

        # procura circulos matematicamente caso não encontre a bola 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)

        circles = cv2.HoughCircles(
            gray,
            cv2.HOUGH_GRADIENT,
            dp=1.2,
            minDist=20,
            param1=100,
            param2=15,
            minRadius=3,
            maxRadius=12
        )

        if circles is not None:
            c = circles[0][0]
            cx, cy, r = int(c[0]), int(c[1]), int(c[2])
            return [(cx - r, cy - r, cx + r, cy + r)]

        return []
