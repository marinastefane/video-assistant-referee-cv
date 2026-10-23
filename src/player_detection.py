from ultralytics import YOLO
import cv2
import numpy as np

class PlayerDetectorYOLO:
    def __init__(self, model_path = "yolov8s.pt", conf = 0.4):
        self.model = YOLO(model_path)
        self.conf = conf

    def detect(self, frame, field_mask = None):
        results = self.model(frame, imgsz = 640, conf = self.conf, classes = [0], verbose = False)[0]
        boxes = []
        
        H, W = frame.shape[:2]

        for box in results.boxes:

            x1, y1, x2, y2 = box.xyxy.cpu().numpy()[0].astype(int)

            # Se não tiver máscara do campo → aceita tudo
            if field_mask is None:
                boxes.append([x1, y1, x2, y2])
                continue

            # pega o ponto do pé do jogador
            foot_x = int((x1 + x2) / 2)
            foot_y = int(y2) - 5
            
            # só pra nao dar erro de fora da imagem
            foot_x = max(0, min(foot_x, W - 1))
            foot_y = max(0, min(foot_y, H - 1))

            # se o pé não estiver no gramado → ignora
            if field_mask[foot_y, foot_x] == 0:
                continue

            boxes.append([x1, y1, x2, y2])

        return boxes


def get_detector(path = "yolov8s.pt", conf = 0.4):
    return PlayerDetectorYOLO(path, conf)
