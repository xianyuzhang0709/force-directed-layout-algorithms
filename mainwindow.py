
from PyQt5 import QtWidgets, QtGui, QtCore



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 40, 761, 411))
        self.graphicsView.setObjectName("graphicsView")
        self.btnTest1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnTest1.setGeometry(QtCore.QRect(110, 480, 113, 32))
        self.btnTest1.setObjectName("btnTest1")
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setGeometry(QtCore.QRect(600, 480, 113, 32))
        self.btnClose.setObjectName("btnClose")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuForce_d = QtWidgets.QMenu(self.menubar)
        self.menuForce_d.setObjectName("menuForce_d")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_FIle = QtWidgets.QAction(MainWindow)
        self.action_FIle.setObjectName("action_FIle")
        self.action_hybird = QtWidgets.QAction(MainWindow)
        self.action_hybird.setObjectName("action_hybird")
        self.actionPivot = QtWidgets.QAction(MainWindow)
        self.actionPivot.setObjectName("actionPivot")
        self.menuForce_d.addAction(self.action_FIle)
        self.menuForce_d.addAction(self.action_hybird)
        self.menuForce_d.addAction(self.actionPivot)
        self.menubar.addAction(self.menuForce_d.menuAction())
        self.toolBar.addAction(self.action_FIle)
        self.toolBar.addAction(self.action_hybird)
        self.toolBar.addAction(self.actionPivot)

        self.retranslateUi(MainWindow)
        self.btnClose.clicked.connect(MainWindow.close)
        self.btnTest1.clicked.connect(self.plot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnTest1.setText(_translate("MainWindow", "test 1"))
        self.btnClose.setText(_translate("MainWindow", "Close"))
        self.menuForce_d.setTitle(_translate("MainWindow", "Force-d"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_FIle.setText(_translate("MainWindow", "&1996"))
        self.action_hybird.setText(_translate("MainWindow", "&hybird"))
        self.actionPivot.setText(_translate("MainWindow", "&Pivot"))

    def plot(self):
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        pen = QtGui.QPen(QtCore.Qt.green)

        side = 20

        for i in range(16):
            for j in range(16):
                r = QtCore.QRectF(QtCore.QPointF(i * side, j * side), QtCore.QSizeF(side, side))
                scene.addRect(r, pen)



