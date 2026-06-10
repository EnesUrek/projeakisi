import cv2
from preprocess import preprocess_pipeline

# Kamera aç
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    processed = preprocess_pipeline(frame)

    cv2.imshow("Orijinal", frame)
    cv2.imshow("Islenmis", processed)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()