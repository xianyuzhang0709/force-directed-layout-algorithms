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
        self.canvas = PlotCanvas(parent=self.PivotGraphic)

        self.closeBtn.clicked.connect(self.close)
        self.PivotBtn.clicked.connect(self.pivot_plot)

    def pivot_plot(self):
        self.canvas.pivot_layout()


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

    def pivot_layout(self):
        self.fig.clear()
        dataset = load_poker(500)
        fl.draw_spring_layout_animated(dataset, algorithm=fl.Pivot, distance=poker_distance)
        # 没有这个，画布上不会画这个，图会在plt弹窗里显示
        self.draw()

    def clear(self):
        self.fig.clear()
        self.draw()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # center = QtWidgets.QDesktopWidget().availableGeometry().center()
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
