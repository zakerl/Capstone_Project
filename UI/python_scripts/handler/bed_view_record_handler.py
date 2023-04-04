'''==========================================
 Title:  BED UI record code
 Author: Labeeb Zaker
 Date:   4 April 2023
=========================================='''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
from python_pyqt.bed_view_record import *
from bed_dataview_handler import *

'''This script is used to add events to view records of participants.
    A csv/db is loaded an data is presented in tabular format for 
    searching and filtering row-wise.
'''

class UI_RecordWindow(QWidget, Ui_Form):
    def __init__(self, MainWindow):
        super(UI_RecordWindow, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        self.MainWindow = MainWindow
        self.all_data = []
        #==================================================#
        # Setting fixed button sizing
        #==================================================#
        self.ButtonOpen.setFixedHeight(31)
        self.BtnDescribe.setFixedHeight(31)
        self.ButtonSearch.setFixedHeight(31)
        self.MainMenu.setFixedHeight(31)
        self.spinBox.setFixedHeight(31)
        self.FirstNameLabel.setFixedHeight(22)
        self.LastNameLabel.setFixedHeight(22)
        self.AgeLabel.setFixedHeight(22)
        self.PIDLabel.setFixedHeight(22)
        self.StudyIDLabel.setFixedHeight(22)
        self.GenderLabel.setFixedHeight(22)
        self.WeightLabel.setFixedHeight(22)
        self.HeightLabel.setFixedHeight(22)
        self.PhnNumberLabel.setFixedHeight(22)
        self.EmailLabel.setFixedHeight(22)
        self.AddrLabel.setFixedHeight(22)
        self.MonitorPeriodLabel.setFixedHeight(22)
        self.TrackerLabel.setFixedHeight(22)
        self.ButtonOpen.clicked.connect(self.OpenFile)
        self.BtnDescribe.clicked.connect(self.dataHead)
        self.ButtonSearch.clicked.connect(self.search)
        self.MainMenu.clicked.connect(self.BackToMain)

    def OpenFile(self):
        try:
            #==================================================#
            # Access Records table from BED database
            #==================================================#
            con = sl.connect(db_path)
            sql_query = pd.read_sql('SELECT * FROM RECORDS', con)
            # Convert SQL to DataFrame
            self.all_data = pd.DataFrame(sql_query)
            self.dataHead()
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(
                0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(
                1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(
                2, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(
                3, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(
                4, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(
                5, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(
                6, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(
                7, QtWidgets.QHeaderView.Stretch)
        except Exception as Error:
            print (Error)

    def dataHead(self):
        numRow = self.spinBox.value()
        if numRow == 0:
            NumRows = len(self.all_data.index)
        else:
            NumRows = numRow
        self.tableWidget.setColumnCount(len(self.all_data.columns))
        self.tableWidget.setRowCount(NumRows)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(NumRows):
            for j in range(len(self.all_data.columns)):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def search(self):
        if(len(self.all_data) == 0):
            return
        #==================================================#
        # Variables to enter into tabular format
        #==================================================#
        firstName = self.FirstNameLabel.text()
        lastName = self.LastNameLabel.text()
        age = self.AgeLabel.text()
        ParticipantID = self.PIDLabel.text()
        gender = self.GenderLabel.text()
        weight = self.WeightLabel.text()
        height = self.HeightLabel.text()
        PhnNumber = self.PhnNumberLabel.text()
        Email = self.EmailLabel.text()
        Address = self.AddrLabel.text()
        MonitorPer = self.MonitorPeriodLabel.text()
        trackerID = self.TrackerLabel.text()
        ref_dict = {
            "FirstName": firstName,
            "LastName": lastName,
            "Age": age,
            "ParticipantID": ParticipantID,
            "StudyID": "",
            "Gender": gender,
            "Weight": weight,
            "Height": height,
            "PhoneNumber": PhnNumber,
            "EmailID": Email,
            "Address": Address,
            "MonitoringPeriod": MonitorPer,
            "TrackerModel": trackerID
        }

        headerNames = list(self.all_data.columns)
        filteredData = self.all_data
        for i in headerNames:
            filteredData[i] = filteredData[i].astype(str).str.replace(
                ".0", "", regex=False)
            if ref_dict[i] != "":
                filteredData = filteredData[filteredData[i] ==
                                            ref_dict[i]]

        NumRows = len(filteredData)
        self.tableWidget.setColumnCount(len(filteredData.columns))
        self.tableWidget.setHorizontalHeaderLabels(filteredData.columns)
        self.tableWidget.setRowCount(NumRows)
        for i in range(NumRows):
            for j in range(len(filteredData.columns)):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(filteredData.iat[i, j])))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def BackToMain(self):
        self.MainWindow.show()
        self.hide()
