import random
import time
print("""
**************************************

Sayı Tahmin Oyunu


1 ile 40 arasında sayıyı tahmin edin.

**************************************  
      """)
      
rastgele_sayi=random.randint(1,40)
tahmin_hakkı=7

while True:
    
    tahmin=int(input("Tahmininiz :"))
    
    if(tahmin < rastgele_sayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        
        print("Daha büyük bir sayı tahmin ediniz.")
        tahmin_hakkı -= 1
    
    elif(tahmin > rastgele_sayi):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        
        print("Daha küçük bir sayı tahmin ediniz.")
        tahmin_hakkı -= 1
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler sayıyı doğru tahmin ettiniz!..Sayımız:",rastgele_sayi)
        break
    if tahmin_hakkı==0:
        print("7 hakkınızı da kullandınız!")
        break