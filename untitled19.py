import numpy as np
import sounddevice as sd
import librosa

def ses_amfisi(ses, guclendirme=1):
    # Ses verisini belirtilen güçte çoğalt
    ses = ses * guclendirme
    # Normalleştirme
    ses = ses / np.max(np.abs(ses))
    return ses

# Ses dosyasını yükle
ses_dosyasi = r"C:\Users\cagat\OneDrive\Belgeler\Image-Line\FL Studio\Projects\slapmelodictechno.mp3"
ses, ornek_sayisi = librosa.load(ses_dosyasi, sr=None)

# Güçlendirme faktörünü belirleyin (örneğin, 2 ile çoğaltma)
guclendirme_faktoru = 2

# Ses amfisini uygulayın
ses_amfi = ses_amfisi(ses, guclendirme_faktoru)

# Ses çalma işlemini başlat
stream = sd.play(ses_amfi, samplerate=ornek_sayisi)

# Ses çalma işlemi devam ederken kullanıcıdan giriş al
input("Ses çalıyor. Durdurmak için Enter'a basın.")

# Ses çalma işlemini durdur
sd.stop()
