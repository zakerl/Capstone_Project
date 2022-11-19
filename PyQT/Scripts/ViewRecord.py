import os
import sys
from os.path import dirname, realpath, join
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
from PyQt5.uic import loadUiType


scriptDir = dirname(realpath(__file__))
From_Main, _ = loadUiType(join(dirname(__file__), "ViewRecord_2.ui"))


class UI_RecordWindow(QWidget, From_Main):
    def __init__(self):
        super(UI_RecordWindow, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)

        self.ButtonOpen.clicked.connect(self.OpenFile)
        self.BtnDescribe.clicked.connect(self.dataHead)

    def OpenFile(self):
        try:
            path = QFileDialog.getOpenFileName(
                self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')[0]
            self.all_data = pd.read_csv(path)
            self.dataHead()
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


# app = QApplication(sys.argv)
# sheet = UI_Record()
# sheet.show()
# sys.exit(app.exec_())
