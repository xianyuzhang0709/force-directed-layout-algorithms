# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(433, 823)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.PivotGraphic = QtWidgets.QGraphicsView(self.centralwidget)
        self.PivotGraphic.setObjectName("PivotGraphic")
        self.gridLayout.addWidget(self.PivotGraphic, 3, 0, 1, 1)
        self.closeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeBtn.setObjectName("closeBtn")
        self.gridLayout.addWidget(self.closeBtn, 5, 2, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 5, 1, 1, 1)
        self.HybirdGraphic = QtWidgets.QGraphicsView(self.centralwidget)
        self.HybirdGraphic.setObjectName("HybirdGraphic")
        self.gridLayout.addWidget(self.HybirdGraphic, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.ChalmerBtn = QtWidgets.QPushButton(self.widget)
        self.ChalmerBtn.setGeometry(QtCore.QRect(0, 10, 83, 32))
        self.ChalmerBtn.setObjectName("ChalmerBtn")
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 3)
        self.ChalmerGraphic = QtWidgets.QGraphicsView(self.centralwidget)
        self.ChalmerGraphic.setObjectName("ChalmerGraphic")
        self.gridLayout.addWidget(self.ChalmerGraphic, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.HybirdBtn = QtWidgets.QPushButton(self.widget_2)
        self.HybirdBtn.setGeometry(QtCore.QRect(0, 10, 113, 32))
        self.HybirdBtn.setObjectName("HybirdBtn")
        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 3)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.PivotBtn = QtWidgets.QPushButton(self.widget_3)
        self.PivotBtn.setGeometry(QtCore.QRect(0, 10, 101, 31))
        self.PivotBtn.setObjectName("PivotBtn")
        self.gridLayout.addWidget(self.widget_3, 3, 1, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 433, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.closeBtn.setText(_translate("MainWindow", "Close"))
        self.pushButton_3.setText(_translate("MainWindow", "Stop"))
        self.ChalmerBtn.setText(_translate("MainWindow", "1996"))
        self.HybirdBtn.setText(_translate("MainWindow", "Hybird"))
        self.PivotBtn.setText(_translate("MainWindow", "Pivot"))
