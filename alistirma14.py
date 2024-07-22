"""
Proje 3
Bu projede ise 4 tane sınıfı oluşturun.

Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.

Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.

At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.
"""

class hayvan():
    def solunum(self):
        print("Bu canlı solunum yapabiliyor.")
    def beslenme(self):
        print("Bu canlı beslenebiliyor.")
    def hareket(self):
        print("Bu canlı hareket edebiliyor.")
    def __init__(self,goz,bacak,kuyruk):
        self.goz=goz
        self.bacak=bacak
        self.kuyruk=kuyruk
        
    def ses(self):
        print("Bu canlı ses çıkartabiliyor.")
    
class kopek(hayvan):
    
    def __init__(self,goz,bacak,kuyruk,salya):
        self.salya=salya
        self.goz=goz
        self.bacak=bacak
        self.kuyruk=kuyruk
     
    def ses(self):
        print("Köpek havlar.")
    def zıpla(self):
        print("Köpek zıplayabilir.")
    def ısır(self):
        print("Köpek ısırabilir.")
        
class kus(hayvan):
    
    def __init__(self,goz,bacak,kuyruk,gaga,kanat):
        self.gaga=gaga
        self.goz=goz
        self.bacak=bacak
        self.kuyruk=kuyruk
        self.kanat=kanat
     
    def ses(self):
        print("Kuş cıvıldar.")
    def uc(self):
        print("Kuş uçabilir.")
    
class at(hayvan):
    
    def __init__(self,goz,bacak,kuyruk,puskul):
        self.puskul=puskul
        self.goz=goz
        self.bacak=bacak
        self.kuyruk=kuyruk
     
    def ses(self):
        print("At kişner.")
    def binmek(self):
        print("Ata binilenebilir.")
        
    
kopek=kopek(2,4,1,"Çok")

at=at(2,4,1,1)

kus=kus(2,2,1,1,2)

hayvan=hayvan(2,2,1)
print("HAYVAN")
print("Göz sayısı    :",hayvan.goz)
print("Bacak sayısı  :",hayvan.bacak)
print("Kuyruk sayısı :",hayvan.kuyruk)
hayvan.solunum()
hayvan.hareket()
hayvan.beslenme()
hayvan.ses()
print("\n")

print("KÖPEK")
print("Göz sayısı    :",kopek.goz)
print("Bacak sayısı  :",kopek.bacak)
print("Kuyruk sayısı :",kopek.kuyruk)
print("Salya miktarı :",kopek.salya)
kopek.solunum()
kopek.hareket()
kopek.beslenme()
kopek.ses()
kopek.zıpla()
kopek.ısır()
print("\n")

print("KUŞ")
print("Göz sayısı    :",kus.goz)
print("Bacak sayısı  :",kus.bacak)
print("Kuyruk sayısı :",kus.kuyruk)
print("Gaga sayısı   :",kus.gaga)
print("Kanat sayısı  :",kus.kanat)
kus.solunum()
kus.hareket()
kus.beslenme()
kus.ses()
kus.uc()
print("\n")

print("AT")
print("Göz sayısı    :",at.goz)
print("Bacak sayısı  :",at.bacak)
print("Kuyruk sayısı :",at.kuyruk)
print("Püskül sayısı :",at.puskul)

at.solunum()
at.hareket()
at.beslenme()
at.ses()
at.binmek()
print("\n")
    
    
    
    