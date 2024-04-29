"""
УВАГА!!! ЖРЕ ДОХУЯ ПАМЯТІ

WARNING!!! USES A LOT OF MEMORY


"""

from tkinter import Frame, Tk, TOP, BOTH
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PlotWidget(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    def plot(self, x_data, y_data, **kwargs):
        self.ax.plot(x_data, y_data, **kwargs)
        self.canvas.draw()

# Приклад використання:
if __name__ == "__main__":
    root = Tk()
    root.title("Графік")

    plot_widget = PlotWidget(root)
    plot_widget.pack(side=TOP, fill=BOTH, expand=True)

    x_data = [1, 2, 10, 4, 5]
    y_data = [2, 3, 5, 7, 11]
    plot_widget.plot(x_data, y_data, marker='o', linestyle='-', color='b')

    root.mainloop()
