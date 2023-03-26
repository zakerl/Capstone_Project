# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_ui/bed_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1385, 1154)
        MainWindow.setStyleSheet("background-color: rgb(1,0,1);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(1114, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 8)
        self.toggleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.toggleBtn.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"border-radius: 15px;")
        self.toggleBtn.setObjectName("toggleBtn")
        self.gridLayout.addWidget(self.toggleBtn, 0, 8, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(17, 112, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 8, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(358, 28, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(331, 281))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pyqt_ui\\../python_scripts/python_pyqt/BED_logo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 6)
        spacerItem3 = QtWidgets.QSpacerItem(358, 28, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 7, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 3, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(427, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 4, 0, 1, 2)
        self.ReadSD = QtWidgets.QPushButton(self.centralwidget)
        self.ReadSD.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;\n"
"")
        self.ReadSD.setObjectName("ReadSD")
        self.gridLayout.addWidget(self.ReadSD, 4, 2, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(473, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 4, 7, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(494, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 5, 0, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 5, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(494, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 5, 7, 1, 2)
        self.ConfigButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConfigButton.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;\n"
"")
        self.ConfigButton.setObjectName("ConfigButton")
        self.gridLayout.addWidget(self.ConfigButton, 6, 2, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem10, 6, 4, 2, 1)
        spacerItem11 = QtWidgets.QSpacerItem(494, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 7, 0, 2, 2)
        spacerItem12 = QtWidgets.QSpacerItem(494, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 7, 7, 2, 2)
        self.CreateRecordsButton = QtWidgets.QPushButton(self.centralwidget)
        self.CreateRecordsButton.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;\n"
"")
        self.CreateRecordsButton.setObjectName("CreateRecordsButton")
        self.gridLayout.addWidget(self.CreateRecordsButton, 8, 2, 1, 3)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem13, 9, 4, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(494, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 9, 6, 1, 3)
        self.RecordsButton = QtWidgets.QPushButton(self.centralwidget)
        self.RecordsButton.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;\n"
"")
        self.RecordsButton.setObjectName("RecordsButton")
        self.gridLayout.addWidget(self.RecordsButton, 10, 2, 1, 2)
        spacerItem15 = QtWidgets.QSpacerItem(494, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 11, 0, 1, 2)
        spacerItem16 = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem16, 11, 5, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(427, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 12, 0, 1, 2)
        self.DataViewButton = QtWidgets.QPushButton(self.centralwidget)
        self.DataViewButton.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;\n"
"")
        self.DataViewButton.setObjectName("DataViewButton")
        self.gridLayout.addWidget(self.DataViewButton, 12, 2, 1, 2)
        spacerItem18 = QtWidgets.QSpacerItem(473, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem18, 12, 7, 1, 2)
        spacerItem19 = QtWidgets.QSpacerItem(20, 342, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem19, 13, 3, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1385, 23))
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
        self.toggleBtn.setText(_translate("MainWindow", "Disconnected to device"))
        self.ReadSD.setText(_translate("MainWindow", "Connect to device"))
        self.ConfigButton.setText(_translate("MainWindow", "Configuration"))
        self.CreateRecordsButton.setText(_translate("MainWindow", "Create Records"))
        self.RecordsButton.setText(_translate("MainWindow", "Records"))
        self.DataViewButton.setText(_translate("MainWindow", "DataView"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
