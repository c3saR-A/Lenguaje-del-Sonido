import soundfile as sf
import numpy as np
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtCore import QObject

class SaveAudioHandler:
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def guardar_audio(self, audio_segment):

        datos_audio = self.main_window.datos_audio_cargado
        samplerate = self.main_window.samplerate_cargado

        if datos_audio is None or samplerate is None:
            QMessageBox.warning(self.main_window, "Sin Audio",
                                "No hay datos de audio para guardar. Cargue, genere o grabe primero.")
            return

        filepath, _ = QFileDialog.getSaveFileName(
            self.main_window,
            "Guardar archivo de audio",
            "",
            "Archivos WAV (*.wav);;Todos los archivos (*.*)",
            "",
        )

        if filepath:
            try:
                # Asegurar la extensión .wav
                if not filepath.lower().endswith('.wav'):
                    filepath += '.wav'

                # soundfile requiere datos en formato float (de -1.0 a 1.0)
                datos_a_guardar = datos_audio.astype(np.float32)

                # Guardar usando soundfile
                sf.write(filepath, datos_a_guardar, samplerate)

                QMessageBox.information(self.main_window, "Guardado Exitoso",
                                        f"Audio guardado correctamente en:\n{filepath}")
            except Exception as e:
                QMessageBox.critical(self.main_window, "Error de Guardado",
                                     f"No se pudo guardar el archivo:\n{e}")
