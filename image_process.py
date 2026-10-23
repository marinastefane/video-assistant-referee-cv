import cv2
import os
from player_detection import get_detector
from ball_detection import BallDetector
from field_detection import detect_field_mask
from field_map import create_2d_map

# --------------------------------------
# CONFIGURAÇÕES
# --------------------------------------
IMAGE_PATH = "input/i.jpg"
OUTPUT_PATH = "output/frame_out.jpg"
YOLO_MODEL_PATH = "yolov8s.pt"

os.makedirs("output", exist_ok=True)

# Detectores
detector = get_detector(YOLO_MODEL_PATH, conf=0.35)
ball_detector = BallDetector(YOLO_MODEL_PATH, conf=0.35)

frame = cv2.imread(IMAGE_PATH)

# Reduz tamanho para acelerar
frame = cv2.resize(frame, (960, 540))
annotated = frame.copy()


# detectar campo
field_mask = detect_field_mask(frame)

# detectar jogadores
player_boxes = detector.detect(frame, field_mask=field_mask)

player_positions = []
for (x1, y1, x2, y2) in player_boxes:
    cx = int((x1 + x2) / 2)
    cy = int(y2)  # posição aproximada dos pes do jogador

    player_positions.append((cx, cy))

    # desenhar
    cv2.rectangle(annotated, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

# detectar bola
ball_boxes = ball_detector.detect_ball(frame)
ball_position = None

if ball_boxes:
    (bx1, by1, bx2, by2) = ball_boxes[0]
    cx = int((bx1 + bx2) / 2)
    cy = int((by1 + by2) / 2)
    ball_position = [ball_boxes[0]]

    # desenhar bola
    cv2.circle(annotated, (cx, cy), 5, (0, 140, 255), -1)
    cv2.putText(annotated, "bola", (cx + 10, cy - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 140, 255), 2)


# bola fora

W, H = 600, 400

ball_out = False

if ball_position:

    bx_center = int((ball_position[0][0] + ball_position[0][2]) / 2)
    by_center = int((ball_position[0][1] + ball_position[0][3]) / 2)
    
    map_x = int(bx_center / 960 * W)
    map_y = int(by_center / 540 * H)
    
    # verifica todas as bordas (com margem de 20px usada no desenho do campo)
    if (map_x < 20 or map_x > W - 20 or 
        map_y < 20 or map_y > H - 20):
        ball_out = True

if ball_out:
    cv2.putText(annotated, "BOLA FORA!", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)


cv2.imwrite(OUTPUT_PATH, annotated)

create_2d_map(player_positions, ball_position, homography_matrix = None, output_path = "output/mapa2d.jpg")

print("\n=== RESULTADO ===")
print("Jogadores detectados:")
for i, (px, py) in enumerate(player_positions):
    print(f"  Jogador {i+1}: x = {px}, y = {py}")

if ball_position:
    print(f"Bola detectada. Status: {'FORA' if ball_out else 'DENTRO'}")
else:
    print("Bola NÃO detectada.")
