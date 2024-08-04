import sys

from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow
                                                                                                                                                                    

class Menu(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        menublogu = self.menuBar()
        
        dosya = menublogu.addMenu("DOSYA")
        duzenle = menublogu.addMenu("DÜZENLE")
        
        ac = QAction("DOSYA AÇ",self)
        ac.setShortcut("Ctrl+O")
        
        kaydet = QAction("DOSYA KAYDET",self)
        kaydet.setShortcut("Ctrl+S")
        
        cikis = QAction("ÇIKIŞ",self)
        cikis.setShortcut("Ctrl+Q")
        
        dosya.addAction(ac)
        dosya.addAction(kaydet)
        dosya.addAction(cikis)
        
        alt_menu = duzenle.addMenu("ARA ve DEĞİŞTİR")
        
        ara = QAction("ARA",self)
        ara.setShortcut("Ctrl+R")
        
        degistir = QAction("DEĞİŞTİR",self)
        degistir.setShortcut("Ctrl+X")
        
        alt_menu.addAction(ara)
        alt_menu.addAction(degistir)
        
        temizle = QAction("TEMİZLE",self)
        
        duzenle.addAction(temizle)
             
        cikis.triggered.connect(self.cikis_yap)
        
        dosya.triggered.connect(self.goster)
    
        self.setWindowTitle("MENÜ UYGULAMASI")
        self.setGeometry(600,250,700,600)
        self.show()
        
    def cikis_yap(self):
        #qApp.quit() bu metod hata verebiliyor
        self.close()
    
    def goster(self,aksiyon):
        
        if(aksiyon.text() == "DOSYA KAYDET"):
            print("Dosya kaydete basıldı")
        
        elif(aksiyon.text() == "DOSYA AÇ"):
            print("Dosya aça basıldı")
            
        else:
            print("Çıkışa basıldı")



uygulama = QApplication(sys.argv)

menu = Menu()

sys.exit(uygulama.exec_())         
                                                                                                                                                                                                       