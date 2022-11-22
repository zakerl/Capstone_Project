import os
import sys
from os.path import dirname, realpath, join
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
from PyQt5.uic import loadUiType
from CreateRecords import *
import numpy as np
import math
from functools import partial
from DataViewLogin import *
from DataViewHandler import *


scriptDir = dirname(realpath(__file__))

class UI_DataViewLogin(QWidget, Ui_Dialog):
    def __init__(self, MainWindow):
        super(UI_DataViewLogin, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        self.MainWindow = MainWindow
        self.all_data = []
        self.pushButton.clicked.connect(lambda: self.loginAttempt())
        self.lineEdit.returnPressed.connect(lambda: self.loginAttempt())
        self.lineEdit_2.returnPressed.connect(lambda: self.loginAttempt())
        #self.pushButton_2.clicked.connect(self.BackToMain)

    def loginAttempt(self):

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        filepath = os.path.join(scriptDir, "credentials.txt")
        with open(filepath) as f:
            lines = f.readlines()

        if lines[0].strip() == username and lines[1].strip() == password:
            loginValidity = 1
        else:
            loginValidity = 0

        if(loginValidity == 1):
            
            self.DataView = UI_DataView(self.MainWindow)
            self.DataView.show()
            self.hide()
            self.MainWindow.hide()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Incorrect attempt. Please try again.')
            msg.setWindowTitle("Error")
            msg.exec_()

        self.lineEdit.clear()
        self.lineEdit_2.clear()

    #def BackToMain(self):
    #    self.MainWindow.show()
    #    self.hide()