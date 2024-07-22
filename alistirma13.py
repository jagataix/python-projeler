"""
Proje 2
Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.

Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın.
"""
from time import*

class bilgisayar():
    
    def __init__(self,ac_kapa=1,depolama=1024,ram=16,ekran="RTX 4060",islemci="i7",marka="Dell",durum="Ofis",fan=10,pil=100,isi=30,sure=0,programlar=["Excel","Chrome"]):
        self.depolama=depolama
        self.ram=ram
        self.ekran=ekran
        self.islemci=islemci
        self.marka=marka
        self.durum=durum
        self.fan=fan
        self.pil=pil
        self.isi=isi
        self.sure=sure
        self.programlar=programlar
        self.ac_kapa=ac_kapa
    def __str__(self):
        
        return """
                  BİLGİSAYARIM
        
        Marka                :   {}
        Depolama             :   {} GB
        RAM                  :   {}
        Ekran Kartı          :   {}
        İşlemci              :   {}
        Durum                :   {}
        Fan Sesi Seviyesi    :   {}
        Pil                  :   %{}
        Kasa Isısı           :   {} derece
        Geçirilen süre       :   {} saat
        Programlar           :   {}
    
            """.format(self.marka,self.depolama,self.ram,self.ekran,self.islemci,self.durum,self.fan,self.pil,self.isi,self.sure,self.programlar)
            
    def __len__(self):
         return self.pil


    def depolama_degistir(self):
        birimler = {"1":128,"2":256,"3":512,"4":1024}
        while True:
         depo=input("""
              Depolama birimleri
              1 - 128 GB
              2 - 256 GB
              3 - 512 GB
              4 - 1024 GB(1 TB)
              
              Eklemek/Çıkarmak istediğiniz birimi seçiniz(İşlemden çıkmak için 'q'ya basınız) :""")
         if(depo=="1" or depo=="2" or depo=="3" or depo=="4"):  
            print("Birim seçiliyor...")
            sleep(1)
            sec=input("Seçtiğiniz birimi eklemek için 'l'ye çıkarmak için 'k'ya basın(İşlemden çıkmak için başka bir tuşa basın) :")
            if sec=="l":
                print("Birim ekleniyor...")
                sleep(1)
                self.depolama += birimler[depo]
                print("Birim eklendi.")
            elif sec=="k":
                if (self.depolama-birimler[depo] > 0):
                    
                    print("Birim çıkartılıyor...")
                    sleep(1)
                    self.depolama -= birimler[depo]
                    print("Birim çıkartıldı.")
                else:
                    print("Depolama alanı 0 veya 0'ın altında olamaz!")
            elif sec=="q":
                break
            else:
                print("Yanlış işlem seçimi,Lütfen tekrar deneyiniz...")
         elif depo=="q":
             break
         else:
             print("Yanlış birim seçimi,Lütfen tekrar deneyiniz...")
    
    
    def ram_degistir(self):
        ram_birimler = {"1":4,"2":8,"3":16,"4":32}
        while True:
         depo=input("""
              RAM birimleri
              1 - 4 GB
              2 - 8 GB
              3 - 16 GB
              4 - 32 GB
              
              Eklemek/Çıkarmak istediğiniz RAM'i seçiniz(İşlemden çıkmak için 'q'ya basınız) :""")
         if(depo=="1" or depo=="2" or depo=="3" or depo=="4"):  
            print("RAM seçiliyor...")
            sleep(1)
            sec=input("Seçtiğiniz RAM'i eklemek için 'l'ye çıkarmak için 'k'ya basın(İşlemden çıkmak için başka bir tuşa basın) :")
            if sec=="l":
                print("RAM ekleniyor...")
                sleep(1)
                self.ram += ram_birimler[depo]
                print("RAM eklendi.")
            elif sec=="k":
                if (self.ram-ram_birimler[depo] > 0):
                    
                    print("RAM çıkartılıyor...")
                    sleep(1)
                    self.ram -= ram_birimler[depo]
                    print("RAM çıkartıldı.")
                else:
                    print("RAM miktarı 0 veya 0'ın altında olamaz!")
            elif sec=="q":
                break
            else:
                print("Yanlış işlem seçimi,Lütfen tekrar deneyiniz...")
         elif depo=="q":
             break
         else:
             print("Yanlış birim seçimi,Lütfen tekrar deneyiniz...")
        
        
    def ekran_karti_degistir(self):
        ad=input("Yeni ekran kartı modelinin adını giriniz :")
        self.ekran=ad

    def islemci_degistir(self):
        ad=input("Yeni islemci modelinin adını giriniz :")
        self.islemci=ad
       
    def islem(self):
      if self.pil > 0:
        while True:
         if bilgisayarim.ac_kapa==0:
             break
         elif bilgisayarim.pil <=0:
             break
         else:
          secenekler=input("""
              Yapılabilecek İşlemler:
              1 - OYUN
              2 - SUNUM
              3 - TARAYICI
              4 - DERS ÇALIŞMA
              
              Yapmak istediğiniz işlemi seçiniz(Çıkmak için 'q'ya basınız) :""")
          if secenekler =="1":
            vakit=int(input("Oyun oynayacağınız süreyi giriniz :"))
            self.durum="Oyun"
            self.pil -= vakit*20
            self.sure += vakit
            self.isi += 20
            self.fan += 10
            if self.isi > 80:
                print("Bilgisayar çok ısındı ve fanlar çok çalışıyor bilgisayar kapatılıyor...")
                sleep(2)
                print("Bilgisayar kapatıldı.")
                self.ac_kapa=0
                
            
          elif secenekler =="2":
            vakit=int(input("Sunum yapacağınız süreyi giriniz :"))
            self.durum="Sunum"
            self.pil -= vakit*10
            self.sure += vakit
            self.isi += 10
            self.fan += 5
            if self.isi > 80:
                print("Bilgisayar çok ısındı ve fanlar çok çalışıyor bilgisayar kapatılıyor...")
                sleep(2)
                print("Bilgisayar kapatıldı.")
                self.ac_kapa=0
                
          elif secenekler =="3":
            vakit=int(input("Tarayıcıda geçireceğiniz süreyi giriniz :"))
            self.durum="Tarayıcı"
            self.pil -= vakit*5
            self.sure += vakit
            self.isi += 8
            self.fan += 4
            if self.isi > 80:
                print("Bilgisayar çok ısındı ve fanlar çok çalışıyor bilgisayar kapatılıyor...")
                sleep(2)
                print("Bilgisayar kapatıldı.")
                self.ac_kapa=0
                
          elif secenekler =="4":
            vakit=int(input("Ders çalışma sürenizi giriniz :"))
            self.durum="Ders Çalışma"
            self.pil -= vakit*12
            self.sure += vakit
            self.isi += 14
            self.fan += 6
            if self.isi > 80:
                print("Bilgisayar çok ısındı ve fanlar çok çalışıyor bilgisayar kapatılıyor...")
                sleep(2)
                print("Bilgisayar kapatıldı.")
                self.ac_kapa=0
                
          elif secenekler=="q":
             break
          else:
             print("Yanlış işlem seçimi,Lütfen tekrar deneyiniz...")
      else: 
          print("Yetersiz pil,bilgisayar kapatılıyor...")
          sleep(2)
          print("Bilgisayar kapatıldı.")
          self.ac_kapa=0
          
            
                
    def program_ekle(self):
        uygulama=input("Ekleyeceğiniz programın adını giriniz :")
        alan=int(input("Programın hacmini giriniz :"))
        if self.depolama - alan < 0:
            print("Yetersiz depolama alanı!")
        else:
            self.programlar.append(uygulama)
            self.depolama -= alan
        
    def program_sil(self):
        sonuc=0
        i=0
        uygulama=input("Sileceğiniz programın adını giriniz :")
        for x in self.programlar:
            if x == uygulama:
                
                sonuc=1
                break
            i+=1
        if sonuc==1:  
          print("Program bulundu.")
          alan=int(input("Programın hacmini giriniz :"))
          self.depolama += alan
          print("Program siliniyor...")
          self.programlar.pop(i)
          sleep(1)
          print("Program silindi.")
        else:
          print("Program bulunamadı!")
        
bilgisayarim=bilgisayar()

print("""
      BİLGİSAYARIMA HOŞGELDİNİZ
      
      1 - Genel Durum
      
      2 - Pil Seviyesi
      
      3 - Depolama Miktarını Değiştirme
      
      4 - RAM Miktarını Değiştirme
      
      5 - Ekran Kartını Değiştirme,
      
      6 - İşlemciyi Değiştirme
      
      7 - İşlem Yapma
      
      8 - Program ekleme
      
      9 - Program silme
      
      (Programdan çıkmak için 'q'ya basınız) 
      """)
while True:
    if bilgisayarim.ac_kapa==0:
        print("Bilgisayar kapatılıyor...")
        sleep(2)
        print("Bilgisayar kapatıldı.")
        break
    elif bilgisayarim.pil < 0:
        print("Bilgisayar kapatılıyor...")
        sleep(2)
        print("Bilgisayar kapatıldı.")
        break
    else:
         secim=input("Ne yapmak istediğinizi seçiniz :")
         
         if secim=="1":
             print(bilgisayarim)
         elif secim=="2":
             print("Kalan Pil : %",len(bilgisayarim))
         elif secim=="3":
             bilgisayarim.depolama_degistir()
         elif secim=="4":
             bilgisayarim.ram_degistir()
         elif secim=="5":
             bilgisayarim.ekran_karti_degistir()
         elif secim=="6":
             bilgisayarim.islemci_degistir()
         elif secim=="7":
             bilgisayarim.islem()
         elif secim=="8":
             bilgisayarim.program_ekle()
         elif secim=="9":
             bilgisayarim.program_sil()
         elif secim=="q":
             print("Bilgisayar kapatılıyor...")
             break
         else:
             print("Yanlış işlem seçimi,lütfen tekrar deneyiniz!")
     
        
                
             
             
          

















    

     
            
          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            