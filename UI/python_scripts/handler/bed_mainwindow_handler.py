'''==========================================
 Title:  BED UI main code
 Author: Nish Shah, Labeeb Zaker
 Date:   4 April 2023
=========================================='''
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
import time
import serial as sr
import sqlite3 as sl


db_path = 'PyQt/python_scripts/handler/BED.db'

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
        self.ReadSD.setFixedWidth(190)
        self.ConfigButton.setFixedWidth(190)
        self.RecordsButton.setFixedWidth(190)
        self.DataViewButton.setFixedWidth(190)

        self.CreateRecordsButton.setFixedHeight(31)
        self.ReadSD.setFixedHeight(31)
        self.ConfigButton.setFixedHeight(31)
        self.RecordsButton.setFixedHeight(31)
        self.DataViewButton.setFixedHeight(31)

        self.ReadSD.clicked.connect(self.OpenSerial)
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

    def OpenSerial(self):
        print("Reading soon")
        baudrate = 115200
        port = "COM4"

        portSerial = sr.Serial(port=port, baudrate=baudrate)
        data = ""
        if portSerial.is_open:
            time.sleep(5)
            size = portSerial.inWaiting()
            if size:
                data = portSerial.read(size)
                print(data)
        else:
            print('serial not open')

        if data == "":
            print ("Something went wrong")
            MainWindow.hide()
            MainWindow.show()

        data = data.decode("utf-8").strip()
        insert_list = data.split("\n")
        Time = insert_list[0]
        StudyID = int(insert_list[1])
        Steps = int(insert_list[2])
        HeartRate = int(insert_list[3])
        ParticipantID = int(insert_list[4])
        ActivityTimeMins = int(insert_list[5])
        ActivityType = insert_list[6]
        PromptGenerated = insert_list[7]
        InPain = insert_list[8]
        PainLevel = int(insert_list[9])

        try:
            con = sl.connect(db_path)
            cursor = con.cursor()
            # Insert values into Records table in Database
            insert_query = """ INSERT INTO DATAVIEW (Time, StudyID, Steps, HeartRate, ParticipantID,
            ActivityTimeMins, ActivityType, PromptGenerated, InPain, PainLevel) VALUES 
            (?,?,?,?,?,?,?,?,?,?)"""

            record = (Time, StudyID, Steps, HeartRate, ParticipantID,
            ActivityTimeMins, ActivityType, PromptGenerated, InPain, PainLevel)

            cursor.execute(insert_query, record)
            con.commit()
            cursor.close()
            con.close()

        except con.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

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
