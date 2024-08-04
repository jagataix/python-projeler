import sys

from PyQt5 import QtWidgets,QtGui

def Pencere():
    
    uygulama = QtWidgets.QApplication(sys.argv)
    
    pencere = QtWidgets.QWidget() 
    
    pencere.setWindowTitle("PENCERE 1")
    
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("Uygulamaya hoşgeldiniz.")
    etiket1.move(280,200)
    
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.move(255,0)
    etiket2.setPixmap(QtGui.QPixmap("koü.png"))
    
    buton1 = QtWidgets.QPushButton(pencere)
    buton1.setText("Buton 1")
    buton1.move(300,250)
    
    buton2 = QtWidgets.QPushButton(pencere)
    buton2.setText("Buton 2")
    buton2.move(300,280)
    
    pencere.setGeometry(600,200,700,600)
    pencere.show()
    
    sys.exit(uygulama.exec_())
  

Pencere()







                                                                                         