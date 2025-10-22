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
                           QPalette, QPixmap, QRadialGradient, QTransform, QIntValidator)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayoutTitulo = QHBoxLayout()
        self.horizontalLayoutTitulo.setObjectName(u"horizontalLayoutTitulo")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutTitulo.addItem(self.horizontalSpacer_2)

        self.lblTitulo = QLabel(self.centralwidget)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblTitulo.sizePolicy().hasHeightForWidth())
        self.lblTitulo.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(24)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayoutTitulo.addWidget(self.lblTitulo)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutTitulo.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayoutTitulo)

        self.lblInfoArchivo = QLabel(self.centralwidget)
        self.lblInfoArchivo.setObjectName(u"lblInfoArchivo")
        self.lblInfoArchivo.setEnabled(True)
        self.lblInfoArchivo.setMinimumSize(QSize(520, 60))
        self.lblInfoArchivo.setMaximumSize(QSize(720, 60))

        self.verticalLayout.addWidget(self.lblInfoArchivo)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1060, 313))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy3)
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollAreaWidgetContents.setAutoFillBackground(True)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnGrabar = QPushButton(self.centralwidget)
        self.btnGrabar.setObjectName(u"btnGrabar")
        self.btnGrabar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"../assets/microphone_fill.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnGrabar.setIcon(icon)
        self.btnGrabar.setIconSize(QSize(24, 16))

        self.horizontalLayout_2.addWidget(self.btnGrabar)

        self.btnDetenerGrabacion = QPushButton(self.centralwidget)
        self.btnDetenerGrabacion.setObjectName(u"btnDetenerGrabacion")
        icon1 = QIcon()
        icon1.addFile(u"../../../../../../Pictures/SVGs/record-stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDetenerGrabacion.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btnDetenerGrabacion)

        self.btnReproducir = QPushButton(self.centralwidget)
        self.btnReproducir.setObjectName(u"btnReproducir")
        self.btnReproducir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"../assets/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnReproducir.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btnReproducir)

        self.btnDetener = QPushButton(self.centralwidget)
        self.btnDetener.setObjectName(u"btnDetener")
        self.btnDetener.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"../assets/stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnDetener.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.btnDetener)

        self.btnAnalizar = QPushButton(self.centralwidget)
        self.btnAnalizar.setObjectName(u"btnAnalizar")
        self.btnAnalizar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAnalizar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon4 = QIcon()
        icon4.addFile(u"../assets/waves-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnAnalizar.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.btnAnalizar)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnGuardar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u"../assets/folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnGuardar.setIcon(icon5)
        self.btnGuardar.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.btnGuardar)

        self.btnCargar = QPushButton(self.centralwidget)
        self.btnCargar.setObjectName(u"btnCargar")
        self.btnCargar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"../assets/upload.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnCargar.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.btnCargar)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btnGenerarTono = QPushButton(self.centralwidget)
        self.btnGenerarTono.setObjectName(u"btnGenerarTono")
        self.btnGenerarTono.setEnabled(True)
        self.btnGenerarTono.setMaximumSize(QSize(90, 25))
        self.btnGenerarTono.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnGenerarTono)

        self.gbControles = QGroupBox(self.centralwidget)
        self.gbControles.setObjectName(u"gbControles")
        self.gbControles.setEnabled(False)
        self.gbControles.setMinimumSize(QSize(0, 90))
        self.gbControles.setMaximumSize(QSize(600, 16777215))
        self.gbControles.setChecked(False)
        self.gbtnCancelarTono = QPushButton(self.gbControles)
        self.gbtnCancelarTono.setObjectName(u"gbtnCancelarTono")
        self.gbtnCancelarTono.setGeometry(QRect(480, 60, 91, 24))
        self.gbtnCancelarTono.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lblFrecuencia = QLabel(self.gbControles)
        self.lblFrecuencia.setObjectName(u"lblFrecuencia")
        self.lblFrecuencia.setGeometry(QRect(10, 20, 91, 16))
        self.gbTipoFuncion = QGroupBox(self.gbControles)
        self.gbTipoFuncion.setObjectName(u"gbTipoFuncion")
        self.gbTipoFuncion.setGeometry(QRect(400, 10, 171, 41))
        self.gbTipoFuncion.setFlat(False)
        self.gbTipoFuncion.setCheckable(False)
        self.grbSeno = QRadioButton(self.gbTipoFuncion)
        self.grbSeno.setObjectName(u"grbSeno")
        self.grbSeno.setGeometry(QRect(10, 10, 61, 20))
        self.grbSeno.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.grbCoseno = QRadioButton(self.gbTipoFuncion)
        self.grbCoseno.setObjectName(u"grbCoseno")
        self.grbCoseno.setGeometry(QRect(90, 10, 71, 20))
        self.grbCoseno.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.grbCoseno.setCheckable(True)
        self.grbCoseno.setChecked(False)
        self.grbCoseno.setAutoRepeat(False)
        self.grbCoseno.setAutoExclusive(True)
        self.lblAmplitud = QLabel(self.gbControles)
        self.lblAmplitud.setObjectName(u"lblAmplitud")
        self.lblAmplitud.setGeometry(QRect(170, 20, 61, 16))
        self.sldAmplitud = QSlider(self.gbControles)
        self.sldAmplitud.setObjectName(u"sldAmplitud")
        self.sldAmplitud.setGeometry(QRect(230, 20, 160, 22))
        self.sldAmplitud.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sldAmplitud.setMaximum(100)
        self.sldAmplitud.setSingleStep(1)
        self.sldAmplitud.setPageStep(10)
        self.sldAmplitud.setValue(0)
        self.sldAmplitud.setTracking(True)
        self.sldAmplitud.setOrientation(Qt.Orientation.Horizontal)
        self.sldAmplitud.setInvertedAppearance(False)
        self.sldAmplitud.setInvertedControls(False)
        self.sldAmplitud.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.sldAmplitud.setTickInterval(0)
        self.gbtnDetener = QPushButton(self.gbControles)
        self.gbtnDetener.setObjectName(u"gbtnDetener")
        self.gbtnDetener.setGeometry(QRect(90, 60, 75, 24))
        self.gbtnDetener.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"../assets/stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.gbtnDetener.setIcon(icon7)
        self.txtFrecuencia = QLineEdit(self.gbControles)
        self.txtFrecuencia.setObjectName(u"txtFrecuencia")
        self.txtFrecuencia.setGeometry(QRect(100, 20, 61, 22))
        validator = QIntValidator(20, 20000)
        self.txtFrecuencia.setValidator(validator)
        self.gbtnReproducir = QPushButton(self.gbControles)
        self.gbtnReproducir.setObjectName(u"gbtnReproducir")
        self.gbtnReproducir.setGeometry(QRect(10, 60, 75, 24))
        self.gbtnReproducir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"../assets/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.gbtnReproducir.setIcon(icon8)

        self.verticalLayout.addWidget(self.gbControles)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lenguaje del Sonido", None))
        self.lblTitulo.setText(QCoreApplication.translate("MainWindow", u"El Lenguaje del Sonido: Creaci\u00f3n y An\u00e1lisis de Ondas Sonoras\n"
"", None))
        self.lblInfoArchivo.setText("")
        self.btnGrabar.setText(QCoreApplication.translate("MainWindow", u"Grabar", None))
        self.btnDetenerGrabacion.setText(QCoreApplication.translate("MainWindow", u"Detener Grabaci\u00f3n", None))
        self.btnReproducir.setText(QCoreApplication.translate("MainWindow", u"Reproducir", None))
        self.btnDetener.setText(QCoreApplication.translate("MainWindow", u"Detener", None))
        self.btnAnalizar.setText(QCoreApplication.translate("MainWindow", u"Analizar", None))
        self.btnGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.btnCargar.setText(QCoreApplication.translate("MainWindow", u"Cargar Archivo", None))
        self.btnGenerarTono.setText(QCoreApplication.translate("MainWindow", u"Generar Tono", None))
        self.gbControles.setTitle(QCoreApplication.translate("MainWindow", u"Controles", None))
        self.gbtnCancelarTono.setText(QCoreApplication.translate("MainWindow", u"Cancelar Tono", None))
        self.lblFrecuencia.setText(QCoreApplication.translate("MainWindow", u"Frecuencia (Hz):", None))
        self.gbTipoFuncion.setTitle("")
        self.grbSeno.setText(QCoreApplication.translate("MainWindow", u"Seno", None))
        self.grbCoseno.setText(QCoreApplication.translate("MainWindow", u"Coseno", None))
        self.lblAmplitud.setText(QCoreApplication.translate("MainWindow", u"Amplitud:", None))
        self.gbtnDetener.setText("")
        self.gbtnReproducir.setText("")
    # retranslateUi

