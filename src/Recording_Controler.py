import sounddevice as sd
import numpy as np
import threading
import queue

from PySide6.QtCore import QThread, Signal

class GrabacionThread(QThread):
    # Señal emitida al finalizar la grabación, lleva los datos de audio consolidados
    grabacion_finalizada = Signal(object)

    def __init__(self, samplerate: int, parent=None):
        super().__init__()
        self.muestreo = samplerate
        self.canales = 1    # Grabación mono
        self.chunk = 1024   # Buffer para lectura de audio
        self.q = queue.Queue()
        self._is_recording = False
        self._stop_requested = False
        self.audio_chunks = []

    def run(self):
        # Método principal del hilo que maneja la grabación de audio.
        
        self.audio_chunks = []
        self._stop_requested = False
        self._is_recording = True
        try:
            # Crea un bloque de contexto para manejar el flujo de entrada de audio
            with sd.InputStream(
                    samplerate=self.muestreo,
                    channels=self.canales,
                    dtype='int16',
                    blocksize=self.chunk,
            ) as stream:
                
                print("Grabación iniciada...")
                
                while not self._stop_requested:
                    # Espera a recibir un bloque de audio
                    data, overflowed = stream.read(self.chunk)
                    
                    if overflowed:
                        print("Advertencia: Se produjo un desbordamiento del buffer de entrada de audio.")
                    
                    # Añade el fragmento (chunk) a la lista
                    self.audio_chunks.append(data.copy())
                    
                print("Grabación finalizada. Procesando los datos...")
            
            # Unir fragmentos grabados
            if self.audio_chunks:
                audio_data_int16 = np.concatenate(self.audio_chunks, axis=0)
                
                # Convertir datos int16 (032768 a 32767) a float64 normalizado (-1.0 a 1.0) permite guardado y análisis correcto.
                max_int16 = 32768.0
                audio_data_float = audio_data_int16.astype(np.float64) / max_int16
                
                datos_finales = audio_data_float.squeeze()  # Quitar el eje de canales si es mono (1,)
            else:
                datos_finales = np.array([])
        
        except Exception as e:
            print(f"ERROR DE GRABACIÓN: {e}")
            datos_finales = np.array([])
        finally:
            self._is_recording = False
            # Emitir la señal con los datos finales
            self.grabacion_finalizada.emit(datos_finales)

    def detener_grabacion(self):
        self._stop_requested = True
    
    def isRunning(self):
        return self._is_recording
        