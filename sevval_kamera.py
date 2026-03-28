import cv2
from ultralytics import YOLO

# Modeli yükle (İnternetten otomatik indirecek)
model = YOLO('yolov8n.pt') 

# Kamerayı aç
cap = cv2.VideoCapture(0)

print("Kamera aciliyor... Cikmak istersen klavyeden 'q'ya bas.")

while cap.isOpened():
    success, frame = cap.read()
    if success:
        # Nesneleri tanı
        results = model(frame)
        # Ekrana çiz
        annotated_frame = results[0].plot()
        # Pencerede göster
        cv2.imshow("Dijital Simyacilar Test", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
