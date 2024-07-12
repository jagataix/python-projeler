"""
Programlama Ödevi - Modüller
Proje 1
Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın.

Proje 2
Math modülünde kullandığınız fonksiyonları kendiniz de ayrı bir modüle (Python dosyasına) yazmaya çalışın ve bu yazdığınız modülü kullanarak gelişmiş bir hesap makinesi yazın.
"""

from math import*

from time import*

print("""
********************************
         Hesap Makinesi      
********************************
İşlemler:
   1 -Toplama
   2 -Çıkarma
   3 -Çarpma
   4 -Bölme
   5 -Üs Alma
   6 -Karekök Alma
   7 -Faktoriyel Hesaplama
   8 -Logaritma Hesaplama
   9 -Mutlak Değer
   10-Sinus Hesaplama
   11-Cosinus Hesaplama
   12-Tanjant Hesaplama
   13-Cotanjant Hesaplama
   14-EBOB bulma
   15-EKOK bulma
   16-Büyük Değeri Bulma
   q -Çıkış
********************************      
      """)
      
      
while True:
    secim=input("İşleminizi seçin :")
    
    if secim=="1":
        print("TOPLAMA:")
        x=int(input("Birinci sayıyı giriniz :"))
        y=int(input("İkinci sayıyı giriniz  :"))
        topla=[x,y]
        print("Hesaplanıyor...")
        sleep(1)
        print("SONUC:",sum(topla))
        
    elif secim=="2":
        print("ÇIKARMA:")
        x=int(input("Birinci sayıyı giriniz :"))
        y=int(input("İkinci sayıyı giriniz  :"))
        print("Hesaplanıyor...")
        sleep(1)
        print("SONUC:",x-y)
        
    elif secim=="3":
        print("ÇARPMA:")
        x=int(input("Birinci sayıyı giriniz :"))
        y=int(input("İkinci sayıyı giriniz  :"))
        print("Hesaplanıyor...")
        sleep(1)
        print("SONUC:",x*y)
        
    elif secim=="4":
        print("BÖLME:")
        x=int(input("Birinci sayıyı giriniz :"))
        y=int(input("İkinci sayıyı giriniz  :"))
        if y==0:
            print("İkinci sayı 0 olamaz!")
            continue
        else:
            print("Hesaplanıyor...")
            sleep(1)
            print("SONUC:",x/y)
    elif secim=="5":
        print("ÜS ALMA:")
        x=int(input("Tabandaki sayıyı giriniz :"))
        y=int(input("Üssü sayıyı giriniz      :"))
        print("Hesaplanıyor...")
        sleep(1)
        print("SONUC:",pow(x,y))
            
    elif secim=="6":
        print("KAREKÖK:")
        x=int(input("Bir sayı giriniz :"))
        print("Hesaplanıyor...")
        sleep(1)
        print("SONUC:",sqrt(x))
         
    elif secim=="7":
        print("FAKTORİYEL:")
        x=int(input("Bir sayı giriniz :"))
        print("Hesaplanıyor...")
        sleep(1)
        print("SONUC:",factorial(x))
    
    elif secim=="8":
        print("LOGARİTMA:")
        y=int(input("Logaritma tabanını giriniz :"))
        x=int(input("Logaritma içini giriniz    :"))
        print("Hesaplanıyor...")
        sleep(1)
        print("SONUC:",log(x,y))
        
    elif secim=="9":
        print("MUTLAK DEĞER:")
        x=int(input("Bir sayı giriniz :"))
        print("Hesaplanıyor...")
        sleep(1)
        print("SONUC:",abs(x))
        
    elif secim=="10":
        print("SİNÜS:")
        x=int(input("Bir açı değeri giriniz :"))
        print("Hesaplanıyor...")
        sleep(1)
        print("SONUC:",sin(radians(x)))
        
    elif secim=="11":
        print("COSİNÜS:")
        x=int(input("Bir açı değeri giriniz :"))
        print("Hesaplanıyor...")
        sleep(1)
        print("SONUC:",cos(radians(x)))
        
    elif secim=="12":
        print("TANJANT:")
        x=int(input("Bir açı değeri giriniz :"))
        print("Hesaplanıyor...")
        sleep(1)
        print("SONUC:",tan(radians(x)))
        
    elif secim=="13":
        print("COTANJANT:")
        x=int(input("Bir açı değeri giriniz :"))
        
        print("SONUC:",1/tan(radians(x)))
    
    elif secim=="14":
        print("EBOB:")
        x=int(input("Birinci sayıyı giriniz :"))
        y=int(input("İkinci sayıyı giriniz  :"))
        print("Hesaplanıyor...")
        sleep(1)
        print("SONUC:",gcd(x,y))
        
    elif secim=="15":
        print("EKOK:")
        x=int(input("Birinci sayıyı giriniz :"))
        y=int(input("İkinci sayıyı giriniz  :"))
        print("Hesaplanıyor...")
        sleep(1)
        print("SONUC:",x*y/(gcd(x,y)))
    
    elif secim=="16":
        print("BÜYÜK SAYI:")
        x=int(input("Birinci sayıyı giriniz :"))
        y=int(input("İkinci sayıyı giriniz  :"))
        print("Hesaplanıyor...")
        sleep(1)
        print("SONUC:",max(x,y))
    elif secim=="q":
        sleep(1)
        print("Programdan Çıkıs Yapılıyor...")
        break
    else:
        print("Yanlış işlem seçimi! Tekrar seçim yapınız.")
        sleep(1)
      
      
