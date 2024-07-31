"""
Proje 2
Siz de bir tane Şarkı projesi geliştirmeye çalışın.

                     Örnek özellikler;

                     1. Şarkı İsmi 
                     2. Sanatçı
                     3. Albüm
                     4. Prodüksiyon Şirketi
                     5. Şarkı Süresi

                     Örnek Metodlar;

                     1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
                     2. Şarkı Ekle
                     3. Şarkı Sil
"""
import sqlite3

from time import *


class sarki():
    
    def __init__(self,ad,sanatcilar,album,sirket,sure,tarz,dil,dinlenme):
        self.ad = ad
        self.sanatcilar = sanatcilar
        self.album = album
        self.sirket = sirket
        self.sure = sure
        self.tarz = tarz 
        self.dil = dil
        self.dinlenme = dinlenme
        
  
        
    
    def __str__(self):
        
        return """
               Şarkı Adı   : {}
               Sanatçılar  : {}
               Albüm       : {}
               Şirket      : {}
               Süre        : {}
               Tarz        : {}
               Dil         : {}
               Dinlenme    : {}
               """.format(self.ad,self.sanatcilar,self.album,self.sirket,self.sure,self.tarz,self.dil,self.dinlenme)
    
class sarki_listesi():
    
    def __init__(self):
       
        self.baglanti_kur()
    
    def baglanti_kur(self):
        
        self.bagla = sqlite3.connect("Şarkı listesi.db")
        
        self.imlec = self.bagla.cursor()
        
        islem = "Create table if not exists listem (Ad TEXT,Sanatçılar TEXT,Albüm TEXT,Şirket TEXT,Süre FLOAT,Tarz TEXT,Dil TEXT,Dinlenme INT)"
    
        self.imlec.execute(islem)
        
        self.bagla.commit()
    
    def sarkilari_goster(self):
        
        islem = "select * from listem"
        
        self.imlec.execute(islem)
        
        şarkılar = self.imlec.fetchall()
        
        if len(şarkılar) == 0:
            print("Listede hiç şarkı yok.")
        else:
        
            for x in şarkılar:
                şarkı = sarki(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
                print(şarkı)
    
    def şarkı_bul(self,ad):
        
        islem = "select * from listem where Ad = ?"
        
        self.imlec.execute(islem,(ad,))
        
        x = self.imlec.fetchall()
        
        if len(x) == 0:
            print("Aradığınız şarkı listede yok.")
        else :
            şarkı = sarki(x[0][0],x[0][1],x[0][2],x[0][3],x[0][4],x[0][5],x[0][6],x[0][7])
            print(şarkı)
            
    def şarkı_ekle(self,x):
        
        islem = "insert into listem values(?,?,?,?,?,?,?,?)"
        
        self.imlec.execute(islem,(x.ad,x.sanatcilar,x.album,x.sirket,x.sure,x.tarz,x.dil,x.dinlenme))
        
        self.bagla.commit()
              
    def şarkı_sil(self,ad):
         
        sorgu = "delete from listem where ad = ?"
         
        self.imlec.execute(sorgu,(ad,))
         
        self.bagla.commit() 
    
    def album_göster(self,ad):
        
        islem = "select * from listem where Albüm = ?"
        
        self.imlec.execute(islem,(ad,))
        
        x = self.imlec.fetchall()
        
        if len(x) == 0:
            print("Albümde şarkı yok.")
        else :
            for y in x:
              şarkı = sarki(y[0],y[1],y[2],y[3],y[4],y[5],y[6],y[7])
              print(şarkı)
     
    def toplam_şarkı_süresi(self):
        
        islem = "select * from listem "
        
        self.imlec.execute(islem)
        
        x = self.imlec.fetchall()
        
        toplam = 0
        
        for y in x:
            toplam += y[4]
            
        print("Toplamda {} dakikalık bir şarkı süresi var.".format(toplam))
        
    def toplam_şarkı_dinlenme(self):
        
        islem = "select * from listem "
        
        self.imlec.execute(islem)
        
        x = self.imlec.fetchall()
        
        toplam = 0
        
        for y in x:
            toplam += y[7]
            
        print("Toplamda dinlenme saysı :",toplam)
    
    def sanatçıları_bul(self):
        
        islem ="select * from listem"
        
        self.imlec.execute(islem)
        
        k = self.imlec.fetchall()
        
        z = dict()
        adlar = []
        
        for x in k:
            isimler= x[1].split(",")
            adlar += isimler
        
        for x in adlar:
            if(x in z):
                z[x] += 1
            else:
                z[x]= 1
        
        for x,y in z.items():
            print("{} sanatçısının {} adet şarkısı vardır.".format(x,y))

    
print("""
=============================================      
     Şarkı Listesine Hoşgeldiniz:
============================================= 
     1 - Şarkıları Göster
     2 - Şarkı Bul
     3 - Şarkı Ekle
     4 - Şarkı Sil
     5 - Albüm Göster
     6 - Toplam Şarkı Süresini Göster
     7 - Toplam Dinlenme Sayısını Göster
     8 - Sanatçıları ve Şarkı Sayılarını Göster
     
     q - Çıkış Yap
     
     """)
     
listem = sarki_listesi()

while True:
    secim = input("Seçiminizi Yapınız :")
    
    if secim == "1":
        
        listem.sarkilari_goster()
        
    elif secim == "2":
        
        ad = input("Şarkı adını giriniz :")
        print("Şarkı aranıyor...")
        sleep(1)
        listem.şarkı_bul(ad)
        
    elif secim == "3":
        
        x = input("Ad :")
        y = input("Sanatçılar :")
        z = input("Albüm :")
        a = input("Şirket :")
        b = float(input("Süre :"))
        c = input("Tarz :")
        d = input("Dil :")
        e = int(input("Dinlenme :"))
        
        ekle = sarki(x,y,z,a,b,c,d,e)
        
        print("Şarkı ekleniyor...")
        sleep(1)
        print("Şarkı eklendi.")
        listem.şarkı_ekle(ekle)
        
    elif secim == "4":
        
        sil = input("Şarkının adını giriniz :")
        
        listem.şarkı_sil(sil) 
        
    elif secim == "5":
        
        albüm = input("Albümün adını giriniz :")
        print("Albüm aranıyor...")
        sleep(1)
        listem.album_göster(albüm) 
        
    elif secim == "6":
        
        listem.toplam_şarkı_süresi()
    
    elif secim == "7":
        
        listem.toplam_şarkı_dinlenme()
    
    elif secim == "8":
        
        listem.sanatçıları_bul()
        
        
    elif secim == "q":
        
        print("Listeden Çıkılıyor...")
        sleep(2)
        print("Listeden Çıkıldı.")
        break
                                                                                                                                                                                                            