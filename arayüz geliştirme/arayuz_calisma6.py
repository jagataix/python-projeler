import sys

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout


class Pencere(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.init_ui()
    
    def init_ui(self):
        
        self.isaretle = QCheckBox("Uygulamayı beğendiniz mi?")
        self.yazim = QLabel("")
        self.buton = QPushButton("TIKLA")
        
        dikey_kutu = QVBoxLayout()
        
        dikey_kutu.addWidget(self.isaretle)
        dikey_kutu.addWidget(self.yazim)
        dikey_kutu.addWidget(self.buton)
        
        self.setLayout(dikey_kutu)
        
        self.setWindowTitle("UYGULAMA")
        
        self.buton.clicked.connect(lambda : self.tikla(self.isaretle.isChecked(),self.yazim))
        
        self.setGeometry(600,250,700,600)
        
        self.show()
        
    def tikla(self,isaret,yazi):
        
        if isaret:
            yazi.setText("Uygulamayı sevdiğiniz için çok mutluyuz!")
        else:
            yazi.setText("Geri bildiriminiz için teşekkürler,kendimizi daha çok geliştirmeye çalışacağız.")

uygulama = QApplication(sys.argv)

pencere = Pencere()

sys.exit(uygulama.exec_())



                                                                                                                                                                                                                