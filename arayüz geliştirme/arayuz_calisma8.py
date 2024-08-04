import sys

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout


class Pencere(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.init_ui()

    def init_ui(self):

        self.yazim = QTextEdit()
        
        self.temizle = QPushButton("TEMİZLE")
        
        kutu = QVBoxLayout()
        
        kutu.addWidget(self.yazim)
        kutu.addStretch()
        kutu.addWidget(self.temizle)
       
        
        self.setWindowTitle("Yazı Uygulaması")
        
        self.setLayout(kutu)
        
        self.temizle.clicked.connect(self.tikla)
        
        
        
        self.setGeometry(600,250,700,600)
        
        self.show()
     
    def tikla(self):
            
        self.yazim.clear()
            
             
uygulama = QApplication(sys.argv)

pencere = Pencere()

sys.exit(uygulama.exec_())                                                                                                                                                                                                                                   