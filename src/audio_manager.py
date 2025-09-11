import numpy as np
import sounddevice as sd

class AudioManager:
    def __init__(self):
        self.stream = None
        self.duracion : float = 30.0 # 30s
        self.samplerate : int = 44100 # Tasa de muestreo en Hz, estándar

    def generar_datos_onda(self, frecuencia: str, amplitud: int, funcion: str):

        frecuencia_int = int(frecuencia)
        t = np.linspace(0, self.duracion, int(self.duracion * self.samplerate), endpoint=False)

        if funcion == "Seno":
            onda = amplitud * np.sin(2 * np.pi * frecuencia_int * t)
        else:
            onda = amplitud * np.cos(2 * np.pi * frecuencia_int * t)

        return onda

    def reproducir_onda(self, onda):
            sd.play(onda, self.samplerate, blocking=False)

    def detener_onda(self):
        sd.stop()
