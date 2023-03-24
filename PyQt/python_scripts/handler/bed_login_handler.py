import os
from os.path import dirname, realpath, abspath
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from python_pyqt.bed_create_record import *
from python_pyqt.bed_login import *
from bed_dataview_handler import *
from bed_mainwindow_handler import *


scriptDir = dirname(realpath(__file__))
path = dirname(abspath(__file__))


class UI_DataViewLogin(QWidget, Ui_Dialog):
    def __init__(self, MainWindow):
        super(UI_DataViewLogin, self).__init__()
        QWidget.__init__(self)
        self.MainWindow = MainWindow
        self.setupUi(self)
        self.all_data = []
        self.label_4.setPixmap(QPixmap(os.path.join(path, 'BED_logo.jpg')))
        self.label_2.setFixedWidth(190)
        self.label_3.setFixedWidth(190)
        self.lineEdit.setFixedWidth(190)
        self.lineEdit_2.setFixedWidth(190)
        self.pushButton.setFixedWidth(190)

        self.label_2.setFixedHeight(31)
        self.label_3.setFixedHeight(31)
        self.lineEdit.setFixedHeight(31)
        self.lineEdit_2.setFixedHeight(31)
        self.pushButton.setFixedHeight(31)

        self.pushButton.clicked.connect(lambda: self.loginAttempt())
        self.lineEdit.returnPressed.connect(lambda: self.loginAttempt())
        self.lineEdit_2.returnPressed.connect(lambda: self.loginAttempt())

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
            self.ToMain()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Incorrect attempt. Please try again.')
            msg.setWindowTitle("Error")
            msg.exec_()

        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def ToMain(self):
        self.MainWindow.show()
        self.hide()
