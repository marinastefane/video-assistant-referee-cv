import cv2
import numpy as np

# ---------------------------------------------
# CONFIGURAÇÕES
# ---------------------------------------------
IMAGE_PATH = "input/tr.jpg"        # sua imagem
OUTPUT_H_FILE = "output/H.npy"        # onde salvar a homografia
OUTPUT_POINTS_FILE = "output/clicked_points.npy"

# TAMANHO REAL DO CAMPO DE FUTEBOL (FIFA)
FIELD_WIDTH = 105.0   # metros (comprimento)
FIELD_HEIGHT = 68.0   # metros (largura)

clicked_points = []
window_name = "Clique 4 pontos (ordem abaixo)"

# ---------------------------------------------
# CALLBACK DO CLICK
# ---------------------------------------------
def click_event(event, x, y, flags, param):
    global clicked_points

    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))
        print(f"Ponto {len(clicked_points)} clicado: {(x, y)}")

        cv2.circle(img_display, (x, y), 5, (0, 0, 255), -1)
        cv2.putText(img_display, str(len(clicked_points)), (x + 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow(window_name, img_display)

        # fechar quando clicar 4
        if len(clicked_points) == 4:
            cv2.destroyAllWindows()


# ---------------------------------------------
# CARREGAR IMAGEM
# ---------------------------------------------
img = cv2.imread(IMAGE_PATH)

if img is None:
    print("ERRO: Não foi possível carregar a imagem.")
    exit()

img_display = img.copy()


print("\n===================================================")
print(" INSTRUÇÕES PARA CLICAR OS 4 PONTOS ")
print("===================================================")
print("""
Clique os pontos na ORDEM CERTA:

  1️⃣  Canto superior esquerdo do CAMPO VISÍVEL
  2️⃣  Canto superior direito do CAMPO VISÍVEL
  3️⃣  Canto inferior esquerdo do CAMPO VISÍVEL
  4️⃣  Canto inferior direito do CAMPO VISÍVEL

⚠️ IMPORTANTE:
- Não são os cantos reais do campo! 
- São os cantos do CAMPO VISÍVEL na imagem.
- Basta clicar exatamente na linha lateral do gramado.

Depois os 4 pontos forem clicados, a janela fecha automaticamente.
""")
print("===================================================\n")

# ---------------------------------------------
# CAPTURAR PONTOS
# ---------------------------------------------
cv2.imshow(window_name, img_display)
cv2.setMouseCallback(window_name, click_event)
cv2.waitKey(0)

if len(clicked_points) != 4:
    print("Erro: você precisa clicar exatamente 4 pontos.")
    exit()

clicked_points = np.array(clicked_points, dtype=np.float32)
np.save(OUTPUT_POINTS_FILE, clicked_points)

print("\nPontos capturados:")
print(clicked_points)


# ---------------------------------------------
# DEFININDO OS PONTOS DESTINO (CAMPO REAL)
# ---------------------------------------------
dst_points = np.array([
    [0, 0],                    # topo esquerda (0m, 0m)
    [FIELD_WIDTH, 0],          # topo direita (105m, 0m)
    [0, FIELD_HEIGHT],         # baixo esquerda (0m, 68m)
    [FIELD_WIDTH, FIELD_HEIGHT]# baixo direita (105m, 68m)
], dtype=np.float32)

# ---------------------------------------------
# CALCULAR HOMOGRAFIA
# ---------------------------------------------
H, status = cv2.findHomography(clicked_points, dst_points)

if H is None:
    print("ERRO: não foi possível calcular homografia.")
    exit()

np.save(OUTPUT_H_FILE, H)

print("\n===================================================")
print(" HOMOGRAFIA CALCULADA COM SUCESSO! ")
print("===================================================")
print("Arquivo salvo em:", OUTPUT_H_FILE)
print("Agora você pode usar esta matriz H para:")
print(" → mapear jogadores para coordenadas reais (metros)")
print(" → gerar mapa 2D real")
print(" → calcular impedimento")
print(" → distância entre jogadores")
print(" → área de cobertura, etc.")
print("===================================================\n")
