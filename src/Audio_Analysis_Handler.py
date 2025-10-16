import numpy as np
from scipy.signal import find_peaks

class AnalisisHandler:
    def __init__(self, main_window):
        self.main_window = main_window

    def realizar_tranformada_rapida(self, datos_audio: np.ndarray, samplerate: int):
        # Args: datos_audio (np.ndarray): Array de datos de audio, samplerate (int): Tasa de muestreo
        # Returns: tuple: (frecuencias, amplitudes)

        if datos_audio is None or samplerate is None:
            return None, None

        datos_transformada_rapida = np.fft.fft(datos_audio)
        amplitudes = np.abs(datos_transformada_rapida)
        frecuencias = np.fft.fftfreq(len(datos_audio), 1/samplerate)

        num_muestras = len(datos_audio)
        mitad_positiva = num_muestras // 2

        frecuencias_positivas = frecuencias[:mitad_positiva]
        amplitudes_positivas = amplitudes[:mitad_positiva]

        amplitudes_max = np.max(amplitudes_positivas)
        if amplitudes_max == 0:
            amplitudes_normalizadas = amplitudes_positivas
        else:
            amplitudes_normalizadas = amplitudes_positivas / amplitudes_max

        return frecuencias_positivas, amplitudes_normalizadas

    def encontrar_tonos_principales(self, frecuencias: np.ndarray, amplitudes: np.ndarray, umbral_minimo: float = 0.01):
        # Args: umbral_minimo (float): Amplitud mínima para considerarse un tono principal.
        # Returns: list: Lista de tuplas (frecuencia, amplitud) para los tonos principales.

        tonos = []

        if len(frecuencias) > 1:
            delta_frecuencia = frecuencias[1] - frecuencias[0]
        else:
            delta_frecuencia = 1

        distancia_minima = 5

        if delta_frecuencia > 0:
            indice_distancia_pico_minimo = int(distancia_minima / delta_frecuencia)
            indice_distancia_pico_minimo = max(1, indice_distancia_pico_minimo)
        else:
            indice_distancia_pico_minimo = 1

        pico_minimo = umbral_minimo

        indices_picos, _ = find_peaks(amplitudes, height=pico_minimo, distance=indice_distancia_pico_minimo)

        frecuencia_minima = 20

        for i in indices_picos:
            frecuencia = frecuencias[i]
            amplitud = amplitudes[i]

            if frecuencia >= frecuencia_minima:
                tonos.append((int(frecuencia), round(amplitud, 3)))

        tonos.sort(key=lambda x: x[1], reverse=True)

        return tonos[:25]
