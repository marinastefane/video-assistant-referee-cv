# Football Video Assistant Referee — Visão Computacional

Um projeto de visão computacional para análise de vídeos de futebol utilizando YOLOv8 e OpenCV. O sistema detecta jogadores e a bola nas imagens e gera um vídeo de saída com os resultados das detecções.

## Funcionalidades

- **Detecção de jogadores:** identifica jogadores em vídeos de futebol utilizando YOLO.
- **Detecção da bola:** detecta a bola por meio de um módulo específico.
- **Detecção do campo:** inclui módulos para detecção do campo de futebol e processamento de imagens.
- **Homografia:** inclui ferramentas para transformação de perspectiva e mapeamento do campo.
- **Processamento de vídeo:** processa o vídeo de entrada e salva um vídeo de saída com as detecções.
- **Arquitetura modular:** organiza os módulos de detecção, processamento de imagens, mapeamento do campo e funções auxiliares.

## Tecnologias Utilizadas

- Python
- OpenCV
- Ultralytics YOLOv8
- NumPy e outras dependências listadas em `requirements.txt`

## Estrutura do Projeto

```text
video-assistant-referee-cv/
├── README.md
├── README.pt-BR.md
├── main.py
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── player_detection.py
│   ├── ball_detection.py
│   ├── field_detection.py
│   ├── field_map.py
│   ├── homography_module.py
│   ├── image_process.py
│   ├── click_homography.py
│   └── utils.py
├── input/
├── output/
├── models/
│   └── yolov8s.pt
├── requirements.txt
└── .gitignore
```

Os arquivos e diretórios podem variar conforme a configuração local do projeto.

## Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/marinastefane/video-assistant-referee-cv.git
cd video-assistant-referee-cv
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv .venv
```

No Windows, ative o ambiente com:

```bash
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Prepare o vídeo e o modelo

- Coloque o vídeo que deseja analisar dentro da pasta `input/`.
- Verifique se os pesos do modelo YOLO estão no caminho esperado pelo código.
- Confira os caminhos configurados em `main.py` e `src/config.py` antes de executar o projeto.

### 5. Execute a aplicação

Na raiz do repositório, execute:

```bash
python main.py
```

O vídeo processado será salvo no caminho definido no projeto. Por padrão, o script principal utiliza `output/video_out.avi`.

## Como Funciona

1. Carrega o vídeo de entrada.
2. Inicializa os módulos de detecção e o modelo.
3. Processa os quadros do vídeo para detectar jogadores e a bola.
4. Desenha os resultados das detecções nos quadros.
5. Salva o vídeo anotado no diretório de saída.

Os módulos adicionais oferecem funcionalidades relacionadas à detecção do campo, homografia e mapeamento do campo.

## Escopo do Projeto

Este projeto é um protótipo educacional de visão computacional inspirado em sistemas de árbitro assistente de vídeo no futebol. Seu foco é a detecção de objetos e a análise de vídeos.

Ele **não é um sistema VAR oficial** e não valida de forma independente decisões de arbitragem, faltas ou impedimentos.

## Melhorias Futuras

- Aprimorar a detecção da bola em cenas complexas.
- Rastrear jogadores e a bola ao longo dos quadros.
- Melhorar a calibração do campo e o mapeamento 2D dos jogadores.
- Explorar a visualização da linha de impedimento e outras análises avançadas de futebol.

🌐 **Leia este README em:** [English](README.md)