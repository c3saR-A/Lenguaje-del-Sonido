import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from Main_ui import Ui_MainWindow   # Importación de la interfaz
from audio_manager import AudioManager

from PySide6.QtWidgets import QFileDialog
import soundfile as sf
import numpy as np



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.audio_manager = AudioManager()
       
        self.datos_audio_cargado = None
        self.samplerate_cargado = None
        # Conexión de los botones a la logica principal
        self.btnAnalizar.clicked.connect(self.analizar_sonido)
        self.btnGenerarTono.clicked.connect(self.activar_controles)
        self.gbtnCancelarTono.clicked.connect(self.desactivar_controles)
        self.gbtnReproducir.clicked.connect(self.reproducir_sonido)
        self.gbtnDetener.clicked.connect(self.detener_sonido)
        # Conecta el botón "Cargar archivo" a una función
        self.btnCargar.clicked.connect(self.cargar_archivo_audio)
        

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