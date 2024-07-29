import sqlite3

baglanti = sqlite3.connect("kütüphane.db")

imlec = baglanti.cursor()

def tablo_olustur():
    imlec.execute("CREATE TABLE IF NOT EXISTS kitaplik (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    baglanti.commit()
    
def veri_ekle():
    imlec.execute("Insert into kitaplik Values('Alamut','Vladimir Bartol','Koridor',542)")
    baglanti.commit()
    
def veri_ekle2(ad,yazar,yayınevi,sayfa):
    imlec.execute("Insert into kitaplik Values(?,?,?,?)",(ad,yazar,yayınevi,sayfa))
    baglanti.commit()
    
def veri_al():
    imlec.execute("Select * from kitaplik")
    listem = imlec.fetchall()
    print("tablo")
    for x in listem:
        print(x)
        
def veri_al2():
    imlec.execute("Select İsim,Yazar from kitaplik")
    listem = imlec.fetchall()
    print("kitap ve yazar tablosu")
    for x in listem:
        print(x)
        
def veri_al3(a):
    imlec.execute("Select * from kitaplik where Yayınevi = ?",(a,))
    listem = imlec.fetchall()
    print("{} yayınevinin kitaplari".format(a))
    for x in listem:
        print(x)

def guncelle(eski,yeni):
    imlec.execute("update kitaplik set Yayınevi = ? where Yayınevi = ?",(yeni,eski))
    baglanti.commit()

def sil(hedef):
    imlec.execute("delete from kitaplik where Yazar = ?",(hedef,))
    baglanti.commit()

ad = input("Kitap İsmi :")
yazar = input("Yazarı :")
yayınevi = input("Yayınevi :")
sayfa = int(input("Sayfa Sayısı :"))
    
tablo_olustur()
veri_ekle()
veri_ekle2(ad,yazar,yayınevi,sayfa)
veri_al()
veri_al2()
veri_al3("KOU")
guncelle("KOU","Umuttepe")
veri_al()
sil("cato")
veri_al()
baglanti.close()
