"""
Proje 1
Kodlama Egzersizimizde yazdığımız Kumanda Sınıfına ek olarak metodlar ve özellikler eklemeye çalışın.
"""




from random import*
from time import*

class kumanda():
    
    def __init__(self,durum="Kapalı",ses=0,kanallar=["TRT"],kanal="TRT",parlaklik=10):
        self.durum=durum
        self.ses=ses
        self.kanallar=kanallar
        self.kanal=kanal
        self.parlaklik=parlaklik
    
    def ac(self):
        
        if(self.durum =="Açık"):
            print("Televizyon zaten açık...")
        else:
            print("Televizyon açılıyor...")
            self.durum="Açık"
            
    def kapa(self):
        
        if(self.durum =="Kapalı"):
            print("Televizyon zaten kapalı...")
        else:
            print("Televizyon kapatılıyor...")
            self.durum="Kapalı"
    
    def ses_ayarla(self):
        
        while True:
            komut = input("Sesi azalt : '<'\nSesi arttır : '>'\nÇıkış : çıkış")
            
            if(komut == "<"):
                if(self.ses !=0):
                    
                    self.ses -= 1
                    print("Ses :",self.ses)
                else:
                    print("Ses minimum seyiyede!")
            elif(komut ==">"):
                if(self.ses !=20):
                    self.ses += 1
                    print("Ses :",self.ses)
                else:
                    print("Ses maksimum seyiyede!")
                
            else:
                print("Ses güncellendi :",self.ses)
                break
            
    
    def kanal_ekle(self,kanalim):
        print("Kanal ekleniyor...")
        sleep(1)
        self.kanallar.append(kanalim)
        
        print("Kanal eklendi...")
    
    def rastgele_kanal(self):
        rast=randint(0,len(self.kanallar)-1)
        
        self.kanal=self.kanallar[rast]
        
        print("Şuanki gösterilen kanal :",self.kanal)
        
    def __len__(self):
        
        return len(self.kanallar)
    
    def __str__(self):
        
        return "Televizyonun durumu : {}\nSes : {}\nKanal : {}\nKanal Listesi : {}\nParlaklık : {}".format(self.durum,self.ses,self.kanal,self.kanallar,self.parlaklik)
    
    def yer_degistir(self):
        a=int(input("Değistimek istediginiz birinci kanalın yerini giriniz :"))
        b=int(input("Değistimek istediginiz ikinci kanalın yerini giriniz  :"))
        yedek=self.kanallar[a-1]
        self.kanallar[a-1]=self.kanallar[b-1]
        self.kanallar[b-1]=yedek
        print("Kanalların yeri değiştiriliyor...")
        sleep(1)
        print("Yeni kanal listesi :",self.kanallar)
    
    def kanal_listesi(self):
        print("Kanalların Listesi:")
        i=1
        for x in self.kanallar:
            print(x)
            i+=1
    
    def parlaklik_ayarla(self):
        while True:
            print("Parlaklık :",self.parlaklik)
            
            ayarla=input("Parlaklığı artırmak için 'm' azaltmak için 'n' tuşuna basınız(çıkmak için başka herhangi bir tuşa basın) :")
            if(ayarla=="m"):
                self.parlaklik+=1
            elif(ayarla=="n"):
                self.parlaklik-=1
            else:
                break
    
    def kanal_ara(self):
        sonuc=0
        ara=input("Kanalın adını giriniz :")
        for x in self.kanallar:
            if(ara==x):
                sonuc=1
                break
        
        if(sonuc==1):
            print("Kanal bulundu...")
        else:
            print("Kanal bulunamadı...")
            
        
            
kumandam=kumanda()                
                
print("""
      KUMANDA
     
 1 - TV AÇ
 
 2 - TV KAPAT
 
 3 - SES AYARLARI
 
 4 - KANAL EKLE
 
 5 - KANAL SAYISINI ÖĞRENME
 
 6 - RASTGELE KANALA GEÇME
 
 7 - TELEVİZYON BİLGİLERİ
 
 8 - KANAL YERİ DEĞİŞTİRME
 
 9 - KANALLARIN LİSTESİ
 
 10- PARLAKLIK AYARI
 
 11- KANAL ARA
 
 (Çıkmak için 'q'ya basın)
           """)           
                
                
while True:

   secim=input("Seçiminizi yapınız :")

   if(secim=="q"):
       print("Programdan çıkılıyor...")
       break
   
   elif(secim=="1"):
       kumandam.ac()
   elif(secim=="2"):
       kumandam.kapa()     
   elif(secim=="3"):
       kumandam.ses_ayarla()
   elif(secim=="4"):
       kanallarim=input("Kanal isimlerini ',' ile ayırarak giriniz :")         
                 
       liste = kanallarim.split(",")
       
       for ekle in liste:
           kumandam.kanal_ekle(ekle)   
   elif(secim=="5"): 
       print("Kanal Sayısı :",len(kumandam))
   elif(secim=="6"): 
       kumandam.rastgele_kanal()
   elif(secim=="7"): 
       print(kumandam)
   elif(secim=="8"):
       kumandam.yer_degistir()
   elif(secim=="9"):
        kumandam.kanal_listesi()
   elif(secim=="10"):
        kumandam.parlaklik_ayarla()
   elif(secim=="11"):
        kumandam.kanal_ara()
   else:
       print("Yanlış seçim yaptınız!...")
       
    
                
                
  