import numpy as np
import matplotlib.pyplot as plt

class AudioManager:
    def __init__(self):
        
        pass

    def reproducir_tono(self, frecuencia: int, amplitud: int, funcion: str):
        # todo lógica para genera y reproducir onda

        print(f"Datos: \n"
              f"Fr: {frecuencia} \n"
              f"Am: {amplitud} \n"
              f"Fun: {funcion}")

        if funcion == "Seno":
            x = np.linspace(-np.pi, np.pi, 10)
            print(f"Onda: {np.sin(x)}")
        else:
            onda = np.cos()
            print(f"Onda: {onda}")

    def detener_tono(self):
        # todo logica para detener tono
        pass
