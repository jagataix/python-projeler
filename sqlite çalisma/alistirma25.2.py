from alistirma25 import *


print(
      """
-------------------------------
      Kütüphane Programı
-------------------------------
İşlemler:
    
   1 - Kitapları Göster
   
   2 - Kitap Sorgulama
   
   3 - Kitap Ekle
   
   4 - Kitap Sil
   
   5 - Baskı Yükselt
   
   q - Çıkış
-------------------------------
      """
      )

kütüphanem = kütüphane()

while True:
    islem =input("İşleminizi seçiniz :")
    
    if(islem == "q"):
        print("Program sonlandırılıyor....")
        time.sleep(2)
        print("Program sonlandı.")
        break
   
    elif islem == "1":
        kütüphanem.kitaplari_goster()
    
    elif islem == "2":
        isim = input("Kitap ismini giriniz :")
        print("Kitap sorgulanıyor...")
        time.sleep(1)
        kütüphanem.kitap_sorgula(isim)
    
    elif islem == "3":
        isim = input("Kitap adı :")
        yazar = input("Yazar :")
        yayınevi = input("Yayınevi :")
        tur = input("Kitabın türü :")
        baskı = int(input("Baskı :"))
        
        yeni = kitap(isim,yazar,yayınevi,tur,baskı)
        
        print("Kitap ekleniyor...")
        time.sleep(1)
        print("Kitap eklendi.")
        kütüphanem.kitap_ekle(yeni)
   
    elif islem == "4":
        isim = input("Silinececk kitabın adını giriniz :")
        
        cevap = input("Kitap silinecektir,Emin misiniz?(E/H) :")
        if cevap == "E":
            print("Kitap siliniyor...")
            time.sleep(1)
            kütüphanem.kitap_sil(isim)
            print("Kitap silindi.")
   
    elif islem == "5":
        isim = input("Baskısını yükseltmek istediğiniz kitabın adını giriniz :")
        print("Baskı yükseltiliyor...")
        time.sleep(1)
        kütüphanem.baskı_yukselt(isim)
        print("Baskı yükseltildi.")
    else:
        print("Geçeersiz işlem!")

