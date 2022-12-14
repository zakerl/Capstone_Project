import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from python_pyqt.bed_mainwindow import *
from bed_view_record_handler import *
from bed_dataview_handler import *
from bed_config_handler import *
from bed_create_record_handler import *
from bed_login_handler import *


class UI_MainWindowHandler(QWidget, Ui_MainWindow):
    def __init__(self, MainWindow):
        super(UI_MainWindowHandler, self).__init__()
        QWidget.__init__(self)
        self.MainWindow = MainWindow
        self.setupUi(self.MainWindow)
        self.connected = False
        self.toggleBtn.setFixedWidth(100)
        self.pushButton.setCheckable(True)

        self.pushButton.setFixedWidth(190)
        self.buttonCreate.setFixedWidth(190)
        self.pushButton_2.setFixedWidth(190)
        self.pushButton_3.setFixedWidth(190)
        self.pushButton_4.setFixedWidth(190)

        self.toggleBtn.setFixedHeight(31)
        self.pushButton.setFixedHeight(31)
        self.buttonCreate.setFixedHeight(31)
        self.pushButton_2.setFixedHeight(31)
        self.pushButton_3.setFixedHeight(31)
        self.pushButton_4.setFixedHeight(31)


        self.pushButton.clicked.connect(
            self.connect)
        # Conifg button
        self.pushButton_2.clicked.connect(
            lambda: self.showConfigView(self.MainWindow))
        #==================================================#
        # Create record button
        #==================================================#
        self.buttonCreate.clicked.connect(
            lambda: self.showCreateRecords(self.MainWindow)
        )
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

    def showCreateRecords(self, MainWindow):
        self.CreateWindow = UI_CreateWindow(MainWindow)
        self.CreateWindow.show()
        MainWindow.hide()

    def showDataView(self, MainWindow):
        self.DataView = UI_DataViewLogin(MainWindow)
        self.DataView.show()
        #MainWindow.hide()

    def showConfigView(self, MainWindow):
        self.ConfigView = UI_ConfigWindow(MainWindow)
        self.ConfigView.show()
        MainWindow.hide()

    def connect(self):
        if(not(self.connected)):
            if(self.pushButton.isChecked()):
                self.connected = True
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
