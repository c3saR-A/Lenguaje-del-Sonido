import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Main_ui import Ui_MainWindow # Importanción de la interfaz

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conecta el botón "Analizar" a una función
        self.btnAnalizar.clicked.connect(self.analizar_sonido)

        # Conecta el boton "Generar Tono" a una función
        self.btnGenerarTono.clicked.connect(self.activar_controles)

        # Conecta el boton "Cancelar Tono" a una función
        self.gbtnCancelarTono.clicked.connect(self.desactivar_controles)

    # todo aplicar Fourier
    def analizar_sonido(self):
        # Aquí va el código para analizar el sonido
        print("Analizando sonido...")

    def activar_controles(self):
        self.grbSeno.setCheckable(True)
        self.grbCoseno.setCheckable(True)
        self.gbControles.setEnabled(True)

    def desactivar_controles(self):
        self.txtFrecuencia.clear()
        self.sldAmplitud.setValue(0)
        self.grbSeno.setCheckable(False)
        self.grbCoseno.setCheckable(False)
        self.gbControles.setEnabled(False)

    # todo capturar datos de controles
    # todo generar grafica con los datos de controles
    # todo poner grafica en interfaz



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())