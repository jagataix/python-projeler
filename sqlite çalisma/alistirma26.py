"""
Proje 1
Kodlama egzersizimizde yazdığımız kütüphane projesini elinizden geldiğince geliştirmeye çalışın.
"""

import sqlite3

import time

class kitap():
    
    def __init__(self,ad,yazar,yayınevi,tür,baskı,fiyat,adet):
        self.ad = ad
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tür = tür
        self.baskı = baskı
        self.fiyat = fiyat
        self.adet = adet
        
    def __str__(self):
        return """
               Kitap adı : {}
               Yazar     : {}
               Yayınevi  : {}
               Tür       : {}
               Baskı     : {}
               Fiyat     : {}
               Adet      : {}
               
        """.format(self.ad,self.yazar,self.yayınevi,self.tür,self.baskı,self.fiyat,self.adet)                       
        
class kütüphane():
     
    def __init__(self):
        
        self.baglanti_olustur()
        
    def baglanti_olustur(self):
        
        self.baglanti = sqlite3.connect("Kütüphane2.db")
        
        self.imlec = self.baglanti.cursor()
        
        sorgu = "Create Table If not exists kitaplar (ad TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT,fiyat INT,adet INT)"
        
                                                                                                                                            
        self.imlec.execute(sorgu)
        
        self.baglanti.commit()
        
    def baglanti_kes(self):
        
        self.baglanti.close()
    
    def kitaplari_goster(self):
        
        sorgu = "select * from kitaplar"
        
        self.imlec.execute(sorgu)
        
        kitaplar = self.imlec.fetchall()
        
        if len(kitaplar) == 0 :
            print("Kütüphanede kayıtlı hiç kitap yok.")
        else:
            for x in kitaplar:
                kitabım = kitap(x[0],x[1],x[2],x[3],x[4],x[5],x[6])
                print(kitabım)
                
    def kitap_sorgula(self,ad):
        
        sorgu = "select * from kitaplar where ad = ?"
        
        self.imlec.execute(sorgu,(ad,))
        
        kitaplar = self.imlec.fetchall()
        
        if len(kitaplar) == 0 :
            print("Kütüphanede bu adla kayıtlı bir kitap yok.")
        else:
            kitabım =kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4],kitaplar[0][5],kitaplar[0][6])
            print(kitabım)
    
    def kitap_ekle(self,kitabım):
        
        sorgu = "Insert into kitaplar values(?,?,?,?,?,?,?)"
        
        self.imlec.execute(sorgu,(kitabım.ad,kitabım.yazar,kitabım.yayınevi,kitabım.tür,kitabım.baskı,kitabım.fiyat,kitabım.adet))
        
        self.baglanti.commit()
        
    def kitap_sil(self,ad):
        
        sorgu = "delete from kitaplar where ad = ?"
        
        self.imlec.execute(sorgu,(ad,))
        
        self.baglanti.commit()
        
    def baskı_yukselt(self,ad):
        
        sorgu = "select * from kitaplar where ad = ?"
        
        self.imlec.execute(sorgu,(ad,))
        
        kitaplar = self.imlec.fetchall()
        
        if len(kitaplar) == 0 :
            print("Bu adda bir kitap yok.")
        else:
            baskı = kitaplar [0][4]
            baskı += 1
        
        sorgu2="update kitaplar set baskı = ? where ad = ?"
        
        self.imlec.execute(sorgu2,(baskı,ad))
        
        self.baglanti.commit()
    
    def alfabetik_sirala(self):
        
        sorgu = "select * from kitaplar"
        
        self.imlec.execute(sorgu)
        
        liste = self.imlec.fetchall()
        
        liste.sort()
        
        for x,y,z,t,v in liste:
            print("{}/{}/{}/{}/{}".format(x,y,z,t,v))
            
    def yayınevi_filtrele(self,ad):
        
        sorgu = "select * from kitaplar where yayınevi = ?"
        
        self.imlec.execute(sorgu,(ad,))
        
        liste = self.imlec.fetchall()
        
        if len(liste) == 0:
            print("Bu yayınevine ait kitap bulunmamaktadır.")
        else:
         for x in liste:
            filtreli = kitap(x[0],x[1],x[2],x[3],x[4],x[5],x[6])
            print(filtreli)
    
    def yazar_filtrele(self,ad):
        
        sorgu = "select * from kitaplar where yazar = ?"
        
        self.imlec.execute(sorgu,(ad,))
        
        liste = self.imlec.fetchall()
        
        if len(liste) == 0:
            print("Bu yazara ait kitap bulunmamaktadır.")
        else:
         for x in liste:
            filtreli = kitap(x[0],x[1],x[2],x[3],x[4],x[5],x[6])
            print(filtreli)
            
            
    def fiyat_filtrele(self,düşük,yüksek):
        
        sorgu = "select * from kitaplar"
        
        self.imlec.execute(sorgu)
        
        liste = self.imlec.fetchall()
        
        print("Bu fiyat aralığındaki kitaplar :")
        
        for x in liste:
            if düşük <= x[5] and yüksek >= x[5]:
                filtreli = kitap(x[0],x[1],x[2],x[3],x[4],x[5],x[6])
                print(filtreli)
                
    def adet_arttır(self,ad,sayı):
        
        sorgu = "select * from kitaplar where ad = ?"   
        
        self.imlec.execute(sorgu,(ad,))
                
        kitabım = self.imlec.fetchall()
        
        if len(kitabım) == 0 :
            print("Bu adda bir kitap yok.")
        else:
            adet = kitabım [0][6]
            adet += sayı
        
            sorgu2="update kitaplar set adet = ? where ad = ?"
        
            self.imlec.execute(sorgu2,(adet,ad))
        
            self.baglanti.commit()
            print("Kitap sayısı arttırıldı.")
        
    def adet_azalt(self,ad,sayı):
        
        sorgu = "select * from kitaplar where ad = ?"   
        
        self.imlec.execute(sorgu,(ad,))
                
        kitabım = self.imlec.fetchall()
        
        if len(kitabım) == 0 :
            print("Bu adda bir kitap yok.")
        else: 
            if kitabım[0][6] >= sayı:
               adet = kitabım [0][6]
               adet -= sayı
               
               sorgu2="update kitaplar set adet = ? where ad = ?"
        
               self.imlec.execute(sorgu2,(adet,ad))
        
               self.baglanti.commit()
               print("Kitap sayısı azaltıldı.")
            else:
                print("Kütüphanede bu sayıda kitap yok.")
        