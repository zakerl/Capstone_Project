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
import bluetooth
import struct
import sqlite3 as sl
import re


scriptDir = dirname(realpath(__file__))

'''
This script handles the MainWindow and is used to generate the Main GUI, Run MainWindowHandler.py 
MainWindowHandler.py is used for handling button clicks/events to redirect to other windows.
MainWindow.py is generated from MainWindow.ui (PyQt Designer) for frontend. 
'''


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
        print(base_path)
    except Exception:
        base_path = scriptDir

    return os.path.join(base_path, relative_path)


db_path = resource_path('BED.db')


class UI_MainWindowHandler(QWidget, Ui_MainWindow):
    def __init__(self, MainWindow):
        super(UI_MainWindowHandler, self).__init__()
        QWidget.__init__(self)
        self.MainWindow = MainWindow
        self.setupUi(self.MainWindow)
        self.connected = False
        self.ReadSD.setCheckable(True)
        #==================================================#
        # Setting fixed width and height
        # for buttons on MainMenu
        #==================================================#
        self.label.setPixmap(QPixmap(resource_path('BED_logo.jpg')))
        self.CreateRecordsButton.setFixedWidth(190)
        self.toggleBtn.setFixedWidth(190)
        self.ReadSD.setFixedWidth(190)
        self.ConfigButton.setFixedWidth(190)
        self.RecordsButton.setFixedWidth(190)
        self.DataViewButton.setFixedWidth(190)

        self.CreateRecordsButton.setFixedHeight(31)
        self.toggleBtn.setFixedHeight(31)
        self.ReadSD.setFixedHeight(31)
        self.ConfigButton.setFixedHeight(31)
        self.RecordsButton.setFixedHeight(31)
        self.DataViewButton.setFixedHeight(31)
        #==================================================#
        #  Open bluetooth connection via sockets
        #==================================================#
        self.ReadSD.clicked.connect(self.ReadBluetooth)
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

    def ReadBluetooth(self):
        loop_time = 10
        bd_addr = "d4:d4:da:1d:de:a6"  # Mac address (hardcoded) for ESP32
        ser = ""
        s = struct.Struct('<' + str(10) + 'f')
        SAMPLES = 30000
        port = 1
        connected = False
        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((bd_addr, port))
            print('Connected')
            connected = True
            self.connect()
        except Exception as error:
            print(error)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Failed to connect to device via bluetooth.")
            msg.setInformativeText(format(error))
            msg.setWindowTitle("Error")
            msg.exec_()

        sock.send("r")
        print('Sent data')
        data = ""

        start_time = time.time()
        start_end_bit = []
        try:
            while True:
                rec_data = sock.recv(1024)
                if len(rec_data) == 0:
                    break
                rec_data = rec_data.decode("utf-8").strip()
                if (rec_data != '0'):
                    data += rec_data
                else:
                    start_end_bit.append(rec_data)
                end_time = time.time()
                if (end_time - start_time > loop_time or len(start_end_bit) >= 2):  # Run for t seconds
                    break
                tmp = re.search("File not available", data)
                if (tmp is not None):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error")
                    msg.setInformativeText(
                        "File not available on sd card, try again")
                    msg.setWindowTitle("Error reading data")
                    msg.exec_()
                    break
            print("===================")
            print(data)
            print("===================")
        except:
            pass
        insert_list = data.split("\n")
        for entry in insert_list:
            entry_list = entry.split(",")
            try:
                Date = entry_list[0]
                Time = entry_list[1]
                Steps = int(entry_list[2])
                HeartRate = int(entry_list[3])
                ActivityTimeMins = int(entry_list[4])
                ActivityType = entry_list[5]
                InPain = entry_list[6]
                WhyStop = entry_list[7]
                PainLocation = entry_list[8]
                PainLevel = int(entry_list[9])
                # print(Time, StudyID, Steps, HeartRate, ParticipantID,
                #       ActivityTimeMins, ActivityType, PromptGenerated, InPain, PainLevel)
            except Exception as error:
                print(error)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(
                    "Error, bluetooth serial communication went wrong.")
                msg.setInformativeText(format(error))
                msg.setWindowTitle("Error")
                msg.exec_()
            try:
                inserted = False
                con = sl.connect(db_path)
                cursor = con.cursor()
                # Insert values into Records table in Database
                insert_query = """ INSERT INTO DATAVIEW (Date, Time, Steps, HeartRate,
                ActivityTimeMins, ActivityType, InPain, WhyStop, PainLocation, PainLevel) VALUES 
                (?,?,?,?,?,?,?,?,?,?)"""

                record = (Date, Time, Steps, HeartRate,
                          ActivityTimeMins, ActivityType, InPain, WhyStop, PainLocation, PainLevel)
                cursor.execute(insert_query, record)
                con.commit()
                cursor.close()
                con.close()
                inserted = True
            except con.Error as error:
                print("Failed to insert into MySQL table {}".format(error))
                inserted = False

        if (inserted == True):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Succesfully inserted data from device to database!")
            msg.setWindowTitle("Insertion successful")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Failed to insert into database.")
            msg.setInformativeText(format(error))
            msg.setWindowTitle("Error")
            msg.exec_()

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

    def connect(self):
        if(not(self.connected)):
            if(self.ReadSD.isChecked()):
                self.connected = True
                self.toggleBtn.setText("Connected")
                style = "background-color: lightgreen"
                self.toggleBtn.setStyleSheet(
                    self.toggleBtn.styleSheet() + "\n" + style)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_MainWindowHandler(MainWindow)
    LoginWindow = UI_DataViewLogin(MainWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
