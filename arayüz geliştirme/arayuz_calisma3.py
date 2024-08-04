import sys

from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    
    
    def __init__(self):
        
          super().__init__()
          
          self.init_ui()
         
    def init_ui(self):
        
        self.yazi_alani = QtWidgets.QLabel("Henüz bir tıklanma yok.")
        self.buton = QtWidgets.QPushButton("TIKLA")
        self.say = 0
        
        
        dikey_kutu = QtWidgets.QVBoxLayout()
        
        dikey_kutu.addWidget(self.buton)
        dikey_kutu.addWidget(self.yazi_alani)
        dikey_kutu.addStretch()
        
        yatay_kutu =  QtWidgets.QHBoxLayout()
        
        yatay_kutu.addStretch()
        yatay_kutu.addLayout(dikey_kutu)
        yatay_kutu.addStretch()
        
        self.setLayout(yatay_kutu)
        
        self.buton.clicked.connect(self.tikla)
        
        self.setGeometry(600,250,700,600)
        
        self.show()
        
    def tikla(self):
        
        self.say += 1
        
        self.yazi_alani.setText("{} defa tıklandı.".format(self.say))
        
        
        
        

uygulama = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(uygulama.exec_())





                                                                                                                                                                                    