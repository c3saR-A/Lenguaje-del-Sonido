import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Main_ui import Ui_MainWindow   # Importación de la interfaz
from audio_manager import AudioManager

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.audio_manager = AudioManager()

        # Conexión de los botones a la logica principal
        self.btnAnalizar.clicked.connect(self.analizar_sonido)
        self.btnGenerarTono.clicked.connect(self.activar_controles)
        self.gbtnCancelarTono.clicked.connect(self.desactivar_controles)
        self.gbtnReproducir.clicked.connect(self.reproducir_sonido)
        self.gbtnDetener.clicked.connect(self.detener_sonido)

    # todo aplicar Fourier
    def analizar_sonido(self):
        # Aquí va el código para analizar el sonido
        print("Analizando sonido...")

    # Funciones para manejo de interfaz
    def activar_controles(self):
        self.grbSeno.setCheckable(True)
        self.grbCoseno.setCheckable(True)
        self.grbSeno.setChecked(True)
        self.gbControles.setEnabled(True)

    def desactivar_controles(self):
        self.txtFrecuencia.clear()
        self.sldAmplitud.setValue(0)
        self.grbSeno.setCheckable(False)
        self.grbCoseno.setCheckable(False)
        self.gbControles.setEnabled(False)

    # todo capturar datos de controles
    def reproducir_sonido(self):
        frecuencia: int = self.txtFrecuencia.text()
        amplitud: int = self.sldAmplitud.value()
        funcion: str = "Coseno" if self.grbCoseno.isChecked() else "Seno"

        # envio de datos a la clase AudioManager
        self.audio_manager.reproducir_tono(frecuencia, amplitud, funcion)

    def detener_sonido(self):
        # todo algo
        pass



    # todo generar grafica con los datos de controles
    # todo poner grafica en interfaz



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())