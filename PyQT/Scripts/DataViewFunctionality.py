import os
import sys
from os.path import dirname, realpath, join
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
from PyQt5.uic import loadUiType
from DataView import *
import numpy as np

scriptDir = dirname(realpath(__file__))

class UI_DataView(QWidget, Ui_DataView):
    def __init__(self):
        super(UI_DataView, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        self.all_data = []
        self.LoadData.clicked.connect(self.OpenFile)
        self.BtnDescribe.clicked.connect(self.dataHead)
        self.ButtonSearch.clicked.connect(self.search)

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
        ID = self.IDLabel.text()
        Steps = self.StepsLabel.text()
        HeartRate = self.HeartRateLabel.text()
        ActivityTime = self.TimeLabel.text()
        ActivityType = self.ActivityTypeLabel.text()
        Prompt = self.PromptLabel.text()
        Pain = self.PainLabel.text()
        PainLevel = self.PainLevelLabel.text()
        ref_dict = {
            "Participant ID": ID,
            "Steps": Steps,
            "Heart rate": HeartRate,
            "Active time (mins)": ActivityTime,
            "Type of Activity": ActivityType,
            "Prompt generated": Prompt,
            "Are you in pain?": Pain,
            "Pain level (1-10)": PainLevel
        }

        headerNames = list(self.all_data.columns)
        filteredData = self.all_data

        if(ID != ""):
            filteredData = filteredData[filteredData["Participant ID"] == ID]
        for i in headerNames:
            filteredData[i] = filteredData[i].astype(str).str.replace(
                ".0", "", regex=False)
            if i.lower() != "Participant ID".lower() and ref_dict[i] != "":
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

