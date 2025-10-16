from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
import numpy as np

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100, animation_on = True):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        super().__init__(fig)
        self.setParent(parent)

        self.linea = None
        self.animacion = None
        self.onda_info = None
        self.offset = 0
        self.animation_on = animation_on

        self.axes.set_axis_off()
        self.samplerate: int = 44100
        self.axes.set_ylim(-1.1, 1.1)  # Rango de amplitud normalizado

    def detener_animacion(self):
        if self.animacion:
            self.animacion.event_source.stop()
            self.animacion = None
        
    def iniciar_animacion(self, onda, frecuencia: int):

        if not self.animation_on:
            return

        self.detener_animacion()
        puntos_por_ciclo = self.samplerate / frecuencia
        num_ciclos = 8
        puntos_mostrar = int(puntos_por_ciclo * num_ciclos)

        if puntos_mostrar < 50:
            puntos_mostrar = 50

        self.axes.cla()
        self.onda_info = onda
        self.offset = 0
        self.axes.set_axis_off()
        self.axes.set_ylim(np.min(onda) * 1.1, np.max(onda) * 1.1)
        self.axes.set_xlim(0, puntos_mostrar)

        # Creación de linea
        self.linea, = self.axes.plot(self.onda_info[:puntos_mostrar])
        
        # Crear y guardar el objeto de animacion
        self.animacion = animation.FuncAnimation(
            self.figure,
            self.actualizar_linea,
            interval=15,
            blit=False,
            cache_frame_data=False
        )
        self.draw()
        
    def actualizar_linea(self, i):

        self.offset = (self.offset + 10) % len(self.onda_info)
        segmento = np.roll(self.onda_info, -self.offset)
        self.linea.set_ydata(segmento[:self.linea.get_xdata().size])

        return self.linea,

    def plot_data(self, datos_audio):

        self.detener_animacion()
        self.axes.cla()

        puntos_mostrar = len(datos_audio)
        datos_a_graficar = datos_audio

        amplitud_abs_max = np.max(np.abs(datos_a_graficar))

        y_lim = max(0.1, amplitud_abs_max * 1.1)

        y_min_final = -y_lim
        y_max_final = y_lim

        self.axes.set_ylim(y_min_final, y_max_final)
        self.axes.set_xlim(0, puntos_mostrar)

        # Configuración de los ejes (Mostramos información del eje X para referencia)
        self.axes.set_axis_off()
        self.axes.set_title("Forma de Onda de Audio")

        self.axes.plot(datos_a_graficar)
        self.draw()

    def plot_fft(self, frecuencias, amplitudes):
        """Grafica el espectro de frecuencia (FFT) con ejes personalizados."""
        self.detener_animacion()
        self.axes.cla()

        # self.axes.set_title(self.titulo_inicial if self.titulo_inicial else "Espectro de Frecuencia (FFT)",
        #                     color='#1f2937')

        # Activar ejes para mostrar Frecuencia (Hz)
        self.axes.set_axis_on()
        self.axes.set_xlabel("Frecuencia (Hz)", color='#4b5563')
        self.axes.set_ylabel("Amplitud Normalizada", color='#4b5563')
        self.axes.grid(True, linestyle='--', alpha=0.6)

        # Límites de la gráfica de FFT (hasta 20000 Hz es suficiente para el oído humano)
        self.axes.set_xlim(0, np.max(frecuencias))


        # Graficar la FFT
        self.axes.plot(frecuencias, amplitudes, color='#34a853', linewidth=1.5)
        self.draw()

    # def plot_data_ftt(self, datos_audio):
    #
    #     self.detener_animacion()
    #     self.axes.cla()
    #
    #     puntos_mostrar = len(datos_audio)
    #     datos_a_graficar = datos_audio
    #
    #     amplitud_abs_max = np.max(np.abs(datos_a_graficar))
    #
    #     y_lim = max(0.1, amplitud_abs_max * 1.1)
    #
    #     y_min_final = -y_lim
    #     y_max_final = y_lim
    #
    #     self.axes.set_ylim(y_min_final, y_max_final)
    #     self.axes.set_xlim(0, puntos_mostrar)
    #
    #     # Configuración de los ejes (Mostramos información del eje X para referencia)
    #     self.axes.set_axis_off()
    #     self.axes.set_title("Forma de Onda de Audio")
    #
    #     self.axes.plot(datos_a_graficar)
    #     self.draw()