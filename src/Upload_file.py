import os
import numpy as np
import soundfile as sf
from PySide6.QtWidgets import QFileDialog, QMessageBox


class UploadFile:
    def __init__(self):
        pass
    
    def cargar_archivo_audio(self):
        """
        Abre un cuadro de seleccion de archivos y carga un archivo de audio.
        Retorna los datos de audio y tasa de muestreo
        """
        archivo_path, _ = QFileDialog.getOpenFileName(
            caption="Seleccionar archivo de audio",
            dir="",
            filter="Archivo de audio (*.wav);;Todos los archivos",
        )

        if archivo_path:
            try:
                datos_audio, samplerate = sf.read(archivo_path, dtype='float64')

                if datos_audio.ndim > 1:
                    # Promedio de canales para convertir a mono
                    datos_audio = np.mean(datos_audio, axis=1)

                nombre_archivo = os.path.basename(archivo_path)
                return datos_audio, samplerate, nombre_archivo

            except Exception as e:
                QMessageBox.critical(None, "Error al Cargar Audio",
                                     f"No se pudo leer el archivo WAV:\n{e}")

        return None, None, None