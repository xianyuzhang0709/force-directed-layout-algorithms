import sys
import matplotlib
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

matplotlib.use("Qt5Agg")

import forcelayout as fl
from examples.poker_utils import load_poker, poker_distance
from mainwindow import Ui_MainWindow


class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.label_placeholder.hide()  # 使用 qt 设计师将布局做好，隐藏占位的标签元素

        # 新建我们的绘图组件
        self.canvas_neighbourSampling = PlotCanvas(parent=self.ChalmerGraphic)
        self.canvas_hybird = PlotCanvas(parent=self.HybirdGraphic)
        self.canvas_pivot = PlotCanvas(parent=self.PivotGraphic)

        self.closeBtn.clicked.connect(self.close)
        self.ChalmerBtn.clicked.connect(self.neighbourSampling_layout)
        self.HybirdBtn.clicked.connect(self.hybird_layout)
        self.PivotBtn.clicked.connect(self.pivot_plot)

    def neighbourSampling_layout(self):
        self.canvas_neighbourSampling.neighbourSampling_layout()

    def hybird_layout(self):
        self.canvas_hybird.hybird_layout()

    def pivot_plot(self):
        self.canvas_pivot.pivot_layout()

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = plt.figure(figsize=(width, height), dpi=dpi, tight_layout=True)

        FigureCanvas.__init__(self, figure=self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(
            self,
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        FigureCanvas.updateGeometry(self)
        self.draw()

    def neighbourSampling_layout(self):
        self.fig.clear()
        dataset = load_poker(500)
        fl.draw_spring_layout_animated(dataset, algorithm=fl.NeighbourSampling, distance=poker_distance)
        self.draw()

    def hybird_layout(self):
        self.fig.clear()
        dataset = load_poker(500)
        fl.draw_spring_layout_animated(dataset, algorithm=fl.Hybrid, distance=poker_distance)
        self.draw()

    # def pivot_layout(self):
    #     self.fig.clear()
    #     dataset = load_poker(500)
    #     fl.draw_spring_layout_animated(dataset, algorithm=fl.Pivot, distance=poker_distance)
    #     self.draw()

    def pivot_layout(self):
        self.fig.clear()
        dataset = load_poker(500)
        layout = fl.draw_spring_layout(dataset, algorithm=fl.Pivot, distance=poker_distance,
                                       color_by=lambda datapoint: datapoint[10])
        draw = fl.DrawLayout(dataset, layout)
        draw.draw(color_by=lambda datapoint: datapoint[10], color_map='hsv')
        self.draw()

    def clear(self):
        self.fig.clear()
        self.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
