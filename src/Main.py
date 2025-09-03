import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Main_ui import Ui_MainWindow # Importanción de la interfaz
from PySide6.QtWidgets import QFileDialog
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.datos_audio_cargado = None
        self.samplerate_cargado = None

        # Conecta el botón "Cargar archivo" a una función
        self.btnCargar.clicked.connect(self.cargar_archivo_audio)

        # Conecta el botón "Analizar" a una función
        self.btnAnalizar.clicked.connect(self.analizar_sonido)

        # Conecta el boton "Generar Tono" a una función
        self.btnGenerarTono.clicked.connect(self.activar_controles)

        # Conecta el boton "Cancelar Tono" a una función
        self.gbtnCancelarTono.clicked.connect(self.desactivar_controles)

    def cargar_archivo_audio(self):
        """
        Abre un dialogo de seleccion de archivos y carga un archivo de audio.
        """
        archivo_path, _ = QFileDialog.getOpenFileName(
            self,
            caption="Seleccionar archivo de audio",
            dir="",
            filter="Archivo de audio (*.wav *.mp3 *.ogg);;Todos los archivos"
        )

        if archivo_path:
            try:
                datos_audio, samplerate = sf.read(archivo_path)
                self.datos_audio_cargado = datos_audio
                self.samplerate_cargado = samplerate

                print(f"Archivo cargado: {archivo_path}")
                print(f"Tasa de muestreo: {samplerate} Hz")
                print(f"Numero de muestras: {len(datos_audio)}")

                self.btnAnalizar.setEnabled(True)

            except Exception as e:
                print(f"Error al cargar archivo: {e}")


    # todo aplicar Fourier
    def analizar_sonido(self):
        if self.datos_audio_cargado is not None:
            # Aquí va el codigo para analizar el sonido usando los datos cargados
            print("Analizando sonido...")
        else:
            print("No hay sonido cargado para analizar.")

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