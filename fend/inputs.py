import cv2
import numpy as np
from pathlib import Path



def input_img(path: Path):
    cap = cv2.VideoCapture(path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    offset = int(fps * 2)       #2sec gap (will change later if needed)

    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    
    for i in range(len(frames) - offset):
        frame_t = frames[i]
        frame_t2 = frames[i + offset]

        print(f"Pair: {i} and {i + offset}")


    # ret, frame1 = cap.read()
    # cap.set(cv2.CAP_PROP_POS_FRAMES, offset)
    # ret, frame2 = cap.read()

    cap.release()

    return frame_t, frame_t2


