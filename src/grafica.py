
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
        self.axes.set_ylim(-1.1, 1.1)  # Rango de amplitud normalizado

    def detener_animacion(self):
        if self.animacion:
            self.animacion.event_source.stop()
            self.animacion = None
        
    def iniciar_animacion(self, onda):

        if not self.animation_on:
            return

        self.detener_animacion()

        self.axes.cla()
        self.onda_info = onda
        self.offset = 0
        puntos_mostrar = 1000

        # # Reconfigurar ejes
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

    def plot_data(self, datos):

        self.detener_animacion()
        self.axes.cla()

        puntos_a_mostrar = min(5000, len(datos))
        datos_recortados = datos[:puntos_a_mostrar]

        x_data = np.arange(puntos_a_mostrar)

        self.axes.plot(x_data, datos_recortados, color='#1f77b4', linewidth=1.5)

        # Configuración de los ejes (Mostramos información del eje X para referencia)
        self.axes.set_axis_on()
        self.axes.set_title("Forma de Onda de Audio Cargado (Primeros 5k Muestras)")
        self.axes.set_xlabel("Muestras")
        self.axes.set_ylabel("Amplitud")
        self.axes.grid(True, linestyle='--', alpha=0.6)

        self.draw()