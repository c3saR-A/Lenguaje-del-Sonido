from pydub import AudioSegment
from PySide6.QtWidgets import QFileDialog, QMessageBox

class SaveAudioHandler:
    def __init__(self, parent=None):
        self.parent = parent

    def guardar_audio(self, audio_segment):
        # Definimos los filtros
        filtros = "MP3 (*.mp3);;WAV (*.wav);;FLAC (*.flac)"

        # Abrimos diálogo con filtros separados
        filename, selected_filter = QFileDialog.getSaveFileName(
            self.parent,
            "Guardar audio",
            "",
            filtros
        )

        if not filename:
            return

        # Detectar el formato según el filtro elegido
        if "mp3" in selected_filter.lower():
            formato = "mp3"
            if not filename.lower().endswith(".mp3"):
                filename += ".mp3"
        elif "wav" in selected_filter.lower():
            formato = "wav"
            if not filename.lower().endswith(".wav"):
                filename += ".wav"
        elif "flac" in selected_filter.lower():
            formato = "flac"
            if not filename.lower().endswith(".flac"):
                filename += ".flac"
        else:
            # Por defecto mp3
            formato = "mp3"
            if not filename.lower().endswith(".mp3"):
                filename += ".mp3"

        try:
            # Exportar en el formato elegido
            audio_segment.export(filename, format=formato)
            QMessageBox.information(self.parent, "Éxito", f"Audio guardado en:\n{filename}")
        except Exception as e:
            QMessageBox.critical(self.parent, "Error al guardar audio", str(e))
