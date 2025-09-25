import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from Main_ui import Ui_MainWindow  # Importación de la interfaz

# Importación desde otros archivos
from grafica import MplCanvas
from controlers_manager import AudioManager
from upload_file import UploadFile
from save_audio import SaveAudioHandler


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


      # Herencia de las clases
        self.audio_manager = AudioManager()
        self.upload_file = UploadFile()
        self.save_handler = SaveAudioHandler(self)
        
        self.grafica_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.grafica_layout.setContentsMargins(0, 0, 0, 0)
        self.grafica_layout.setSpacing(5)
        
        self.grafica_mostradas = []
        
        self.datos_audio_cargado = None
        self.samplerate_cargado = None
        
        # Conexión de los botones a la interfaz
        self.btnGenerarTono.clicked.connect(self.activar_controles)
        self.gbtnCancelarTono.clicked.connect(self.desactivar_controles)
        
        # Conexión de los botones a la lógica
        self.btnAnalizar.clicked.connect(self.analizar_sonido)
        self.gbtnReproducir.clicked.connect(self.reproducir_sonido)
        self.gbtnDetener.clicked.connect(self.detener_sonido)
        self.btnCargar.clicked.connect(self.cargar_archivo_audio)
        self.btnGuardar.clicked.connect(lambda: self.save_handler.guardar_audio(None))
    
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
        
    # Funciones para la logica
    
    def reproducir_sonido(self):
        frecuencia: str = self.txtFrecuencia.text()
        amplitud: int = self.sldAmplitud.value()
        funcion: str = "Coseno" if self.grbCoseno.isChecked() else "Seno"
        
        self.limpiar_graficas()
        
        # Envio de datos para generar onda
        onda = self.audio_manager.generar_datos_onda(frecuencia, amplitud, funcion)

        # reproducir onda
        self.audio_manager.reproducir_onda(onda)
        
        if onda is not None:
            self.mostrar_grafica(onda)
    
    def detener_sonido(self):
        self.audio_manager.detener_onda()
        self.limpiar_graficas()
        
    def mostrar_grafica(self, onda):
        
        nueva_grafica = MplCanvas(self.scrollAreaWidgetContents)
        nueva_grafica.iniciar_animacion(onda)
        
        self.grafica_layout.addWidget(nueva_grafica)
        self.grafica_mostradas.append(nueva_grafica)
        
    def limpiar_graficas(self):
        for grafica in self.grafica_mostradas:
            if grafica.animacion:
                grafica.animacion.event_source.stop()
            self.grafica_layout.removeWidget(grafica)
            grafica.deleteLater()
        self.grafica_mostradas = []
        
    
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
    
    def analizar_sonido(self):
        if self.datos_audio_cargado is not None:
            # Aquí va el codigo para analizar el sonido usando los datos cargados
            print("Analizando sonido...")
        else:
            print("No hay sonido cargado para analizar.")
        # todo aplicar Fourier

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

