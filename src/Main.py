import sys
import numpy as np
# Importación de la interfaz y componentes
from Main_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QMessageBox, QSpacerItem, QSizePolicy
# Importación desde otros archivos
from Grafica import MplCanvas
from Controlers_manager import AudioManager
from Upload_file import UploadFile
from Save_audio import SaveAudioHandler
from Audio_Analysis_Handler import AnalisisHandler
from Recording_Controler import GrabacionThread


SAMPLERATE_GRABACION = 44100
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

      # Instancias de las clases
        self.audio_manager = AudioManager()
        self.upload_file = UploadFile()
        self.save_handler = SaveAudioHandler(self)
        self.analisis_handler = AnalisisHandler(self)
        self.recording_thread: GrabacionThread | None = None
        
        self.grafica_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.grafica_layout.setContentsMargins(0, 0, 0, 0)
        self.grafica_layout.setSpacing(50)
        
        self.grafica_mostradas = []

        self.main_window = self
        
        self.datos_audio_cargado: np.ndarray | None = None
        self.samplerate_cargado: int | None = None
        self.nombre_archivo_cargado: str | None = None
        
        # Conexión de los botones a la interfaz
        self.btnGenerarTono.clicked.connect(self.activar_controles)
        self.gbtnCancelarTono.clicked.connect(self.desactivar_controles)
        
        # Conexión de los botones a la lógica
        self.gbtnReproducir.clicked.connect(self.reproducir_tono_generado)
        self.gbtnDetener.clicked.connect(self.detener_tono_generado)
        self.btnReproducir.clicked.connect(self.reproducir_audio_externo)
        self.btnGuardar.clicked.connect(self.save_handler.guardar_audio)
        self.btnDetener.clicked.connect(self.detener_audio_externo)
        self.btnCargar.clicked.connect(self.cargar_archivo_audio)
        self.btnAnalizar.clicked.connect(self.analizar_sonido)
        self.btnGrabar.clicked.connect(self.iniciar_grabacion)
        self.btnDetenerGrabacion.clicked.connect(self.detener_grabacion)

    # Funciones para manejo de interfaz
    def activar_controles(self):
        # Habilitar componentes internos
        self.grbSeno.setCheckable(True)
        self.grbCoseno.setCheckable(True)
        self.grbSeno.setChecked(True)
        self.gbControles.setEnabled(True)


        # Deshabilitar componentes externos que interfieren
        self.btnCargar.setEnabled(False)
        self.btnGrabar.setEnabled(False)

        # Desactivar botones externos que no son relevantes
        self.btnDetener.setEnabled(False)
        self.btnReproducir.setEnabled(False)
        self.btnAnalizar.setEnabled(False)

    
    def desactivar_controles(self):
        # Deshabilitar componentes y limpiar
        self.txtFrecuencia.clear()
        self.sldAmplitud.setValue(0)
        self.grbSeno.setCheckable(False)
        self.grbCoseno.setCheckable(False)
        self.gbControles.setEnabled(False)

        # Habilitar componentes al estado inicial
        self.btnCargar.setEnabled(True)
        self.btnDetener.setEnabled(True)
        self.btnReproducir.setEnabled(True)
        self.btnAnalizar.setEnabled(True)
        self.btnGrabar.setEnabled(True)

        self.datos_audio_cargado = None
        self.samplerate_cargado = None
        self.nombre_archivo_cargado = None

        # Detener sonido y limpiar grafica
        self.detener_tono_generado()
        
    # Funciones para la logica
    
    def reproducir_tono_generado(self):
        frecuencia: str = self.txtFrecuencia.text()

        try:
            frecuencia_int = int(frecuencia)
            amplitud: int = self.sldAmplitud.value()
            funcion: str = "Coseno" if self.grbCoseno.isChecked() else "Seno"
            
            if (frecuencia_int < 20 or frecuencia_int > 20000) or amplitud == 0:
                QMessageBox.warning(self, 'Error de Entrada',"Valor de frecuencia o amplitud invalido")
                return

            self.limpiar_graficas()

            # Envio de datos para generar onda
            onda, samplerate = self.audio_manager.generar_datos_onda(frecuencia_int, amplitud, funcion)

            # reproducir onda
            if onda is not None:

                self.main_window.datos_audio_cargado = onda
                self.main_window.samplerate_cargado = samplerate

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
            
        else:
            QMessageBox.information(self, "Sin Audio", "Primero debe cargar o grabar un archivo de audio.")

    def detener_tono_generado(self):
        self.audio_manager.detener_sonido()
        self.limpiar_graficas()

    def detener_audio_externo(self):
        self.audio_manager.detener_sonido()
        self.limpiar_graficas()
        self.lblInfoArchivo.setText("")

        self.datos_audio_cargado = None

        # Habilitar componentes para otras funciones
        self.btnGrabar.setEnabled(True)
        self.btnGenerarTono.setEnabled(True)
        
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
        nueva_grafica.plot_data_completa(datos_audio)

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

            # Calculo de duracion
            duracion_segundos = len(datos_audio) / samplerate

            # Info a mostrar
            info = (
                f"Archivo: {nombre_archivo}\n"
                f"Duración: {duracion_segundos:.2f}s\n"
                f"Tasa de muestreo: {samplerate} Hz\n"
                f"Muestras: {len(datos_audio)}"

            )

            if hasattr(self, 'lblInfoArchivo'):
                self.lblInfoArchivo.setText(info)
            else:
                print(f"Info: {info}")

            # Deshabilitar botones para no interferir
            self.btnGrabar.setEnabled(False)
            self.btnGenerarTono.setEnabled(False)

            # Mostrar gráfica estática del archivo
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
    
    def iniciar_grabacion(self):
        # Prepara e inicia el hilo de grabación de audio.
        self.audio_manager.detener_sonido()  # Asegurar que no hay nada activo
        self.limpiar_graficas()
        
        # Cambio de UI para grabación
        self.lblInfoArchivo.setText("Grabación iniciada... \n "
                                    "Presione: 'Detener Grabación' para finalizar.")
        self.btnGrabar.setEnabled(False)
        self.btnDetenerGrabacion.setEnabled(True)  # Habilitar detención
        self.btnReproducir.setEnabled(False)
        self.btnDetener.setEnabled(False)
        self.btnAnalizar.setEnabled(False)
        self.btnCargar.setEnabled(False)
        self.btnGenerarTono.setEnabled(False)
        self.btnGuardar.setEnabled(False)
        
        # Instanciar y conectar el hilo de grabación pasando el samplerate
        self.recording_thread = GrabacionThread(samplerate=SAMPLERATE_GRABACION)
        self.recording_thread.grabacion_finalizada.connect(self.finalizar_grabacion)
        
        # Iniciar grabación
        self.recording_thread.start()
    
    def detener_grabacion(self):
        # Detener el hilo *existente* si está corriendo
        if self.recording_thread and self.recording_thread.isRunning():
            self.recording_thread.detener_grabacion()
            self.lblInfoArchivo.setText("Deteniendo Grabación... \n Grabación finalizada. Procesando los datos...")
            # La limpieza y el cambio de estado de botones se completará en finalizar_grabacion
        else:
            QMessageBox.information(self, "Error", "No hay grabación activa para detener.")
    
    def finalizar_grabacion(self, datos_audio_norm: np.ndarray):
        # Restaurar botones básicos (deshabilitar detención y habilitar inicio/carga)
        self.btnGrabar.setEnabled(True)
        self.btnCargar.setEnabled(True)
        self.btnGenerarTono.setEnabled(True)
        self.btnDetenerGrabacion.setEnabled(False)
        
        if datos_audio_norm.size > 0:
            self.datos_audio_cargado = datos_audio_norm
            self.samplerate_cargado = SAMPLERATE_GRABACION
            self.nombre_archivo_cargado = "Grabación_Reciente"
            
            # Mostrar información y gráfica
            duracion_segundos = len(datos_audio_norm) / SAMPLERATE_GRABACION
            info = (
                f"Archivo: Grabación_Reciente\n"
                f"Duración: {duracion_segundos:.2f}s\n"
                f"Tasa de muestreo: {SAMPLERATE_GRABACION} Hz\n"
                f"Muestras: {len(datos_audio_norm)}"
            )
            self.lblInfoArchivo.setText(info)
            self.mostrar_grafica_archivo(self.datos_audio_cargado)
            
            # Habilitar botones de uso para el audio grabado
            self.btnReproducir.setEnabled(True)
            self.btnDetener.setEnabled(True)
            self.btnAnalizar.setEnabled(True)
            self.btnGuardar.setEnabled(True)
        
        else:
            QMessageBox.warning(self, "Grabación Vacía", "No se grabó audio.")
            self.lblInfoArchivo.setText("No hay archivo cargado.")
            self.btnReproducir.setEnabled(False)
            self.btnDetener.setEnabled(False)
            self.btnAnalizar.setEnabled(False)
            self.btnGuardar.setEnabled(False)
        
        # Limpiar la referencia al hilo después de que ha terminado
        self.recording_thread = None
    
    def analizar_sonido(self):

        if self.datos_audio_cargado is None:
            QMessageBox.information(self, "Sin Audio", "No hay sonido cargado para analizar.")
            return

        self.audio_manager.detener_sonido()
        self.limpiar_graficas()

        datos_audio = self.datos_audio_cargado
        samplerate = self.samplerate_cargado
        duracion_muestras = len(datos_audio)

        frecuencias, amplitudes = self.analisis_handler.realizar_tranformada_rapida(datos_audio, samplerate)

        if frecuencias is None:
            QMessageBox.critical(self, "Error de Análisis",
                                 "No se pudo calcular la Tranformada Rápida. Datos inválidos.")
            return

        tonos_principales = self.analisis_handler.encontrar_tonos_principales(frecuencias, amplitudes)

        if not tonos_principales:
            QMessageBox.critical(self, "Sin tonos puros",
                                 "No se detectaron tonos puros significativos (amplitud > 1%).")

        # Grafica de fft
        titulo_fft = "1. Espectro de Frecuencia (FFT)"
        grafica_fft = MplCanvas(self.scrollAreaWidgetContents, animation_on=False, titulo=titulo_fft)
        grafica_fft.setFixedHeight(450)
        grafica_fft.plot_fft(frecuencias, amplitudes)
        self.grafica_layout.addWidget(grafica_fft)
        self.grafica_mostradas.append(grafica_fft)
        
        # Gráfica de la Onda Original (ya cargada)
        titulo_original = "2. Onda Original Cargada (Completa)"
        grafica_original = MplCanvas(self.scrollAreaWidgetContents, animation_on=False, titulo=titulo_original)
        grafica_original.setFixedHeight(300)
        grafica_original.plot_data_completa(datos_audio)
        self.grafica_layout.addWidget(grafica_original)
        self.grafica_mostradas.append(grafica_original)

        colores = ['#4C54AD', '#0542FB', '#34A88D', '#05BDFB', '#3580EA'] * (len(tonos_principales) // 5 + 1)

        for i, (frecuencia, amplitud_normalizada) in enumerate(tonos_principales):
            # Generar la onda senoidal pura
            onda_pura = self.audio_manager.sintetizar_onda(
                frecuencia,
                amplitud_normalizada,
                duracion_muestras
            )

            # Gráfica del tono puro
            nombre_tono = f"3. Tono {i + 1}: {frecuencia} Hz (Amplitud: {amplitud_normalizada})"
            grafica_tono = MplCanvas(self.scrollAreaWidgetContents, animation_on=False, titulo=nombre_tono)
            grafica_tono.setFixedHeight(250)
            grafica_tono.plot_data_parcial(onda_pura, color=colores[i])

            self.grafica_layout.addWidget(grafica_tono)
            self.grafica_mostradas.append(grafica_tono)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.grafica_layout.addItem(spacer)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

