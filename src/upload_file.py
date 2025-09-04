import soundfile as sf
from PySide6.QtWidgets import QFileDialog
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
            filter="Archivo de audio (*.wav *.mp3 *.ogg);;Todos los archivos"
        )

        if archivo_path:
            try:
                datos_audio, samplerate = sf.read(archivo_path)
                return datos_audio, samplerate
            except Exception as e:
                print(f"Error al cargar archivo: {e}")
        return None, None