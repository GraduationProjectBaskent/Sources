import cv2
import pandas as pd
from ultralytics import YOLO

# YOLO modelini yükle
model = YOLO('deneme.pt')

# Video dosyasını yükle
cap = cv2.VideoCapture('Red_ballon.mp4')

# COCO sınıflarını yükle
with open("coco.txt", "r") as my_file:
    class_list = my_file.read().split("\n")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    
    frame = cv2.resize(frame, (1020, 500))
    frame = cv2.flip(frame, 1)
    
    # Model tahmini
    results = model.predict(frame)
    detections = results[0].boxes.data.cpu().numpy()  
    
    
    for detection in detections:
        x1, y1, x2, y2, conf, class_id = detection
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        class_name = class_list[int(class_id)]
        
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{class_name} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    
    cv2.imshow("Detections", frame)
    
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
