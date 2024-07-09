import cv2
import numpy as np
import matplotlib.pyplot as plt

# Yüz algılama için CascadeClassifier yüklenmesi
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Kamerayı açma
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Gri tonlamalı resmi al
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri algıla
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Yüz varsa
    for (x, y, w, h) in faces:
        # Yüzün etrafına dikdörtgen çiz
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Yüzün merkezini hesapla
        centerX = x + w // 2
        centerY = y + h // 2

        # Ekranın merkez noktasını bul
        screen_centerX = frame.shape[1] // 2
        screen_centerY = frame.shape[0] // 2

        # Yüzün ekranın hangi yönde olduğunu belirle
        if centerX < screen_centerX - 50:
            directionX = "Sol"
        elif centerX > screen_centerX + 50:
            directionX = "Sağ"
        else:
            directionX = "Center"

        if centerY < screen_centerY - 50:
            directionY = "Yukarı"
        elif centerY > screen_centerY + 50:
            directionY = "Aşağı"
        else:
            directionY = "Center"

        # Yüzün ekranın hangi yönde olduğunu ekrana yazdır
        cv2.putText(frame, f"{directionX}, {directionY}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Kameradan görüntüyü göster
    cv2.imshow('Face Detection', frame)

    # Q ile çıkış yap
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera kapat
cap.release()
cv2.destroyAllWindows()

# Ekran üzerindeki tüm renkleri ayırıp gösterme
colors = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
plt.imshow(colors)
plt.axis('off')
plt.show()
