"""
Proje 3
Süpermarket içindeki ürünler üzerinden bir tane Süpermarket Projesi geliştirmeye çalışın.
"""

import sqlite3 

class ürün():
    
    def __init__(self,ad,marka,tür,ağırlık,ambalaj,fiyat,adet):
        
        self.ad = ad
        self.marka = marka
        self.tür = tür
        self.ağırlık = ağırlık
        self.ambalaj = ambalaj
        self.fiyat = fiyat
        self.adet = adet
        
    def __str__(self):
        
        return """
               Ad       : {}
               Marka    : {}
               Tür      : {}
               Ağırlık  : {}
               Ambalaj  : {}
               Fiyat    : {}
               Adet     : {}
               
               """.format(self.ad,self.marka,self.tür,self.ağırlık,self.ambalaj,self.fiyat,self.adet)
class market():
    
    def __init__(self):
        
        self.bagla = sqlite3.connect("Süpermarket.db")
        
        self.imlec = self.bagla.cursor()
        
        islem = "Create table if not exists Ürünler (Ad TEXT,Marka TEXT,Tür TEXT,Ağırlık FLOAT,Ambalaj TEXT,Fiyat FLOAT,Adet INT)"
    
        self.imlec.execute(islem)
        
        self.bagla.commit()

    def ürünleri_göster(self):
        
        islem = "select * from Ürünler"
        
        self.imlec.execute(islem)
        
        ürünler = self.imlec.fetchall()
        
        if len(ürünler) == 0:
           
            print("Markette ürün yok.")
            
        else:
        
            for x in ürünler:
                ürünüm = ürün(x[0],x[1],x[2],x[3],x[4],x[5],x[6])
                print(ürünüm)
                
    def ürün_bul(self,ad):
        
        islem = "select * from Ürünler where Ad = ?"
        
        self.imlec.execute(islem,(ad,))
        
        x = self.imlec.fetchall()
        
        if len(x) == 0:
            print("Markette bu adda bir ürün yok.")
        else :
            ürünüm = ürün(x[0][0],x[0][1],x[0][2],x[0][3],x[0][4],x[0][5],x[0][6])
            print(ürünüm)

    def ürün_ekle(self,x):
        
        islem = "insert into Ürünler values(?,?,?,?,?,?,?)"
        
        self.imlec.execute(islem,(x.ad,x.marka,x.tür,x.ağırlık,x.ambalaj,x.fiyat,x.adet))
        
        self.bagla.commit()
              
    def ürün_sil(self,ad):
         
        sorgu = "delete from Ürünler where Ad = ?"
         
        self.imlec.execute(sorgu,(ad,))
         
        self.bagla.commit() 
    
    def fiyat_degistir(self,ad,güncel):
        
        sorgu = "select * from Ürünler where Ad = ?"
        
        self.imlec.execute(sorgu,(ad,))
        
        ürünler = self.imlec.fetchall()
        
        if len(ürünler) == 0 :
            print("Bu adda bir ürün yok.")
        else:
            
            sorgu2="update Ürünler set Fiyat = ? where Ad = ?"
        
            self.imlec.execute(sorgu2,(güncel,ad))
        
            self.bagla.commit()
            
    def alışveriş(self):
        
        toplam = 0
        
        while True:
            ürünüm = input("Ürünün adını giriniz (Alışverişi bitirmek için q'ya basın) :") 
            
            
            if ürünüm == "q" :
                print("Alışveriş toplam tutar :",toplam)
                break
            else:
                
                islem = "select * from Ürünler where Ad = ?"
                
                self.imlec.execute(islem,(ürünüm,))
                
                x = self.imlec.fetchall()
                
                if len(x) == 0:
                    print("Markette bu adda bir ürün yok.")
                else :
                    adet = int(input("Üründen kaç adet alacağınızı giriniz :"))
                    
                    if adet > x[0][6]:
                        print("Üründen bu adet kadar yok.")
                    else:
                        toplam += x[0][5] * adet
                        
                        if x[0][6] - adet == 0:
                            sorgu = "delete from Ürünler where Ad = ?"
                         
                            self.imlec.execute(sorgu,(ürünüm,))
                         
                            self.bagla.commit() 
                            
                        else:
                            sorgu2="update Ürünler set Adet = ? where Ad = ?"
                        
                            self.imlec.execute(sorgu2,((x[0][6]-adet),ürünüm))
                        
                            self.bagla.commit()
                            
                        
                        print("Ürün sepete eklendi.Şuanlık toplam tutar :",toplam)
                        
print("""
=============================================      
     Süpermarkete Hoşgeldiniz:
============================================= 
     1 - Ürünleri Göster
     2 - Ürün Bul
     3 - Ürün Ekle
     4 - Ürün Sil
     5 - Fiyat Değiştir
     6 - Alışveriş Yap
     
     q - Çıkış Yap
     
     """)

ürünler = market()
     
while True:
    secim= input("İşleminiz seçiniz :")
    
    if secim == "1":
        
        ürünler.ürünleri_göster()
    elif secim == "2":
        ad = input("Ürün adını giriniz :")
        
        ürünler.ürün_bul(ad)
        
    elif secim == "3":
        
        x = input("Ad :")
        y = input("Marka :")
        z = input("Tür :")
        a = float(input("Ağırlık :"))
        b = input("Ambalaj :")
        c = float(input("Fiyat :"))
        d = int(input("Adet :"))
        
        ekle = ürün(x,y,z,a,b,c,d)
        
        ürünler.ürün_ekle(ekle)
        
    elif secim == "4":
        
        kaldır = input("Ürünün adını giriniz :")
        
        ürünler.ürün_sil(kaldır) 
        
    elif secim == "5":
        ad = input("Ürünün adını giriniz :")
        yeni = float(input("Güncellenecek yeni fiyatı giriniz :"))
        
        ürünler.fiyat_degistir(ad,yeni)
    elif secim == "6":
        ürünler.alışveriş()
    elif secim == "q":
        print("Yine bekleriz iyi günler.")
        break 
    else: 
        print("Yanlış İşlem seçimi!")
                
                
            






