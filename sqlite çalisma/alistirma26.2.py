from alistirma26 import *


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
   
   6 - Alfabetik Sira ile göster
   
   7 - Yayınevine Göre Filtrele
   
   8 - Yazara Göre Filtrele
   
   9 - Fiyat Göre Filtrele
   
   10- Adet Arttır
   
   11- Adet Azalt
   
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
        fiyat = int(input("Fiyat :"))
        adet = int(input("Adet :"))
        
        yeni = kitap(isim,yazar,yayınevi,tur,baskı,fiyat,adet)
        
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
    
    elif islem == "6":
        print("Kitaplar sıralanıyor...")
        time.sleep(1)
        kütüphanem.alfabetik_sirala()
    
    elif islem == "7":
            ad = input("Yayınevini giriniz :")
            print("Yayınevine ait kitaplar aranıyor...")
            time.sleep(1)
            kütüphanem.yayınevi_filtrele(ad)
    
    elif islem == "8":
            ad = input("Yazarın adını giriniz :")
            print("Yazara ait kitaplar aranıyor...")
            time.sleep(1)
            kütüphanem.yazar_filtrele(ad)
   
    elif islem == "9":
            a = int(input("En Düşük  :"))
            b = int(input("En Yüksek :"))
            
            print("Aralığa göre kitaplar aranıyor...")
            time.sleep(1)
            kütüphanem.fiyat_filtrele(a,b)
    
    elif islem == "10":
            x = input("Adet arttırmak istediğiniz kitabın adını giriniz :")
            y = int(input("Kaç adet arttıracağınız giriniz :"))
            
            print("Kitap aranıyor...")
            time.sleep(1)
            kütüphanem.adet_arttır(x,y)
    
    elif islem == "11":
            x = input("Adet azaltmak istediğiniz kitabın adını giriniz :")
            y = int(input("Kaç adet azaltacağınızı giriniz :"))
            
            print("Kitap aranıyor...")
            time.sleep(1)
            kütüphanem.adet_azalt(x,y)
        
    
    else:
        print("Geçeersiz işlem!")
