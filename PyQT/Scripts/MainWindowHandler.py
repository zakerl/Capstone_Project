import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from MainWindow import *
from ViewRecord import *
from DataViewFunctionality import *


class UI_MainWindowHandler(QWidget, Ui_MainWindow):
    def __init__(self, MainWindow):
        super(UI_MainWindowHandler, self).__init__()
        QWidget.__init__(self)
        self.MainWindow = MainWindow
        self.setupUi(self.MainWindow)

        self.toggleBtn.setFixedWidth(100)
        self.pushButton.setCheckable(True)

        self.pushButton.setFixedWidth(140)
        self.pushButton_2.setFixedWidth(140)
        self.pushButton_3.setFixedWidth(140)
        self.pushButton_4.setFixedWidth(140)

        self.toggleBtn.setFixedHeight(31)
        self.pushButton.setFixedHeight(31)
        self.pushButton_2.setFixedHeight(31)
        self.pushButton_3.setFixedHeight(31)
        self.pushButton_4.setFixedHeight(31)

        self.pushButton.clicked.connect(
            self.connect)
        #==================================================#
        # Addeed event to Records button

        self.pushButton_3.clicked.connect(
            lambda: self.showRecordWindow(self.MainWindow))
        #==================================================#

        #==================================================#
        # Added event to Dataview button
        self.pushButton_4.clicked.connect(
            lambda: self.showDataView(self.MainWindow))
        #==================================================#

    def showRecordWindow(self, MainWindow):
        self.RecordWindow = UI_RecordWindow(MainWindow)
        self.RecordWindow.show()
        MainWindow.hide()

    def showDataView(self, MainWindow):
        self.DataView = UI_DataView(MainWindow)
        self.DataView.show()
        MainWindow.hide()

    def connect(self):
        if(self.pushButton.isChecked()):
            self.toggleBtn.setText("Connected")
            style = "background-color: lightgreen"
            self.toggleBtn.setStyleSheet(
                self.toggleBtn.styleSheet() + "\n" + style)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_MainWindowHandler(MainWindow)
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
