import numpy as np
import sounddevice as sd

class AudioManager:
    def __init__(self):
        self.duracion: float = 15.0     # 15s
        self.samplerate: int = 44100    # Tasa de muestreo en Hz, estándar

    def generar_datos_onda(self, frecuencia: str, amplitud: int, funcion: str):
        
        try:
            frecuencia_num = float(frecuencia)
        except ValueError:
            print('Frecuencia invalida')
            return None
        
        tiempo = np.linspace(0, self.duracion, int(self.duracion * self.samplerate), endpoint=False)

        if funcion == "Seno":
            onda = amplitud * np.sin(2 * np.pi * frecuencia_num * tiempo)
        else:
            onda = amplitud * np.cos(2 * np.pi * frecuencia_num * tiempo)

        return onda

    def reproducir_onda(self, onda):
            sd.play(onda, self.samplerate, blocking=False)

    def detener_onda(self):
        sd.stop()
