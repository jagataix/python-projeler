import cv2
import numpy as np

# Seçilen alanı tutacak değişkenler
start_point = None
end_point = None
cropping = False

# Kamera bağlantısını başlat
cap = cv2.VideoCapture(0)

def select_roi(event, x, y, flags, param):
    global start_point, end_point, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        start_point = (x, y)
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        end_point = (x, y)
        cropping = False

# Fare olaylarını takip et
cv2.namedWindow("Goruntu")
cv2.setMouseCallback("Goruntu", select_roi)

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()

    # Seçilen alanın gösterilmesi
    if start_point and end_point:
        cv2.rectangle(frame, start_point, end_point, (0, 255, 0), 2)

    # Seçilen alanın işlenmesi
    if not cropping:
        if start_point and end_point:
            # Seçilen alanın bölgesini al
            roi = frame[start_point[1]:end_point[1], start_point[0]:end_point[0]]

            # Görüntüyü BGR'den HSV'ye dönüştür
            hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

            # Mavi ve yeşil renk aralıklarını belirle
            lower_blue = np.array([100, 100, 100])
            upper_blue = np.array([140, 255, 255])
            lower_green = np.array([20, 20, 20])
            upper_green = np.array([80, 255, 255])

            # Mavi ve yeşil renkler için maske oluştur
            mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
            mask_green = cv2.inRange(hsv, lower_green, upper_green)

            # Mavi ve yeşil renkleri içeren maskeyi birleştir
            combined_mask = cv2.bitwise_or(mask_blue, mask_green)

            # Maskeleme işlemi uygula
            res = cv2.bitwise_and(roi, roi, mask=combined_mask)

            # Sonuçları ana görüntüde göster
            frame[start_point[1]:end_point[1], start_point[0]:end_point[0]] = res

    cv2.imshow("Goruntu", frame)

    # Çıkış için 'q' tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Kamera bağlantısını kapat
cap.release()
cv2.destroyAllWindows()
