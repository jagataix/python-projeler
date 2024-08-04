import sys

from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout


class Pencere(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.init_ui()

    def init_ui(self):
        
        self.secim = QLabel("Hangi dersi daha çok seviyorsun ?")
        
        self.mat = QRadioButton("Matematik")
        self.fizik = QRadioButton("Fizik")
        self.kimya = QRadioButton("Kimya")
        
        self.yazim = QLabel("")
        
        self.buton = QPushButton("Gönder")
        
        kutu = QVBoxLayout()
        
        kutu.addWidget(self.secim)
        kutu.addWidget(self.mat)
        kutu.addWidget(self.fizik)
        kutu.addWidget(self.kimya)
        kutu.addStretch()
        kutu.addWidget(self.yazim)
        kutu.addStretch()
        kutu.addStretch()
        kutu.addStretch()
        kutu.addStretch()
        kutu.addStretch()
        kutu.addStretch()
        kutu.addWidget(self.buton)
        
        
        self.setLayout(kutu)
        
        self.buton.clicked.connect(lambda : self.tikla(self.mat.isChecked(),self.fizik.isChecked(),self.kimya.isChecked(),self.yazim))
        
        self.setWindowTitle("Ders Beğeni Anketi")
        
        self.setGeometry(600,250,700,600)
        
        self.show()
    
    def tikla(self,mat,fizik,kimya,yazi):
        
        if mat:
            yazi.setText("Matematik dersini seçtiniz.")
        elif fizik:
            yazi.setText("Fizik dersini seçtiniz.")
        elif kimya:
            yazi.setText("Kimya dersini seçtiniz.")
        else:
            yazi.setText("Seçim yapılmadı.")
            
            
            
            
            
uygulama = QApplication(sys.argv)

pencere = Pencere()

sys.exit(uygulama.exec_())


                                                                                                                                                                                    