
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QMainWindow
from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

import random
from examples.poker_utils import load_poker, annotate_poker, poker_distance
import matplotlib.pyplot as plt
import forcelayout as fl


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        # self.figure = plt.figure()

        # self.figure = Figure(figsize=(5, 5), dpi=100)

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__

        # self.canvas = FigureCanvas(self.figure)
        # self.myFig = Figure_Canvas()
        # self.addWidget(self.myFig, *(0, 1))
        self.LAYOUT_A = QtWidgets.QGridLayout()
        self.canvas = Figure_Canvas()
        # self.LAYOUT_A.addWidget(self.canvas, *(0, 1))
        self.LAYOUT_A.addWidget(self.canvas)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)
        #

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.show()

    def plot(self):
        ''' plot some random stuff '''

        # dataset = load_poker(500)
        # self.canvas.ani = fl.draw_spring_layout_animated(dataset, algorithm=fl.Pivot, distance=poker_distance)

        # self.figure.clear()
        #
        # self.canvas.draw()
        self.draw()

class Figure_Canvas(FigureCanvas, FuncAnimation):

    def __init__(self):
        # fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        self.fig = Figure(figsize=(5, 5), dpi=100)
        # FigureCanvas.__init__(self, self.fig)  # 初始化父类
        # self.setParent(parent)
        # self.axes = fig.add_subplot(111)  # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        # self.canvas = FigureCanvas(self.figure)
        FigureCanvas.__init__(self, self.fig)
        # dataset = load_poker(500)
        FuncAnimation.__init__(self, self.fig, func=None)
        # Animation(fl.draw_spring_layout_animated(dataset, algorithm=fl.Pivot, distance=poker_distance))

    def test(self):
        # dataset = load_poker(500)
        # self.canvas.ani = fl.draw_spring_layout_animated(dataset, algorithm=fl.Pivot, distance=poker_distance)
        # self.draw()
        dataset = load_poker(500)
        FuncAnimation = fl.draw_spring_layout_animated(dataset, algorithm=fl.Pivot, distance=poker_distance)
        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()

    sys.exit(app.exec_())