import cv2
from ultralytics import YOLO

model = YOLO(r"C:\Users\VikasVarpe\Downloads\last.pt")  
camera_id = 0  
cap = cv2.VideoCapture(camera_id)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow('YOLOv8 Inference - Live Camera', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
