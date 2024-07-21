from random import*
from time import*

class kumanda():
    
    def __init__(self,durum="Kapalı",ses=0,kanallar=["TRT"],kanal="TRT"):
        self.durum=durum
        self.ses=ses
        self.kanallar=kanallar
        self.kanal=kanal
    
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
        
        return "Televizyonun durumu : {}\nSes : {}\nKanal : {}\nKanal Listesi : {}".format(self.durum,self.ses,self.kanal,self.kanallar)
        
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
   else:
       print("Yanlış seçim yaptınız!...")
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                