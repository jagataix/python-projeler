import sqlite3

import time

class kitap():
    
    def __init__(self,ad,yazar,yayınevi,tür,baskı):
        self.ad = ad
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tür = tür
        self.baskı = baskı
        
    def __str__(self):
        return """
               Kitap adı : {}
               Yazar     : {}
               Yayınevi  : {}
               Tür       : {}
               Baskı     : {}
               
        """.format(self.ad,self.yazar,self.yayınevi,self.tür,self.baskı)                       
        
class kütüphane():
     
    def __init__(self):
        
        self.baglanti_olustur()
        
    def baglanti_olustur(self):
        
        self.baglanti = sqlite3.connect("Kütüphane.db")
        
        self.imlec = self.baglanti.cursor()
        
        sorgu = "Create Table If not exists kitaplar (ad TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT)"
        
        
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
                kitabım = kitap(x[0],x[1],x[2],x[3],x[4])
                print(kitabım)
                
    def kitap_sorgula(self,ad):
        
        sorgu = "select * from kitaplar where ad = ?"
        
        self.imlec.execute(sorgu,(ad,))
        
        kitaplar = self.imlec.fetchall()
        
        if len(kitaplar) == 0 :
            print("Kütüphanede bu adla kayıtlı bir kitap yok.")
        else:
            kitabım =kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitabım)
    
    def kitap_ekle(self,kitabım):
        
        sorgu = "Insert into kitaplar values(?,?,?,?,?)"
        
        self.imlec.execute(sorgu,(kitabım.ad,kitabım.yazar,kitabım.yayınevi,kitabım.tür,kitabım.baskı))
        
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
        
        