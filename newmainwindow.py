from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib

matplotlib.use("Qt5Agg") 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

from examples.poker_utils import load_poker, annotate_poker, poker_distance
import matplotlib.pyplot as plt
import forcelayout as fl


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 605)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.closeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeBtn.setObjectName("closeBtn")
        self.gridLayout.addWidget(self.closeBtn, 1, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 6)
        self.testBtn = QtWidgets.QPushButton(self.centralwidget)
        self.testBtn.setObjectName("testBtn")
        self.gridLayout.addWidget(self.testBtn, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.closeBtn.clicked.connect(MainWindow.close)
        self.testBtn.clicked.connect(self.plot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.closeBtn.setText(_translate("MainWindow", "Close"))
        self.testBtn.setText(_translate("MainWindow", "Test1"))

    def plot(self):
        draw = Figure_Canvas()

        draw.test()  # 画图
        graphicscene = QtWidgets.QGraphicsScene()

        graphicscene.addWidget(draw)

        self.graphicsView.setScene(graphicscene)
        self.graphicsView.show()

class Figure_Canvas(FigureCanvas, FuncAnimation):

    def __init__(self):
        # self.setParent(parent)
        self.fig = Figure(figsize=(7, 5), dpi=100)
        FigureCanvas.__init__(self, self.fig)
        dataset = load_poker(500)
        FuncAnimation.__init__ = fl.draw_spring_layout_animated(dataset, algorithm=fl.Pivot, distance=poker_distance)
        # self.draw()

    def test(self):

        self.draw()
        print("111")

        plt.show() #问题就是非要有这一步才可以显示动画，但是我需要把这个嵌入到mainwindow里去。

        # self.canvas.draw()
        print(type(self))


