
from ultralytics import YOLO
import os

model = YOLO('yolov8s.pt')

ROOT_DIR = r"C:\Users\VikasVarpe\Downloads\EgoHands Public.v1-specific.yolov81"
model.train(data=os.path.join(ROOT_DIR, "hand_detection.yaml"),optimizer='SGD',save_period=10,degrees=25,imgsz = 480,patience=10,lr0= 0.001, lrf=0.001, batch=32, epochs=50)


