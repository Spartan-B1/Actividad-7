from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
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


