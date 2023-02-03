# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bed_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 907)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(409, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 11, 3, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(433, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(952, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 5)
        self.ConnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(61, 217, 245, 255), stop:1 rgba(240, 53, 218, 255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.ConnectButton.setObjectName("ConnectButton")
        self.gridLayout.addWidget(self.ConnectButton, 2, 2, 1, 1)
        self.DataViewButton = QtWidgets.QPushButton(self.centralwidget)
        self.DataViewButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(61, 217, 245, 255), stop:1 rgba(240, 53, 218, 255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.DataViewButton.setObjectName("DataViewButton")
        self.gridLayout.addWidget(self.DataViewButton, 10, 2, 2, 1)
        spacerItem3 = QtWidgets.QSpacerItem(409, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 3, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(409, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 3, 1, 2)
        self.ReadSDCard_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ReadSDCard_btn.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(61, 217, 245, 255), stop:1 rgba(240, 53, 218, 255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.ReadSDCard_btn.setObjectName("ReadSDCard_btn")
        self.gridLayout.addWidget(self.ReadSDCard_btn, 3, 2, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(13, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 0, 2, 1)
        spacerItem6 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 9, 0, 2, 1)
        spacerItem7 = QtWidgets.QSpacerItem(13, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 0, 1, 1)
        self.ConfigButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConfigButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(61, 217, 245, 255), stop:1 rgba(240, 53, 218, 255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.ConfigButton.setObjectName("ConfigButton")
        self.gridLayout.addWidget(self.ConfigButton, 4, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(425, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 6, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 292, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 12, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(409, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 9, 3, 1, 2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 293, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 1, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(403, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 3, 4, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(13, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 11, 0, 2, 1)
        self.toggleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.toggleBtn.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"border-radius: 15px;")
        self.toggleBtn.setObjectName("toggleBtn")
        self.gridLayout.addWidget(self.toggleBtn, 0, 5, 1, 1)
        self.RecordsButton = QtWidgets.QPushButton(self.centralwidget)
        self.RecordsButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(61, 217, 245, 255), stop:1 rgba(240, 53, 218, 255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.RecordsButton.setObjectName("RecordsButton")
        self.gridLayout.addWidget(self.RecordsButton, 9, 2, 1, 1)
        self.CreateRecordsButton = QtWidgets.QPushButton(self.centralwidget)
        self.CreateRecordsButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(61, 217, 245, 255), stop:1 rgba(240, 53, 218, 255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.CreateRecordsButton.setObjectName("CreateRecordsButton")
        self.gridLayout.addWidget(self.CreateRecordsButton, 6, 2, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(27, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 4, 0, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 21))
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
        self.ConnectButton.setText(_translate("MainWindow", "Connect to Tracker"))
        self.DataViewButton.setText(_translate("MainWindow", "DataView"))
        self.ReadSDCard_btn.setText(_translate("MainWindow", "Read from SD card"))
        self.ConfigButton.setText(_translate("MainWindow", "Configuration"))
        self.toggleBtn.setText(_translate("MainWindow", "Disconnected"))
        self.RecordsButton.setText(_translate("MainWindow", "Records"))
        self.CreateRecordsButton.setText(_translate("MainWindow", "Create Records"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
