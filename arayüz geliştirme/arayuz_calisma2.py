import sys

from PyQt5 import QtWidgets,QtGui

def Pencere():
    
    uygulama = QtWidgets.QApplication(sys.argv)
    
    pencere = QtWidgets.QWidget() 
    
    pencere.setWindowTitle("PENCERE 2")

#horizontal box lar icin kullanılır
    """
    giris = QtWidgets.QPushButton("GİRİŞ")
    cikis = QtWidgets.QPushButton("ÇIKIŞ")

    yatay_kutu = QtWidgets.QHBoxLayout()

    yatay_kutu.addWidget(giris)
    yatay_kutu.addStretch()
    yatay_kutu.addWidget(cikis)

    pencere.setLayout(yatay_kutu)
    """
    
#vertical box lar icin kullanılır 
    """   
    onay = QtWidgets.QPushButton("ONAYLA")
    iptal = QtWidgets.QPushButton("İPTAL ET")
    
    dikey_kutu = QtWidgets.QVBoxLayout()
    
    dikey_kutu.addWidget(onay)
    dikey_kutu.addStretch()
    dikey_kutu.addWidget(iptal)
    
    pencere.setLayout(dikey_kutu)
    """
    
    buton1 = QtWidgets.QPushButton("BUTON 1")
    buton2 = QtWidgets.QPushButton("BUTON 2")
    
    kutu1 = QtWidgets.QHBoxLayout()

    kutu1.addStretch()
    kutu1.addWidget(buton1)
    kutu1.addWidget(buton2)
    
    kutu2 = QtWidgets.QVBoxLayout()
    
    kutu2.addStretch()
    
    kutu2.addLayout(kutu1)
    
    pencere.setLayout(kutu2)
    
    pencere.setGeometry(600,200,700,600)
    pencere.show()
    
    sys.exit(uygulama.exec_())

Pencere()