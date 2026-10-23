# Football Video Assistant Referee — Computer Vision

A computer vision project for football video analysis using YOLOv8 and OpenCV. The system detects players and the ball in video footage and generates an annotated video with the detection results.

## Features

- **Player detection:** identifies players in football footage using YOLO.
- **Ball detection:** detects the ball using a dedicated detection module.
- **Field detection:** includes modules for football field detection and image processing.
- **Homography:** includes tools for perspective transformation and field mapping.
- **Video processing:** processes input footage and saves an annotated output video.
- **Modular architecture:** separates detection, image processing, field mapping, and utility functions.

## Technologies

- Python
- OpenCV
- Ultralytics YOLOv8
- NumPy and other dependencies listed in `requirements.txt`

## Project Structure

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

The exact files and directories may vary depending on your local setup.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/marinastefane/video-assistant-referee-cv.git
cd video-assistant-referee-cv
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Prepare the input video and model

- Place the video you want to analyze in the `input/` directory.
- Make sure the YOLO model weights are available in the expected location.
- Check the paths configured in `main.py` and `src/config.py` before running the project.

### 5. Run the application

From the repository root, run:

```bash
python main.py
```

The processed video is saved to the output path configured in the project. By default, the main script uses `output/video_out.avi`.

## How It Works

1. Loads the input football video.
2. Initializes the detection modules and model.
3. Processes video frames to detect players and the ball.
4. Draws the detection results on the frames.
5. Saves the annotated video to the output directory.

Additional modules provide field detection, homography, and field mapping functionality.

## Project Scope

This project is an educational computer vision prototype inspired by football video assistant referee systems. It focuses on object detection and video analysis.

It is **not an official VAR system** and does not independently validate refereeing decisions, fouls, or offside calls.

## Future Improvements

- Improve ball detection in challenging scenes.
- Track players and the ball across consecutive frames.
- Improve field calibration and 2D player mapping.
- Explore offside-line visualization and other advanced football analytics.

🌐 **Read this README in:** [Português (Brasil)](README.pt-BR.md)