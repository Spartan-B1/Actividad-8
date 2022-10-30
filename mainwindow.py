from operator import truediv
from re import L
from wsgiref import headers
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide2.QtCore import Slot
from ui_interfaz import Ui_MainWindow
from libreria import Lista
from particula import Particula

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.lista = Lista()
        self.id = int(0)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.Agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.Mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_elemento)

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID","Orig X", "Orig Y", "Dest X", "Dest Y", "Velocidad" ,"Red",  "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.lista))

        row = 0
        for particula in self.lista:
            id_widget = QTableWidgetItem(particula.id)
            origenX_widget = QTableWidgetItem(particula.origenX)
            origenY_widget = QTableWidgetItem(particula.origenY)
            destinoX_widget = QTableWidgetItem(particula.destinoX)
            destinoY_widget = QTableWidgetItem(particula.destinoY)
            velocidad_widget = QTableWidgetItem(particula.velocidad)
            red_widget = QTableWidgetItem(particula.red)
            green_widget = QTableWidgetItem(particula.green)
            blue_widget = QTableWidgetItem(particula.blue)
            distancia_widget = QTableWidgetItem(particula.distancia)

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origenX_widget)
            self.ui.tabla.setItem(row, 2, origenY_widget)
            self.ui.tabla.setItem(row, 3, destinoX_widget)
            self.ui.tabla.setItem(row, 4, destinoY_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)
            row += 1


    @Slot()
    def buscar_elemento(self):
        identificador = self.ui.buscar_lineEdit.text()

        find = False
        for particula in self.lista:
            if identificador == particula.id:
                self.ui.tabla.clear()
                self.ui.tabla.setColumnCount(10)
                headers = ["ID","Orig X", "Orig Y", "Dest X", "Dest Y", 
                "Velocidad" ,"Red",  "Green", "Blue", "Distancia"]
                self.ui.tabla.setHorizontalHeaderLabels(headers)
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(particula.id)
                origenX_widget = QTableWidgetItem(particula.origenX)
                origenY_widget = QTableWidgetItem(particula.origenY)
                destinoX_widget = QTableWidgetItem(particula.destinoX)
                destinoY_widget = QTableWidgetItem(particula.destinoY)
                velocidad_widget = QTableWidgetItem(particula.velocidad)
                red_widget = QTableWidgetItem(particula.red)
                green_widget = QTableWidgetItem(particula.green)
                blue_widget = QTableWidgetItem(particula.blue)
                distancia_widget = QTableWidgetItem(particula.distancia)

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origenX_widget)
                self.ui.tabla.setItem(0, 2, origenY_widget)
                self.ui.tabla.setItem(0, 3, destinoX_widget)
                self.ui.tabla.setItem(0, 4, destinoY_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                find = True
                return

        if not find:
            QMessageBox.warning(
                self,
                "Atencion",
                "La particula" + identificador + "no encontrada"
            )    
        


    @Slot()
    def action_abrir_archivo(self):
        dir = QFileDialog.getOpenFileName(
            self, 
            "Abrir Archivo:",
            ".",
            "JSON (*.json)"
        )[0]
        if self.lista.abrir(dir):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrió el archivo " + dir
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + dir
            )

    @Slot()
    def action_guardar_archivo(self):
        #print("Guardando archivo")
        dir = QFileDialog.getSaveFileName(
            self, 
            "Guardar como:",
            ".",
            "JSON (*.json)"
        )[0]

        if self.lista.guardar(dir):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear y guardar datos del archivo " + dir
            )
        else:
            QMessageBox.critical(
                self, 
                "Error",
                "No se pudo crear y/o guardar datos en el archivo " + dir
            )

    @Slot()
    def click_agregar_inicio(self):
        self.id = self.id + int(1)
        origenx = float(self.ui.Origen_X_lineEdit.text())
        origeny = float(self.ui.Origen_Y_lineEdit.text())
        destinox = float(self.ui.DestinoX_lineEdit.text())
        destinoy = float(self.ui.DestinoY_lineEdit.text())
        velocidad = float(self.ui.Velocidad_lineEdit.text())
        red = float(self.ui.Red_lineEdit.text())
        green = float(self.ui.Green_lineEdit.text())
        blue = float(self.ui.Blue_lineEdit.text())

        particula = Particula(self.id, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)

        self.lista.agregar_inicio(particula)

    @Slot()
    def click_agregar_final(self):
        self.id = self.id + int(1)
        origenx = float(self.ui.Origen_X_lineEdit.text())
        origeny = float(self.ui.Origen_Y_lineEdit.text())
        destinox = float(self.ui.DestinoX_lineEdit.text())
        destinoy = float(self.ui.DestinoY_lineEdit.text())
        velocidad = float(self.ui.Velocidad_lineEdit.text())
        red = float(self.ui.Red_lineEdit.text())
        green = float(self.ui.Green_lineEdit.text())
        blue = float(self.ui.Blue_lineEdit.text())

        particula = Particula(self.id, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)

        self.lista.agregar_final(particula)

        #self.ui.Salida.insertPlainText()

    @Slot()
    def click_mostrar(self):

        self.ui.Salida.clear()
        self.ui.Salida.insertPlainText(str(self.lista))


