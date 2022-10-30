from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

#Se crea la aplicacion de QT
app = QApplication()

#Se crea un botton con la palabra hola
window = MainWindow()

#Se hace visible el boton.
window.show()

#QT Loop
sys.exit(app.exec_())

