# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(398, 405)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Mostrar_pushButton = QPushButton(self.centralwidget)
        self.Mostrar_pushButton.setObjectName(u"Mostrar_pushButton")

        self.gridLayout_2.addWidget(self.Mostrar_pushButton, 4, 0, 1, 1)

        self.Agregar_inicio_pushButton = QPushButton(self.centralwidget)
        self.Agregar_inicio_pushButton.setObjectName(u"Agregar_inicio_pushButton")

        self.gridLayout_2.addWidget(self.Agregar_inicio_pushButton, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Velocidad = QLabel(self.groupBox)
        self.Velocidad.setObjectName(u"Velocidad")

        self.gridLayout.addWidget(self.Velocidad, 4, 1, 1, 1)

        self.DestinoX_lineEdit = QLineEdit(self.groupBox)
        self.DestinoX_lineEdit.setObjectName(u"DestinoX_lineEdit")

        self.gridLayout.addWidget(self.DestinoX_lineEdit, 2, 3, 1, 2)

        self.DestinoY = QLabel(self.groupBox)
        self.DestinoY.setObjectName(u"DestinoY")

        self.gridLayout.addWidget(self.DestinoY, 3, 1, 1, 2)

        self.DestinoX = QLabel(self.groupBox)
        self.DestinoX.setObjectName(u"DestinoX")

        self.gridLayout.addWidget(self.DestinoX, 2, 1, 1, 2)

        self.Origen_Y = QLabel(self.groupBox)
        self.Origen_Y.setObjectName(u"Origen_Y")

        self.gridLayout.addWidget(self.Origen_Y, 1, 1, 1, 1)

        self.DestinoY_lineEdit = QLineEdit(self.groupBox)
        self.DestinoY_lineEdit.setObjectName(u"DestinoY_lineEdit")

        self.gridLayout.addWidget(self.DestinoY_lineEdit, 3, 3, 1, 2)

        self.Red_lineEdit = QLineEdit(self.groupBox)
        self.Red_lineEdit.setObjectName(u"Red_lineEdit")

        self.gridLayout.addWidget(self.Red_lineEdit, 8, 3, 1, 2)

        self.Green = QLabel(self.groupBox)
        self.Green.setObjectName(u"Green")

        self.gridLayout.addWidget(self.Green, 12, 1, 1, 1)

        self.Red = QLabel(self.groupBox)
        self.Red.setObjectName(u"Red")

        self.gridLayout.addWidget(self.Red, 8, 1, 1, 1)

        self.Blue = QLabel(self.groupBox)
        self.Blue.setObjectName(u"Blue")

        self.gridLayout.addWidget(self.Blue, 14, 1, 1, 1)

        self.Green_lineEdit = QLineEdit(self.groupBox)
        self.Green_lineEdit.setObjectName(u"Green_lineEdit")

        self.gridLayout.addWidget(self.Green_lineEdit, 12, 3, 1, 2)

        self.Velocidad_lineEdit = QLineEdit(self.groupBox)
        self.Velocidad_lineEdit.setObjectName(u"Velocidad_lineEdit")

        self.gridLayout.addWidget(self.Velocidad_lineEdit, 4, 3, 1, 2)

        self.Blue_lineEdit = QLineEdit(self.groupBox)
        self.Blue_lineEdit.setObjectName(u"Blue_lineEdit")

        self.gridLayout.addWidget(self.Blue_lineEdit, 14, 3, 1, 2)

        self.Origen_X = QLabel(self.groupBox)
        self.Origen_X.setObjectName(u"Origen_X")

        self.gridLayout.addWidget(self.Origen_X, 0, 1, 1, 1)

        self.Origen_Y_lineEdit = QLineEdit(self.groupBox)
        self.Origen_Y_lineEdit.setObjectName(u"Origen_Y_lineEdit")

        self.gridLayout.addWidget(self.Origen_Y_lineEdit, 1, 3, 1, 2)

        self.Origen_X_lineEdit = QLineEdit(self.groupBox)
        self.Origen_X_lineEdit.setObjectName(u"Origen_X_lineEdit")

        self.gridLayout.addWidget(self.Origen_X_lineEdit, 0, 3, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)

        self.Agregar_final_pushButton = QPushButton(self.centralwidget)
        self.Agregar_final_pushButton.setObjectName(u"Agregar_final_pushButton")

        self.gridLayout_2.addWidget(self.Agregar_final_pushButton, 3, 0, 1, 1)

        self.Salida = QPlainTextEdit(self.centralwidget)
        self.Salida.setObjectName(u"Salida")

        self.gridLayout_2.addWidget(self.Salida, 1, 1, 4, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 398, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.Mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar elementos", None))
        self.Agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particula", None))
        self.Velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.DestinoY.setText(QCoreApplication.translate("MainWindow", u"Destino Y: (0 - 500) ", None))
        self.DestinoX.setText(QCoreApplication.translate("MainWindow", u"Destino X: (0 - 500) ", None))
        self.Origen_Y.setText(QCoreApplication.translate("MainWindow", u"Origen Y: (0 - 500)", None))
        self.Green.setText(QCoreApplication.translate("MainWindow", u"Green: (0 - 255)", None))
        self.Red.setText(QCoreApplication.translate("MainWindow", u"Red: (0 - 255)", None))
        self.Blue.setText(QCoreApplication.translate("MainWindow", u"Blue: (0 - 255)", None))
        self.Origen_X.setText(QCoreApplication.translate("MainWindow", u"Origen X: (0 - 500)", None))
        self.Agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

