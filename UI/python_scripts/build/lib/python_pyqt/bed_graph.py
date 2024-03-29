# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_ui/bed_graph.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GraphWindow(object):
    def setupUi(self, GraphWindow):
        GraphWindow.setObjectName("GraphWindow")
        GraphWindow.resize(960, 772)
        GraphWindow.setStyleSheet("background-color: rgb(1,0,1);")
        self.centralwidget = QtWidgets.QWidget(GraphWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.GraphWidget = PlotWidget(self.centralwidget)
        self.GraphWidget.setObjectName("GraphWidget")
        self.gridLayout.addWidget(self.GraphWidget, 0, 0, 1, 7)
        spacerItem = QtWidgets.QSpacerItem(154, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.HeartGraph = QtWidgets.QPushButton(self.centralwidget)
        self.HeartGraph.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.HeartGraph.setObjectName("HeartGraph")
        self.gridLayout.addWidget(self.HeartGraph, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(154, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.StepsGraph = QtWidgets.QPushButton(self.centralwidget)
        self.StepsGraph.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.StepsGraph.setObjectName("StepsGraph")
        self.gridLayout.addWidget(self.StepsGraph, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(154, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        self.ActivityGraph = QtWidgets.QPushButton(self.centralwidget)
        self.ActivityGraph.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.ActivityGraph.setObjectName("ActivityGraph")
        self.gridLayout.addWidget(self.ActivityGraph, 1, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(154, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 6, 1, 1)
        GraphWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GraphWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 23))
        self.menubar.setObjectName("menubar")
        GraphWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GraphWindow)
        self.statusbar.setObjectName("statusbar")
        GraphWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GraphWindow)
        QtCore.QMetaObject.connectSlotsByName(GraphWindow)

    def retranslateUi(self, GraphWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphWindow.setWindowTitle(_translate("GraphWindow", "MainWindow"))
        self.HeartGraph.setText(_translate("GraphWindow", "Heart Rate vs Time"))
        self.StepsGraph.setText(_translate("GraphWindow", "Steps vs Time"))
        self.ActivityGraph.setText(_translate("GraphWindow", "Activity vs Time"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GraphWindow = QtWidgets.QMainWindow()
    ui = Ui_GraphWindow()
    ui.setupUi(GraphWindow)
    GraphWindow.show()
    sys.exit(app.exec_())
