import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QMessageBox
from Main_ui import Ui_MainWindow  # Importación de la interfaz

# Importación desde otros archivos
from Grafica import MplCanvas
from Controlers_manager import AudioManager
from upload_file import UploadFile
from save_audio import SaveAudioHandler

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

      # Instancias de las clases
        self.audio_manager = AudioManager()
        self.upload_file = UploadFile()
        self.save_handler = SaveAudioHandler(self)
        
        self.grafica_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.grafica_layout.setContentsMargins(0, 0, 0, 0)
        self.grafica_layout.setSpacing(5)
        
        self.grafica_mostradas = []
        
        self.datos_audio_cargado = None
        self.samplerate_cargado = None
        self.nombre_archivo_cargado = None
        
        # Conexión de los botones a la interfaz
        self.btnGenerarTono.clicked.connect(self.activar_controles)
        self.gbtnCancelarTono.clicked.connect(self.desactivar_controles)
        
        # Conexión de los botones a la lógica
        self.gbtnReproducir.clicked.connect(self.reproducir_tono_generado)
        self.gbtnDetener.clicked.connect(self.detener_sonido)
        self.btnReproducir.clicked.connect(self.reproducir_audio_externo)
        self.btnAnalizar.clicked.connect(self.analizar_sonido)
        self.btnCargar.clicked.connect(self.cargar_archivo_audio)
        self.btnGuardar.clicked.connect(lambda: self.save_handler.guardar_audio(None))

        self.btnReproducir.setEnabled(False)
        self.btnAnalizar.setEnabled(False)
    
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
        self.detener_sonido()
        
    # Funciones para la logica
    
    def reproducir_tono_generado(self):
        frecuencia: str = self.txtFrecuencia.text()

        try:
            frecuencia_int = int(frecuencia)
            amplitud: int = self.sldAmplitud.value()
            funcion: str = "Coseno" if self.grbCoseno.isChecked() else "Seno"

            self.limpiar_graficas()

            # Envio de datos para generar onda
            onda = self.audio_manager.generar_datos_onda(frecuencia_int, amplitud, funcion)

            # reproducir onda
            if onda is not None:
                self.mostrar_grafica_tono(onda)
                self.audio_manager.reproducir_onda(onda)

        except ValueError:
            QMessageBox.warning(self, "Error de Entrada",
                                "Por favor, ingresa un frecuencia valida (número entre 20 y 20000).",
                                )

        except Exception as e:
            QMessageBox.critical(self, "Error Inesperado",
                                 f"Ocurrio un error al intentar reproducir el sonido: {e}",
                                 )

    def reproducir_audio_externo(self):
        #Reproduce el archivo cargado o el audio grabado (todo implementar audio grabado).
        if self.datos_audio_cargado is not None:
            self.audio_manager.reproducir_archivo_cargado(self.datos_audio_cargado, self.samplerate_cargado)
            self.mostrar_grafica_archivo(self.datos_audio_cargado)
        else:
            QMessageBox.information(self, "Sin Audio", "Primero debe cargar o grabar un archivo de audio.")

    def detener_sonido(self):
        self.audio_manager.detener_sonido()
        self.limpiar_graficas()
        
    def mostrar_grafica_tono(self, onda):

        frecuencia:int = int(self.txtFrecuencia.text())
        
        nueva_grafica = MplCanvas(self.scrollAreaWidgetContents)
        nueva_grafica.iniciar_animacion(onda, frecuencia)
        
        self.grafica_layout.addWidget(nueva_grafica)
        self.grafica_mostradas.append(nueva_grafica)

    def mostrar_grafica_archivo(self, datos_audio):
        # Muestra una gráfica estática del archivo de audio cargado.
        self.limpiar_graficas()

        # Enviar datos para visualización estática
        nueva_grafica = MplCanvas(self.scrollAreaWidgetContents, animation_on=False)
        nueva_grafica.plot_data(datos_audio)

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
        
        datos_audio, samplerate, nombre_archivo = self.upload_file.cargar_archivo_audio()

        if datos_audio is not None:
            self.datos_audio_cargado = datos_audio
            self.samplerate_cargado = samplerate
            self.nombre_archivo_cargado = nombre_archivo

            # Cáculo de duración para feedback
            duracion_segundos = len(datos_audio) / samplerate

            # 1. Mostrar feedback en la interfaz
            info = (
                f"Archivo: {nombre_archivo}\n"
                f"Duración: {duracion_segundos:.2f}s\n"
                f"Tasa de muestreo: {samplerate} Hz\n"
                f"Muestras: {len(datos_audio)}"

            )
            # Asume que existe self.lblInfoArchivo para mostrar esto
            if hasattr(self, 'lblInfoArchivo'):
                self.lblInfoArchivo.setText(info)
            else:
                print(f"Info: {info}")

            # 2. Habilitar botones para operar sobre el archivo
            self.btnAnalizar.setEnabled(True)
            self.btnReproducir.setEnabled(True)

            # 3. Mostrar gráfica estática del archivo
            self.mostrar_grafica_archivo(datos_audio)

        else:
            # Si se cancela o falla, limpia y deshabilita
            self.limpiar_graficas()
            if hasattr(self, 'lblInfoArchivo'):
                self.lblInfoArchivo.setText("No hay archivo cargado.")
            self.btnAnalizar.setEnabled(False)
            self.btnReproducir.setEnabled(False)
            self.datos_audio_cargado = None
            self.samplerate_cargado = None
            self.nombre_archivo_cargado = None
    
    def analizar_sonido(self):
        #todo Calcula y muestra el espectro de frecuencias (FFT) del audio cargado
        if self.datos_audio_cargado is not None:
            # Lógica de Fourier va aquí...
            QMessageBox.information(self, "Estamos trabajando", "Analizando sonido...")
        else:
            QMessageBox.information(self, "Sin Audio", "No hay sonido cargado para analizar.")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

