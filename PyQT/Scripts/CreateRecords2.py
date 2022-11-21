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
from CreateRecords import *


scriptDir = dirname(realpath(__file__))

key = "TRON"
s = len(key)

class UI_CreateWindow(QWidget, Ui_Dialog):
    def __init__(self, MainWindow):
        super(UI_CreateWindow, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        self.MainWindow = MainWindow
        self.all_data = []
        self.pushButton.clicked.connect(lambda: self.save_file())
        self.pushButton_2.clicked.connect(self.BackToMain)
        self.lineEdit.returnPressed.connect(lambda: self.save_file())
        self.lineEdit_2.returnPressed.connect(lambda: self.save_file())
        self.lineEdit_3.returnPressed.connect(lambda: self.save_file())

    def transpositionEncrypt(self,msg):
        cipher = ""
        k_indx = 0
    
        msg_len = float(len(msg))
        msg_lst = list(msg)
        key_lst = sorted(list(key))
    
        col = len(key)
        row = int(math.ceil(msg_len / col))
    
        # add the padding character '_' in empty
        fill_null = int((row * col) - msg_len)
        msg_lst.extend('_' * fill_null)
    
        # create Matrix and insert message and 
        matrix = [msg_lst[i: i + col] 
                for i in range(0, len(msg_lst), col)]
    
        # read matrix column-wise using key
        for _ in range(col):
            curr_idx = key.index(key_lst[k_indx])
            cipher += ''.join([row[curr_idx] 
                            for row in matrix])
            k_indx += 1
    
        return cipher
    
    def transpositionDecrypt(self,cipher):
        msg = ""

        k_indx = 0
        msg_indx = 0
        msg_len = float(len(cipher))
        msg_lst = list(cipher)
    
        # calculate column of the matrix
        col = len(key)
        
        # calculate maximum row of the matrix
        row = int(math.ceil(msg_len / col))
    
        # convert key into list and sort alphabetically so we can access each character by its alphabetical position.
        key_lst = sorted(list(key))
    
        # create an empty matrix to store deciphered message
        dec_cipher = []
        for _ in range(row):
            dec_cipher += [[None] * col]
    
        # Arrange the matrix column wise according to permutation order by adding into new matrix
        for _ in range(col):
            curr_idx = key.index(key_lst[k_indx])
    
            for j in range(row):
                dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                msg_indx += 1
            k_indx += 1
    
        # convert decrypted msg matrix into a string
        msg = ''.join(sum(dec_cipher, []))
    
        null_count = msg.count('_')
    
        if null_count > 0:
            return msg[: -null_count]
    
        eliminate = "y"
        for char in eliminate:
            msg = msg.replace(char, "")

        return msg

    def caesarEncrypt(self,text,keylength):
        result = ""

        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + keylength-65) % 26 + 65)
    
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + keylength - 97) % 26 + 97)
                    
        return result

    def caeserDecrypt(self,text, keylength):
        return self.caesarEncrypt(text,26-keylength)

    def encryption(self,entry):
        keylength = s
        partiallyCiphered = self.transpositionEncrypt(entry)
        ciphered = self.caesarEncrypt(partiallyCiphered, keylength)
        return ciphered

    def decryption(self,entry):
        keylength = s
        partiallyDeciphered = self.caeserDecrypt(entry, keylength)
        deciphered = self.transpositionDecrypt(partiallyDeciphered)
        return deciphered

    def save_file(self):

        inputName = self.lineEdit.text()
        inputAge = self.lineEdit_2.text()
        inputID = self.lineEdit_3.text()
        
        # Having spaces in inputs is okay....
        eliminate = " "
        for char in eliminate:
            temporaryName = inputName.replace(char, "")
            temporaryAge = inputAge.replace(char, "")
            temporaryID = inputID.replace(char, "")

        if (not inputName.isalpha() and not temporaryName.isalpha()):
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
        
        elif (inputName == "" or inputAge == ""or inputID == ""):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Missing Inputs!')
            msg.setWindowTitle("Error")
            msg.exec_()

        else:
            cipheredName = self.encryption(inputName)
            cipheredAge = self.encryption(inputAge)
            cipheredID = self.encryption(inputID)

            filepath = os.path.join(r'C:\Users\jessi\Desktop\MECHTRON_4TB6\GitBranch\Capstone_Project\PyQT\Scripts', 'encrypted.txt')

            with open(filepath, 'w') as f: 
                f.write("Encrypted Name: " + cipheredName + "\n")
                f.write("Encrypted Age: " + cipheredAge + "\n")
                f.write("Encrypted ID: " + cipheredID + "\n")

            filepath2 = os.path.join(r'C:\Users\jessi\Desktop\MECHTRON_4TB6\GitBranch\Capstone_Project\PyQT\Scripts', 'decrypted.txt')

            with open(filepath2, 'w') as f: 
                f.write("Name: " + self.decryption(cipheredName)+ "\n")
                f.write("Age: " + self.decryption(cipheredAge)+ "\n")
                f.write("ID: " + self.decryption(cipheredID)+ "\n")

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