from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
import numpy as np

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)
        self.linea = None
        self.animacion = None
        self.onda_info = None
        self.offset = 0
        
    def iniciar_animacion(self, onda):
        self.axes.cla()
        self.onda_info = onda
        self.offset = 0
        puntos_mostrar = 500
        self.axes.set_ylim(-100, 100)
        self.axes.set_xlim(0, puntos_mostrar)

        # oculta los números o valores
        self.axes.set_xticklabels([])
        self.axes.set_yticklabels([])

        # Ocultar los ticks de los ejes
        self.axes.tick_params(axis='x', which='both', bottom=False, top=False)
        self.axes.tick_params(axis='y', which='both', left=False, right=False)

        # Ocultar el recuadro de la gráfica
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)
        self.axes.spines['left'].set_visible(False)

        self.linea, = self.axes.plot(self.onda_info[:puntos_mostrar])
        
        # Crear y guardar el objeto de animacion
        self.animacion = animation.FuncAnimation(
            self.figure,
            self.actualizar_linea,
            frames=np.arange(len(onda)),
            interval=1,
            blit=True,
        )
        self.draw()
        
    def actualizar_linea(self, i):
        self.offset = (self.offset + 10) % len(self.onda_info)
        segmento = np.roll(self.onda_info, -self.offset)
        self.linea.set_ydata(segmento[:self.linea.get_xdata().size])
        return self.linea,