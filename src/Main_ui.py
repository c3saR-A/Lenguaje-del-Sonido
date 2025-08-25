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
        MainWindow.setEnabled(True)
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
        self.btnReproducir.setGeometry(QRect(990, 630, 75, 24))
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(890, 630, 91, 23))
        self.btnGuardar.setIconSize(QSize(24, 24))
        self.btnAnalizar = QPushButton(self.centralwidget)
        self.btnAnalizar.setObjectName(u"btnAnalizar")
        self.btnAnalizar.setGeometry(QRect(810, 660, 75, 24))
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
        self.btnGenerarTono = QPushButton(self.centralwidget)
        self.btnGenerarTono.setObjectName(u"btnGenerarTono")
        self.btnGenerarTono.setEnabled(True)
        self.btnGenerarTono.setGeometry(QRect(10, 570, 91, 24))
        self.gbControles = QGroupBox(self.centralwidget)
        self.gbControles.setObjectName(u"gbControles")
        self.gbControles.setEnabled(False)
        self.gbControles.setGeometry(QRect(10, 600, 581, 91))
        self.gbControles.setChecked(False)
        self.btnCancelarTono = QPushButton(self.gbControles)
        self.btnCancelarTono.setObjectName(u"btnCancelarTono")
        self.btnCancelarTono.setGeometry(QRect(480, 60, 91, 24))
        self.lblFrecuencia = QLabel(self.gbControles)
        self.lblFrecuencia.setObjectName(u"lblFrecuencia")
        self.lblFrecuencia.setGeometry(QRect(10, 20, 91, 16))
        self.gbTipoFuncion = QGroupBox(self.gbControles)
        self.gbTipoFuncion.setObjectName(u"gbTipoFuncion")
        self.gbTipoFuncion.setGeometry(QRect(400, 10, 171, 41))
        self.rbSeno = QRadioButton(self.gbTipoFuncion)
        self.rbSeno.setObjectName(u"rbSeno")
        self.rbSeno.setGeometry(QRect(10, 10, 61, 20))
        self.rbCoseno = QRadioButton(self.gbTipoFuncion)
        self.rbCoseno.setObjectName(u"rbCoseno")
        self.rbCoseno.setGeometry(QRect(90, 10, 71, 20))
        self.lblAmplitud = QLabel(self.gbControles)
        self.lblAmplitud.setObjectName(u"lblAmplitud")
        self.lblAmplitud.setGeometry(QRect(170, 20, 61, 16))
        self.sldAmplitud = QSlider(self.gbControles)
        self.sldAmplitud.setObjectName(u"sldAmplitud")
        self.sldAmplitud.setGeometry(QRect(230, 20, 160, 22))
        self.sldAmplitud.setOrientation(Qt.Orientation.Horizontal)
        self.btnStop = QPushButton(self.gbControles)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setGeometry(QRect(90, 60, 75, 24))
        icon = QIcon()
        icon.addFile(u"C:/Users/Alexander Cortez/OneDrive/Escritorio/stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStop.setIcon(icon)
        self.txtFrecuencia = QLineEdit(self.gbControles)
        self.txtFrecuencia.setObjectName(u"txtFrecuencia")
        self.txtFrecuencia.setGeometry(QRect(100, 20, 61, 22))
        self.btnPlay = QPushButton(self.gbControles)
        self.btnPlay.setObjectName(u"btnPlay")
        self.btnPlay.setGeometry(QRect(10, 60, 75, 24))
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/Alexander Cortez/OneDrive/Escritorio/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPlay.setIcon(icon1)
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
        self.btnGenerarTono.setText(QCoreApplication.translate("MainWindow", u"Generar Tono", None))
        self.gbControles.setTitle(QCoreApplication.translate("MainWindow", u"Controles", None))
        self.btnCancelarTono.setText(QCoreApplication.translate("MainWindow", u"Cancelar Tono", None))
        self.lblFrecuencia.setText(QCoreApplication.translate("MainWindow", u"Frecuencia (Hz):", None))
        self.gbTipoFuncion.setTitle("")
        self.rbSeno.setText(QCoreApplication.translate("MainWindow", u"Seno", None))
        self.rbCoseno.setText(QCoreApplication.translate("MainWindow", u"Coseno", None))
        self.lblAmplitud.setText(QCoreApplication.translate("MainWindow", u"Amplitud:", None))
        self.btnStop.setText("")
        self.btnPlay.setText("")
    # retranslateUi

