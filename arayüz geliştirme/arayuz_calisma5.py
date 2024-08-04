import sys

import sqlite3

from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):
     
    def __init__(self):
        
        super().__init__()
        
        self.init_ui()
        self.baglanti()
        
    def baglanti(self):
        
        baglantim = sqlite3.connect("veritabanı.db")
        self.imlec = baglantim.cursor()
        
        islem = "create table if not exists bilgiler (kullanıcı_adı TEXT,parola TEXT)"
        
        self.imlec.execute(islem)
        
        baglantim.commit()

    def init_ui(self):
        
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)

        self.giris = QtWidgets.QPushButton("GİRİŞ YAP")
        self.yazim = QtWidgets.QLabel("")
        
        dikey_kutu = QtWidgets.QVBoxLayout()
        dikey_kutu.addWidget(self.kullanici_adi)
        dikey_kutu.addWidget(self.parola)
        dikey_kutu.addWidget(self.yazim)
        dikey_kutu.addStretch()
        dikey_kutu.addWidget(self.giris)
        
        yatay_kutu = QtWidgets.QHBoxLayout()
        yatay_kutu.addStretch()
        yatay_kutu.addLayout(dikey_kutu)
        yatay_kutu.addStretch()
        
        self.setLayout(yatay_kutu)
        
        self.setWindowTitle("KULLANICI GİRİŞİ")
        self.giris.clicked.connect(self.degerler)
        self.setGeometry(600,250,700,600)
        
        self.show()
    
    def degerler(self):
        
        ad = self.kullanici_adi.text()
        sifre = self.parola.text()
        
        islem2 = "select * from bilgiler where kullanıcı_adı = ? and parola = ?"
        
        self.imlec.execute(islem2,(ad,sifre))
        
        veri = self.imlec.fetchall()
        
        if len(veri) == 0 :
            self.yazim.setText("Böyle bir kullanıcı yok.\nLütfen tekrar deneyiniz.")
        
        else:
            self.yazim.setText("Giriş başarılı.\nHoşgeldin " + ad)
               
        
uygulama = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(uygulama.exec_())
