# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSlider, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QSize(1080, 720))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnCargar = QPushButton(self.centralwidget)
        self.btnCargar.setObjectName(u"btnCargar")
        self.btnCargar.setGeometry(QRect(890, 660, 91, 24))
        self.btnGrabar = QPushButton(self.centralwidget)
        self.btnGrabar.setObjectName(u"btnGrabar")
        self.btnGrabar.setGeometry(QRect(810, 630, 75, 24))
        self.btnReproducir = QPushButton(self.centralwidget)
        self.btnReproducir.setObjectName(u"btnReproducir")
        self.btnReproducir.setGeometry(QRect(810, 660, 75, 24))
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(890, 630, 91, 23))
        self.btnAnalizar = QPushButton(self.centralwidget)
        self.btnAnalizar.setObjectName(u"btnAnalizar")
        self.btnAnalizar.setGeometry(QRect(990, 660, 75, 24))
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(50, 120, 980, 360))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 978, 358))
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 5, 880, 85))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.lblTitulo = QLabel(self.centralwidget)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setGeometry(QRect(100, 10, 881, 41))
        font = QFont()
        font.setPointSize(24)
        self.lblTitulo.setFont(font)
        self.lblFrecuencia = QLabel(self.centralwidget)
        self.lblFrecuencia.setObjectName(u"lblFrecuencia")
        self.lblFrecuencia.setGeometry(QRect(10, 660, 91, 16))
        self.lblAmplitud = QLabel(self.centralwidget)
        self.lblAmplitud.setObjectName(u"lblAmplitud")
        self.lblAmplitud.setGeometry(QRect(170, 660, 61, 16))
        self.txtFrecuencia = QLineEdit(self.centralwidget)
        self.txtFrecuencia.setObjectName(u"txtFrecuencia")
        self.txtFrecuencia.setGeometry(QRect(100, 660, 61, 22))
        self.sldAmplitud = QSlider(self.centralwidget)
        self.sldAmplitud.setObjectName(u"sldAmplitud")
        self.sldAmplitud.setGeometry(QRect(230, 660, 160, 22))
        self.sldAmplitud.setOrientation(Qt.Orientation.Horizontal)
        self.gbTipoFuncion = QGroupBox(self.centralwidget)
        self.gbTipoFuncion.setObjectName(u"gbTipoFuncion")
        self.gbTipoFuncion.setGeometry(QRect(400, 650, 171, 41))
        self.rbSeno = QRadioButton(self.gbTipoFuncion)
        self.rbSeno.setObjectName(u"rbSeno")
        self.rbSeno.setGeometry(QRect(10, 10, 61, 20))
        self.rbCoseno = QRadioButton(self.gbTipoFuncion)
        self.rbCoseno.setObjectName(u"rbCoseno")
        self.rbCoseno.setGeometry(QRect(90, 10, 71, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lenguaje del Sonido", None))
        self.btnCargar.setText(QCoreApplication.translate("MainWindow", u"Cargar Archivo", None))
        self.btnGrabar.setText(QCoreApplication.translate("MainWindow", u"Grabar", None))
        self.btnReproducir.setText(QCoreApplication.translate("MainWindow", u"Reproducir", None))
        self.btnGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.btnAnalizar.setText(QCoreApplication.translate("MainWindow", u"Analizar", None))
        self.lblTitulo.setText(QCoreApplication.translate("MainWindow", u"El Lenguaje del Sonido: Creaci\u00f3n y An\u00e1lisis de Ondas Sonoras\n"
"", None))
        self.lblFrecuencia.setText(QCoreApplication.translate("MainWindow", u"Frecuencia (Hz):", None))
        self.lblAmplitud.setText(QCoreApplication.translate("MainWindow", u"Amplitud:", None))
        self.gbTipoFuncion.setTitle("")
        self.rbSeno.setText(QCoreApplication.translate("MainWindow", u"Seno", None))
        self.rbCoseno.setText(QCoreApplication.translate("MainWindow", u"Coseno", None))
    # retranslateUi

