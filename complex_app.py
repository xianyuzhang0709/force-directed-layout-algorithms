import sys
import matplotlib
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

matplotlib.use("Qt5Agg")

from examples.poker_utils import load_poker, poker_distance
from complex import Ui_MainWindow
import forcelayout as fl


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fl = fl
        self.fig = self.fl.draw.plt.figure(figsize=(width, height), dpi=dpi, tight_layout=True)

        FigureCanvas.__init__(self, figure=self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(
            self,
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        FigureCanvas.updateGeometry(self)
        self.draw()

    def plot(self, dataset, algorithm, distance):
        self.fig.clear()
        self.fl.draw_spring_layout_animated(
            dataset=dataset, algorithm=algorithm, distance=distance, size=2, alpha=0.4
        )
        self.draw()

    def clear(self):
        self.fig.clear()
        self.draw()


class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.frame_chalmer_layout = QtWidgets.QGridLayout(self.frame_chalmer)
        self.canvas_chalmer = PlotCanvas(self.frame_chalmer)
        self.frame_chalmer_layout.addWidget(self.canvas_chalmer, 0, 0, 1, 1)

        self.frame_hybird_layout = QtWidgets.QGridLayout(self.frame_hybird)
        self.canvas_hybird = PlotCanvas(self.frame_hybird)
        self.frame_hybird_layout.addWidget(self.canvas_hybird, 0, 0, 1, 1)

        self.frame_pivot_layout = QtWidgets.QGridLayout(self.frame_pivot)
        self.canvas_pivot = PlotCanvas(self.frame_pivot)
        self.frame_pivot_layout.addWidget(self.canvas_pivot, 0, 0, 1, 1)

        self.btn_chalmer.clicked.connect(self.plot_chalmer)
        self.btn_hybird.clicked.connect(self.plot_hybird)
        self.btn_pivot.clicked.connect(self.plot_pivot)

    def plot_chalmer(self):
        print("chalmer")
        dataset = load_poker(200)
        self.canvas_chalmer.plot(
            dataset=dataset,
            algorithm=fl.NeighbourSampling,
            distance=poker_distance)

    def plot_hybird(self):
        print("hybird")
        dataset = load_poker(500)
        self.canvas_hybird.plot(
            dataset=dataset,
            algorithm=fl.Hybrid,
            distance=poker_distance)

    def plot_pivot(self):
        print("pivot")
        dataset = load_poker(1000)
        self.canvas_pivot.plot(
            dataset=dataset,
            algorithm=fl.Pivot,
            distance=poker_distance)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    center = QtWidgets.QDesktopWidget().availableGeometry().center()
    m = MainApp()
    m.show()
    sys.exit(app.exec_())


