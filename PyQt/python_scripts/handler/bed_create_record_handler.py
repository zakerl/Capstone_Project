import os
from os.path import dirname, realpath
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from python_pyqt.bed_create_record import *


'''This script stores records in database'''


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

    def save_file(self):

        inputName = self.lineEdit.text()
        inputAge = self.lineEdit_2.text()
        inputID = self.lineEdit_3.text()
        #==================================================#
        # Having spaces in inputs is okay....
        #==================================================#
        eliminate = " "
        for char in eliminate:
            temporaryName = inputName.replace(char, "")
            temporaryAge = inputAge.replace(char, "")
            temporaryID = inputID.replace(char, "")

        if (inputName == "" or inputAge == ""or inputID == ""):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Missing Inputs!')
            msg.setWindowTitle("Error")
            msg.exec_()
        
        elif (not inputName.isalpha() and not temporaryName.isalpha()):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Participant name must be in alphabets!')
            msg.setWindowTitle("Error")
            msg.exec_()
        
        elif (inputAge.isalpha() and temporaryAge.isalpha()):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Participant Age must be in numbers!')
            msg.setWindowTitle("Error")
            msg.exec_()

        elif (inputID.isalpha() and temporaryID.isalpha()):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Device ID must be in numbers!')
            msg.setWindowTitle("Error")
            msg.exec_()

        else:
            cipheredName, badIndex = self.encryption(inputName)
            cipheredAge, badIndex = self.encryption(inputAge)
            cipheredID, badIndex = self.encryption(inputID)

            filepath = os.path.join(scriptDir, 'encrypted.txt')

            with open(filepath, 'w') as f: 
                f.write("Encrypted Name: " + cipheredName + "\n")
                f.write("Encrypted Age: " + cipheredAge + "\n")
                f.write("Encrypted ID: " + cipheredID + "\n")

            filepath2 = os.path.join(scriptDir, 'decrypted.txt')

            with open(filepath2, 'w') as f: 
                f.write("Name: " + self.decryption(cipheredName, badIndex)+ "\n")
                f.write("Age: " + self.decryption(cipheredAge, badIndex)+ "\n")
                f.write("ID: " + self.decryption(cipheredID, badIndex)+ "\n")

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Saved!")
            msg.setInformativeText('Data is created and saved. Check the folder.')
            msg.setWindowTitle("Saved")
            msg.exec_()
        
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()

    def BackToMain(self):
        self.MainWindow.show()
        self.hide()