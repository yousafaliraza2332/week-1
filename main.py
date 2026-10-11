import cv2

INPUT_PATH = "input.mp4"
OUTPUT_PATH = "output.mp4"

cap = cv2.VideoCapture(INPUT_PATH)
if not cap.isOpened():
    raise SystemExit(f"Could not open {INPUT_PATH}")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) or 30

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (width, height))

frame_no = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_no += 1

    
    x1, y1 = width // 4, height // 4
    x2, y2 = 3 * width // 4, 3 * height // 4
    cv2.rectangle(frame, (x1, y1), (x2, y2), (12, 255, 0), 3)

    
    cv2.circle(frame, (width // 2, height // 2), 40, (0, 86, 255), 3)

   
    cv2.line(frame, (0, 60), (width, 60), (255, 15, 0), 2)

   
    cv2.putText(frame, "OpenCV Demo", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f"Frame: {frame_no}", (20, height - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    out.write(frame)

cap.release()
out.release()
print(f"Done. Processed {frame_no} frames -> {OUTPUT_PATH}")
