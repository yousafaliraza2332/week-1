# OpenCV Video Annotation

A Python script that reads a video, draws shapes and text on every frame using OpenCV, and saves the annotated result. Three colour themes are available through a command-line option.

## What it draws
- Rectangle around the centre region
- Circle at the centre
- Line across the top
- Title text ("OpenCV Demo") and a live frame counter

## Setup
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
pip install opencv-python
```

## Usage
Place a video named `input.mp4` in the project folder, then run:
```bash
python main_themed.py                  # default theme -> output_default.mp4
python main_themed.py --theme red      # red theme     -> output_red.mp4
python main_themed.py --theme purple   # purple theme  -> output_purple.mp4
```
Use `--input <file>` to process a different video.

## Files
- `main_themed.py`: the script
- `input.mp4`: source video
- `output_*.mp4`: annotated results, one per theme

## How it works
1. Opens the video with `cv2.VideoCapture` and reads its width, height and FPS.
2. Loops over every frame, drawing the rectangle, circle, line and text with the selected theme's colours.
3. Writes each frame to a new video with `cv2.VideoWriter` (mp4v codec).
