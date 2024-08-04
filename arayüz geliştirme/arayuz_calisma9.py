import sys

import os

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout
                                                                                                                                                                    
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow

class Notepad(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.init_ui()

    def init_ui(self):
        
        self.yazim = QTextEdit()
        
        self.temizle = QPushButton("TEMİZLE")
        self.ac = QPushButton("AÇ")  
        self.kaydet = QPushButton("KAYDET")
        
        kutu1 = QHBoxLayout()
        
        kutu1.addWidget(self.temizle)
        kutu1.addWidget(self.ac)
        kutu1.addWidget(self.kaydet)
        
        kutu2 = QVBoxLayout()
        
        kutu2.addWidget(self.yazim)
        kutu2.addLayout(kutu1)
        
        self.setLayout(kutu2)
        
        self.temizle.clicked.connect(self.temizledim)
        self.ac.clicked.connect(self.actim)
        self.kaydet.clicked.connect(self.kaydettim)
        
    def temizledim(self):
        
        self.yazim.clear()
        
    def actim(self):
        
        dosyam = QFileDialog.getOpenFileName(self,"DOSYA AÇ",os.getenv("HOME"))
        
        with open(dosyam[0],"r",encoding = "utf-8") as dosya:
            
            self.yazim.setText(dosya.read())
        
    def kaydettim(self):
        
        dosyam = QFileDialog.getSaveFileName(self,"DOSYA KAYDET",os.getenv("HOME"))
        
        with open(dosyam[0],"w",encoding = "utf-8") as dosya:
            
            dosya.write(self.yazim.toPlainText())
            
class Menu(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        self.pencere = Notepad()
        
        self.setCentralWidget(self.pencere)
        
        self.menuler()
        
        self.setWindowTitle("NOTEPAD UYGULAMASI")
        self.setGeometry(600,250,700,600)
        self.show()
    
    def menuler(self):
        
        menublogu = self.menuBar()
        
        dosya = menublogu.addMenu("DOSYA")
        
        ac = QAction("DOSYA AÇ",self)
        ac.setShortcut("Ctrl+O")
        
        kaydet = QAction("DOSYA KAYDET",self)
        kaydet.setShortcut("Ctrl+S")
        
        temizle = QAction("TEMİZLE",self)
        temizle.setShortcut("Ctrl+X")
        
        cikis = QAction("ÇIKIŞ",self)
        cikis.setShortcut("Ctrl+Q")
        
        dosya.addAction(ac)
        dosya.addAction(kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)
        
        dosya.triggered.connect(self.gonder)
        
    def gonder(self,komut):
        
        if komut.text() == "DOSYA AÇ":
            self.pencere.actim()
    
        elif komut.text() == "DOSYA KAYDET":
            self.pencere.kaydettim()
        
        elif komut.text() == "TEMİZLE":
            self.pencere.temizledim()
        
        elif komut.text() == "ÇIKIŞ":
            self.close()
    
uygulama = QApplication(sys.argv)

menu = Menu()

sys.exit(uygulama.exec_())   
      