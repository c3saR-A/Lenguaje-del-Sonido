import numpy as np
import sounddevice as sd

class AudioManager:
    def __init__(self):
        self.duracion: float = 15.0     # 15s
        self.samplerate: int = 44100    # Tasa de muestreo en Hz, estándar

    def generar_datos_onda(self, frecuencia: int, amplitud: int, funcion: str):
         
        tiempo = np.linspace(0, self.duracion, int(self.duracion * self.samplerate), endpoint=False)
        if funcion == "Seno":
            onda = amplitud * np.sin(2 * np.pi * frecuencia * tiempo)
        else:
            onda = amplitud * np.cos(2 * np.pi * frecuencia * tiempo)

        return onda.astype(np.float32), self.samplerate

    def reproducir_onda(self, onda):
        self.detener_sonido()
        sd.play(onda, self.samplerate, blocking=False)

    def reproducir_archivo_cargado(self, datos_audio: np.ndarray, samplerate: int):
        self.detener_sonido()
        sd.play(datos_audio, samplerate, blocking=False)

    @staticmethod
    def detener_sonido():
        sd.stop()

    def sintetizar_onda(self, frecuencia: int, amplitud: float, duracion_muestras: int):

        samplerate = self.samplerate

        tiempo = np.linspace(0, duracion_muestras / samplerate, duracion_muestras, endpoint=False)

        onda = amplitud * np.sin(2 * np.pi * frecuencia * tiempo)

        return onda.astype(np.float32)
