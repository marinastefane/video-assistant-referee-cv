import cv2
import numpy as np

def create_2d_map(player_positions, ball_position, homography_matrix=None, output_path="output/map2d.jpg"):
    # Tamanho do mapa 2D
    W, H = 600, 400
    field = np.ones((H, W, 3), dtype=np.uint8) * 30  # cinza escuro

    # Desenhar bordas do campo
    cv2.rectangle(field, (20, 20), (W-20, H-20), (0, 255, 0), 3)

    # Converter coordenadas da imagem (960x540) → mapa (600x400)
    def transform_point(px, py):
        # tentando melhorar a perspectiva 
        if homography_matrix is not None:
 
            pt_array = np.array([[[px, py]]], dtype=np.float32)
            dst_pt = cv2.perspectiveTransform(pt_array, homography_matrix)
            return int(dst_pt[0][0][0]), int(dst_pt[0][0][1])
        
        # se nao funcionar faz o basico
        else:
            sx = int(px / 960 * W)
            sy = int(py / 540 * H)
            return sx, sy
        
    # Jogadores em azul
    for (px, py) in player_positions:
        x, y = transform_point(px, py)
        cv2.circle(field, (x, y), 8, (255, 0, 0), -1)

    # Bola em laranja
    if ball_position:
        box = ball_position[0]
        
        # Calcula o centro da bola
        bx = int((box[0] + box[2]) / 2)
        by = int((box[1] + box[3]) / 2)
        
        # Transforma para o mapa 2D
        x, y = transform_point(bx, by)
        cv2.circle(field, (x, y), 10, (0, 140, 255), -1)

        ball_out = (x < 20 or x > W - 20 or y < 20 or y > H - 20)

        if ball_out:
            cv2.putText(field, "BOLA FORA!", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

        cv2.putText(field, "Bola", (x + 10, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 140, 255), 1)

    # Salvar mapa
    cv2.imwrite(output_path, field)
    print(f"Mapa 2D salvo em {output_path}")

    return field
