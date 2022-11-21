import os
import sys
from os.path import dirname, realpath, join
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
from PyQt5.uic import loadUiType
from ViewRecord_2 import *
import numpy as np

scriptDir = dirname(realpath(__file__))
#From_Main, _ = loadUiType(join(dirname(__file__), "ViewRecord_2.ui"))


class UI_RecordWindow(QWidget, Ui_Form):
    def __init__(self, MainWindow):
        super(UI_RecordWindow, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        self.MainWindow = MainWindow
        self.all_data = []
        self.ButtonOpen.setFixedHeight(31)
        self.BtnDescribe.setFixedHeight(31)
        self.ButtonSearch.setFixedHeight(31)
        self.MainMenu.setFixedHeight(31)
        self.spinBox.setFixedHeight(31)
        self.FirstNameLabel.setFixedHeight(22)
        self.LastNameLabel.setFixedHeight(22)
        self.AgeLabel.setFixedHeight(22)
        self.PIDLabel.setFixedHeight(22)
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
            path = QFileDialog.getOpenFileName(
                self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')[0]
            self.all_data = pd.read_csv(path)
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
        except:
            print(path)

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
            "First Name": firstName,
            "Last Name": lastName,
            "Age": age,
            "Participant ID": ParticipantID,
            "Gender": gender,
            "Weight (kgs)": weight,
            "Height (cm)": height,
            "Phone number": PhnNumber,
            "Email ID": Email,
            "Address": Address,
            "Monitoring Period": MonitorPer,
            "Tracker model": trackerID
        }

        # searchResults = [row for row in self.all_data if]
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
