import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from Main_ui import Ui_MainWindow  # Importación de la interfaz
from audio_manager import AudioManager
from upload_file import UploadFile


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Herencia de las clases
        self.audio_manager = AudioManager()
        self.upload_file = UploadFile()
        
        self.datos_audio_cargado = None
        self.samplerate_cargado = None
        
        
        # Conexión de los botones de la interfaz
        self.btnGenerarTono.clicked.connect(self.activar_controles)
        self.gbtnCancelarTono.clicked.connect(self.desactivar_controles)
        
        # Conexión de los botones a la lógica
        self.btnAnalizar.clicked.connect(self.analizar_sonido)
        self.gbtnReproducir.clicked.connect(self.reproducir_sonido)
        self.gbtnDetener.clicked.connect(self.detener_sonido)
        self.btnCargar.clicked.connect(self.cargar_archivo_audio)
    
    
    def analizar_sonido(self):
        if self.datos_audio_cargado is not None:
            # Aquí va el codigo para analizar el sonido usando los datos cargados
            print("Analizando sonido...")
        else:
            print("No hay sonido cargado para analizar.")
        # todo aplicar Fourier
    
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
        
    def cargar_archivo_audio(self):
        
        datos_audio, samplerate = self.upload_file.cargar_archivo_audio()
        
        if datos_audio is not None:
            self.datos_audio_cargado = datos_audio
            self.samplerate_cargado = samplerate
            
            print(f"Archivo cargado. Tasa de muestreo: {samplerate} Hz")
            print(f"Número de muestras: {len(datos_audio)}")
            
            self.btnAnalizar.setEnabled(True)
        else:
            print("No se seleccionó un archivo o hubo un error.")
    
    def reproducir_sonido(self):
        frecuencia: int = self.txtFrecuencia.text()
        amplitud: int = self.sldAmplitud.value()
        funcion: str = "Coseno" if self.grbCoseno.isChecked() else "Seno"
        
        # envio de datos a la clase AudioManager
        self.audio_manager.reproducir_tono(frecuencia, amplitud, funcion)
        
        # todo devolver datos y poner grafica en la interfaz
    
    def detener_sonido(self):
        # todo algo
        pass
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())