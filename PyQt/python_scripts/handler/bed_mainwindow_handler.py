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

'''
This script handles the MainWindow and is used to generate the Main GUI, Run MainWindowHandler.py 
MainWindowHandler.py is used for handling button clicks/events to redirect to other windows.
MainWindow.py is generated from MainWindow.ui (PyQt Designer) for frontend. 
'''
class UI_MainWindowHandler(QWidget, Ui_MainWindow):
    def __init__(self, MainWindow):
        super(UI_MainWindowHandler, self).__init__()
        QWidget.__init__(self)
        self.MainWindow = MainWindow
        self.setupUi(self.MainWindow)
        #==================================================#
        # Setting fixed width and height 
        # for buttons on MainMenu
        #==================================================#
        self.CreateRecordsButton.setFixedWidth(190)
        self.ConfigButton.setFixedWidth(190)
        self.RecordsButton.setFixedWidth(190)
        self.DataViewButton.setFixedWidth(190)

        self.CreateRecordsButton.setFixedHeight(31)
        self.ConfigButton.setFixedHeight(31)
        self.RecordsButton.setFixedHeight(31)
        self.DataViewButton.setFixedHeight(31)

        #==================================================#
        # Config button events opens configuration window
        #==================================================#
        self.ConfigButton.clicked.connect(
            lambda: self.showConfigView(self.MainWindow))
        #==================================================#
        # Create record button event opens create 
         # record window
        #==================================================#
        self.CreateRecordsButton.clicked.connect(
            lambda: self.showCreateRecords(self.MainWindow)
        )
        #==================================================#
        # Records button opens view record window
        #==================================================#

        self.RecordsButton.clicked.connect(
            lambda: self.showRecordWindow(self.MainWindow))
        #==================================================#
        # Added event to Dataview button, 
        # opens DataView with graph
        #==================================================#
        self.DataViewButton.clicked.connect(
            lambda: self.showDataView(self.MainWindow))
    '''
    Different windows open when buttons are clicked, event handler functions described below
    '''
    def showRecordWindow(self, MainWindow):
        self.RecordWindow = UI_RecordWindow(MainWindow)
        self.RecordWindow.show()
        MainWindow.hide()

    def showCreateRecords(self, MainWindow):
        self.CreateWindow = UI_CreateWindow(MainWindow)
        self.CreateWindow.show()
        MainWindow.hide()

    def showConfigView(self, MainWindow):
        self.ConfigView = UI_ConfigWindow(MainWindow)
        self.ConfigView.show()
        MainWindow.hide()

    def showDataView(self, MainWindow):
        self.DataView = UI_DataView(MainWindow)
        self.DataView.show()
        MainWindow.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_MainWindowHandler(MainWindow)
    LoginWindow = UI_DataViewLogin(MainWindow)
    LoginWindow.show()
    sys.exit(app.exec_())