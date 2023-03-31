# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bed_create_record.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1094, 776)
        Dialog.setStyleSheet("background-color: rgb(1,0,1);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.FirstName = QtWidgets.QLabel(Dialog)
        self.FirstName.setStyleSheet("color: rgb(255, 255, 255);")
        self.FirstName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FirstName.setObjectName("FirstName")
        self.gridLayout.addWidget(self.FirstName, 0, 1, 1, 1)
        self.FirstNameLabel = QtWidgets.QLineEdit(Dialog)
        self.FirstNameLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.FirstNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FirstNameLabel.setObjectName("FirstNameLabel")
        self.gridLayout.addWidget(self.FirstNameLabel, 0, 2, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.LastName = QtWidgets.QLabel(Dialog)
        self.LastName.setStyleSheet("color: rgb(255, 255, 255);")
        self.LastName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LastName.setObjectName("LastName")
        self.gridLayout.addWidget(self.LastName, 1, 1, 1, 1)
        self.LastNameLabel = QtWidgets.QLineEdit(Dialog)
        self.LastNameLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.LastNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LastNameLabel.setObjectName("LastNameLabel")
        self.gridLayout.addWidget(self.LastNameLabel, 1, 2, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)
        self.Age = QtWidgets.QLabel(Dialog)
        self.Age.setStyleSheet("color: rgb(255, 255, 255);")
        self.Age.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Age.setObjectName("Age")
        self.gridLayout.addWidget(self.Age, 2, 1, 1, 1)
        self.AgeLabel = QtWidgets.QLineEdit(Dialog)
        self.AgeLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.AgeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AgeLabel.setObjectName("AgeLabel")
        self.gridLayout.addWidget(self.AgeLabel, 2, 2, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 1)
        self.ParticipantID_2 = QtWidgets.QLabel(Dialog)
        self.ParticipantID_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.ParticipantID_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ParticipantID_2.setObjectName("ParticipantID_2")
        self.gridLayout.addWidget(self.ParticipantID_2, 3, 1, 1, 1)
        self.ParticipantIDLabel = QtWidgets.QLineEdit(Dialog)
        self.ParticipantIDLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.ParticipantIDLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ParticipantIDLabel.setObjectName("ParticipantIDLabel")
        self.gridLayout.addWidget(self.ParticipantIDLabel, 3, 2, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 4, 0, 1, 1)
        self.StudyID_3 = QtWidgets.QLabel(Dialog)
        self.StudyID_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.StudyID_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.StudyID_3.setObjectName("StudyID_3")
        self.gridLayout.addWidget(self.StudyID_3, 4, 1, 1, 1)
        self.StudyIDLabel = QtWidgets.QLineEdit(Dialog)
        self.StudyIDLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.StudyIDLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StudyIDLabel.setObjectName("StudyIDLabel")
        self.gridLayout.addWidget(self.StudyIDLabel, 4, 2, 1, 3)
        spacerItem8 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 4, 5, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 5, 0, 1, 1)
        self.Gender = QtWidgets.QLabel(Dialog)
        self.Gender.setStyleSheet("color: rgb(255, 255, 255);")
        self.Gender.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Gender.setObjectName("Gender")
        self.gridLayout.addWidget(self.Gender, 5, 1, 1, 1)
        self.GenderLabel = QtWidgets.QLineEdit(Dialog)
        self.GenderLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.GenderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GenderLabel.setObjectName("GenderLabel")
        self.gridLayout.addWidget(self.GenderLabel, 5, 2, 1, 3)
        spacerItem10 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 5, 5, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 6, 0, 1, 1)
        self.Weight_2 = QtWidgets.QLabel(Dialog)
        self.Weight_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.Weight_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Weight_2.setObjectName("Weight_2")
        self.gridLayout.addWidget(self.Weight_2, 6, 1, 1, 1)
        self.WeightLabel = QtWidgets.QLineEdit(Dialog)
        self.WeightLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.WeightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WeightLabel.setObjectName("WeightLabel")
        self.gridLayout.addWidget(self.WeightLabel, 6, 2, 1, 3)
        spacerItem12 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 6, 5, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 7, 0, 1, 1)
        self.Height_2 = QtWidgets.QLabel(Dialog)
        self.Height_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.Height_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Height_2.setObjectName("Height_2")
        self.gridLayout.addWidget(self.Height_2, 7, 1, 1, 1)
        self.HeightLabel = QtWidgets.QLineEdit(Dialog)
        self.HeightLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.HeightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HeightLabel.setObjectName("HeightLabel")
        self.gridLayout.addWidget(self.HeightLabel, 7, 2, 1, 3)
        spacerItem14 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 7, 5, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 8, 0, 1, 1)
        self.PhoneNumber = QtWidgets.QLabel(Dialog)
        self.PhoneNumber.setStyleSheet("color: rgb(255, 255, 255);")
        self.PhoneNumber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PhoneNumber.setObjectName("PhoneNumber")
        self.gridLayout.addWidget(self.PhoneNumber, 8, 1, 1, 1)
        self.PhoneNumberLabel = QtWidgets.QLineEdit(Dialog)
        self.PhoneNumberLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.PhoneNumberLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PhoneNumberLabel.setObjectName("PhoneNumberLabel")
        self.gridLayout.addWidget(self.PhoneNumberLabel, 8, 2, 1, 3)
        spacerItem16 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 8, 5, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 9, 0, 1, 1)
        self.EmailID = QtWidgets.QLabel(Dialog)
        self.EmailID.setStyleSheet("color: rgb(255, 255, 255);")
        self.EmailID.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EmailID.setObjectName("EmailID")
        self.gridLayout.addWidget(self.EmailID, 9, 1, 1, 1)
        self.EmailIDLabel = QtWidgets.QLineEdit(Dialog)
        self.EmailIDLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.EmailIDLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EmailIDLabel.setObjectName("EmailIDLabel")
        self.gridLayout.addWidget(self.EmailIDLabel, 9, 2, 1, 3)
        spacerItem18 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem18, 9, 5, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem19, 10, 0, 1, 1)
        self.Address = QtWidgets.QLabel(Dialog)
        self.Address.setStyleSheet("color: rgb(255, 255, 255);")
        self.Address.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Address.setObjectName("Address")
        self.gridLayout.addWidget(self.Address, 10, 1, 1, 1)
        self.AddressLabel = QtWidgets.QLineEdit(Dialog)
        self.AddressLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.AddressLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AddressLabel.setObjectName("AddressLabel")
        self.gridLayout.addWidget(self.AddressLabel, 10, 2, 1, 3)
        spacerItem20 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem20, 10, 5, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem21, 11, 0, 1, 1)
        self.MonitoringPeriod = QtWidgets.QLabel(Dialog)
        self.MonitoringPeriod.setStyleSheet("color: rgb(255, 255, 255);")
        self.MonitoringPeriod.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MonitoringPeriod.setObjectName("MonitoringPeriod")
        self.gridLayout.addWidget(self.MonitoringPeriod, 11, 1, 1, 1)
        self.MonitoringPeriodLabel = QtWidgets.QLineEdit(Dialog)
        self.MonitoringPeriodLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.MonitoringPeriodLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MonitoringPeriodLabel.setObjectName("MonitoringPeriodLabel")
        self.gridLayout.addWidget(self.MonitoringPeriodLabel, 11, 2, 1, 3)
        spacerItem22 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem22, 11, 5, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem23, 12, 0, 1, 1)
        self.TrackerModel = QtWidgets.QLabel(Dialog)
        self.TrackerModel.setStyleSheet("color: rgb(255, 255, 255);")
        self.TrackerModel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TrackerModel.setObjectName("TrackerModel")
        self.gridLayout.addWidget(self.TrackerModel, 12, 1, 1, 1)
        self.TrackerModelLabel = QtWidgets.QLineEdit(Dialog)
        self.TrackerModelLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.TrackerModelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TrackerModelLabel.setObjectName("TrackerModelLabel")
        self.gridLayout.addWidget(self.TrackerModelLabel, 12, 2, 1, 3)
        spacerItem24 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem24, 12, 5, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem25, 13, 0, 1, 1)
        self.CreateRecord = QtWidgets.QPushButton(Dialog)
        self.CreateRecord.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.CreateRecord.setObjectName("CreateRecord")
        self.gridLayout.addWidget(self.CreateRecord, 13, 1, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem26, 13, 2, 1, 1)
        self.MainMenu = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainMenu.sizePolicy().hasHeightForWidth())
        self.MainMenu.setSizePolicy(sizePolicy)
        self.MainMenu.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.MainMenu.setObjectName("MainMenu")
        self.gridLayout.addWidget(self.MainMenu, 13, 3, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem27, 13, 4, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(357, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem28, 13, 5, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Configuration"))
        self.FirstName.setText(_translate("Dialog", "First Name"))
        self.LastName.setText(_translate("Dialog", "Last Name"))
        self.Age.setText(_translate("Dialog", "Age"))
        self.ParticipantID_2.setText(_translate("Dialog", "Participant ID"))
        self.StudyID_3.setText(_translate("Dialog", "Study ID"))
        self.Gender.setText(_translate("Dialog", "Gender"))
        self.Weight_2.setText(_translate("Dialog", "Weight"))
        self.Height_2.setText(_translate("Dialog", "Height"))
        self.PhoneNumber.setText(_translate("Dialog", "Phone Number"))
        self.EmailID.setText(_translate("Dialog", "Email ID"))
        self.Address.setText(_translate("Dialog", "Address"))
        self.MonitoringPeriod.setText(_translate("Dialog", "Monitoring Period"))
        self.TrackerModel.setText(_translate("Dialog", "Device Model"))
        self.CreateRecord.setText(_translate("Dialog", "Create Record"))
        self.MainMenu.setText(_translate("Dialog", "Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
