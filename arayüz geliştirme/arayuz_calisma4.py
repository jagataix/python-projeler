import sys

from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):
    
    def __init__(self):

           super().__init__()
           
           self.init_ui()
    
    def init_ui(self):
        
        self.yazim = QtWidgets.QLineEdit()
        self.temizle = QtWidgets.QPushButton("TEMİZLE")
        self.yazdir = QtWidgets.QPushButton("YAZDIR")


        dikey_kutu = QtWidgets.QVBoxLayout()
        
        dikey_kutu.addWidget(self.yazim)
        dikey_kutu.addWidget(self.temizle)
        dikey_kutu.addWidget(self.yazdir)
        dikey_kutu.addStretch()
        
        self.setLayout(dikey_kutu)
        
        self.temizle.clicked.connect(self.tikla)
        self.yazdir.clicked.connect(self.tikla)
        
        self.setGeometry(600,250,700,600)
        
        self.show()
        
    def tikla(self):
        
        gönder = self.sender()
        
        if gönder.text() == "TEMİZLE":
            
            self.yazim.clear()   
            
        else:
            print(self.yazim.text())
            

uygulama = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(uygulama.exec_())
                                                                                                                                                                                                                                                                                         