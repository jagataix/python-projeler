import librosa
import librosa.display
import matplotlib.pyplot as plt
plt.ion()  # Matplotlib'i interaktif moda geçir

# Kodunuzun geri kalanı


# Ses dosyasını yükle
ses_dosyasi = r"C:\Users\cagat\OneDrive\Belgeler\Image-Line\FL Studio\Projects\slapmelodictechno3.mp3"
ses, ornek_sayisi = librosa.load(ses_dosyasi)

# Ses dosyasını görselleştir
plt.figure(figsize=(10, 4))
plt.plot(ses, color='blue')  # veya istediğiniz bir renk
plt.title('Ses Dosyasının Dalga Formu')
plt.xlabel('Zaman (örnek)')
plt.ylabel('Amplitüd')
plt.show()

# Kod çalışmayı bitirince görselin kapanmasını sağlamak için
input("Devam etmek için bir tuşa basın...")
