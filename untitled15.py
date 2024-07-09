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
            directionX = "SOL"
        elif centerX > screen_centerX + 50:
            directionX = "SAG"
        else:
            directionX = "MERKEZ"

        if centerY < screen_centerY - 50:
            directionY = "YUKARI"
        elif centerY > screen_centerY + 50:
            directionY = "ASAGI"
        else:
            directionY = "MERKEZ"

        # Yüzün ekranın hangi yönde olduğunu ekrana yazdır
        cv2.putText(frame, f"{directionX}, {directionY}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Kameradan görüntüyü göster
    cv2.imshow('Face Detection', frame)

    

    # Mavi renk aralığını belirleme
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([140, 255, 255])

    # Kırmızı renk aralığını belirleme
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([20, 255, 255])

    # Renk uzayını BGR'den HSV'ye dönüştürme
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mavi renk alanlarını bulma
    blue_mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)
    blue_result = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Kırmızı renk alanlarını bulma
    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
    red_result = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Mavi ve kırmızı renklerin koyuluğunu artırma
    blue_result_dark = cv2.addWeighted(blue_result, 1.5, np.zeros_like(frame), 0, 0)
    red_result_dark = cv2.addWeighted(red_result, 1.5, np.zeros_like(frame), 0, 0)

    # Mavi ve kırmızı renklerin gösterilmesi
    cv2.imshow('Blue Colors', blue_result_dark)
    cv2.imshow('Red Colors', red_result_dark)

    # Q ile çıkış yap
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Q ile çıkış yap
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera kapat
cap.release()
cv2.destroyAllWindows()
