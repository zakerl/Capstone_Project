import sqlite3 as sl
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from python_pyqt.bed_create_record import *


'''This script stores records in database'''
db_path = 'PyQt/python_scripts/handler/BED.db'

class UI_CreateWindow(QWidget, Ui_Dialog):
    def __init__(self, MainWindow):
        super(UI_CreateWindow, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        self.MainWindow = MainWindow
        self.all_data = []
        #==================================================#
        # Setting fixed button sizes for UI
        #==================================================#
        self.MainMenu.setFixedHeight(31)
        self.CreateRecord.setFixedHeight(31)
        self.CreateRecord.setFixedWidth(170)
        self.FirstNameLabel.setFixedHeight(22)
        self.LastNameLabel.setFixedHeight(22)
        self.AgeLabel.setFixedHeight(22)
        self.ParticipantIDLabel.setFixedHeight(22)
        self.StudyIDLabel.setFixedHeight(22)
        self.GenderLabel.setFixedHeight(22)
        self.WeightLabel.setFixedHeight(22)
        self.HeightLabel.setFixedHeight(22)
        self.PhoneNumberLabel.setFixedHeight(22)
        self.EmailIDLabel.setFixedHeight(22)
        self.AddressLabel.setFixedHeight(22)
        self.MonitoringPeriodLabel.setFixedHeight(22)
        self.TrackerModelLabel.setFixedHeight(22)
        # Function event calls for events
        self.CreateRecord.clicked.connect(lambda: self.InsertDB())
        self.MainMenu.clicked.connect(self.BackToMain)

    def InsertDB(self):

        FirstName = self.FirstNameLabel.text()
        LastName = self.LastNameLabel.text()
        Age = int(self.AgeLabel.text())
        ParticipantID = int(self.ParticipantIDLabel.text())
        StudyID = int(self.StudyIDLabel.text())
        Gender = self.GenderLabel.text()
        Weight = float(self.WeightLabel.text())
        Height = float(self.HeightLabel.text())
        PhoneNumber = self.PhoneNumberLabel.text()
        EmailID = self.EmailIDLabel.text()
        Address = self.AddressLabel.text()
        MonitoringPeriod = int(self.MonitoringPeriodLabel.text())
        TrackerModel = self.TrackerModelLabel.text()

        try:
            con = sl.connect(db_path)
            cursor = con.cursor()
            # Insert values into Records table in Database
            insert_query = """ INSERT INTO RECORDS (FirstName, LastName, Age, ParticipantID, StudyID,
            Gender, Weight, Height, PhoneNumber, EmailID, Address, MonitoringPeriod, TrackerModel) VALUES 
            (?,?,?,?,?,?,?,?,?,?,?,?,?)"""

            record = (FirstName, LastName, Age, ParticipantID, StudyID,
            Gender, Weight, Height, PhoneNumber, EmailID, Address, MonitoringPeriod, TrackerModel)

            cursor.execute(insert_query, record)
            con.commit()
            cursor.close()
            con.close()

        except con.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

        

        # Clear all fields when create record button is clicked 
        self.FirstNameLabel.clear()
        self.LastNameLabel.clear()
        self.AgeLabel.clear()
        ParticipantID = self.ParticipantIDLabel.clear()
        StudyID = self.StudyIDLabel.clear()
        Gender = self.GenderLabel.clear()
        Weight = self.WeightLabel.clear()
        Height = self.HeightLabel.clear()
        PhoneNumber = self.PhoneNumberLabel.clear()
        EmailID = self.EmailIDLabel.clear()
        Address = self.AddressLabel.clear()
        MonitoringPeriod = self.MonitoringPeriodLabel.clear()
        TrackerModel = self.TrackerModelLabel.clear()

    def BackToMain(self):
        self.MainWindow.show()
        self.hide()