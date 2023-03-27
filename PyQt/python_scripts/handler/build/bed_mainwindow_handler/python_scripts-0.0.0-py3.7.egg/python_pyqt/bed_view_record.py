# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_ui/bed_view_record.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1209, 953)
        Form.setStyleSheet("background-color: rgb(1,0,1);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 2)
        self.ButtonOpen = QtWidgets.QPushButton(Form)
        self.ButtonOpen.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;\n"
"")
        self.ButtonOpen.setObjectName("ButtonOpen")
        self.gridLayout.addWidget(self.ButtonOpen, 0, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)
        self.FirstNameLabel = QtWidgets.QLineEdit(Form)
        self.FirstNameLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.FirstNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FirstNameLabel.setObjectName("FirstNameLabel")
        self.gridLayout.addWidget(self.FirstNameLabel, 1, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 8, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 3, 1, 1)
        self.LastNameLabel = QtWidgets.QLineEdit(Form)
        self.LastNameLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.LastNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LastNameLabel.setObjectName("LastNameLabel")
        self.gridLayout.addWidget(self.LastNameLabel, 2, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 8, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 3, 1, 1)
        self.AgeLabel = QtWidgets.QLineEdit(Form)
        self.AgeLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.AgeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AgeLabel.setObjectName("AgeLabel")
        self.gridLayout.addWidget(self.AgeLabel, 3, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 8, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(161, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 3, 1, 1)
        self.PIDLabel = QtWidgets.QLineEdit(Form)
        self.PIDLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.PIDLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PIDLabel.setObjectName("PIDLabel")
        self.gridLayout.addWidget(self.PIDLabel, 4, 5, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(330, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 4, 7, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(330, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 5, 0, 1, 2)
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 2, 1, 2)
        self.StudyIDLabel = QtWidgets.QLineEdit(Form)
        self.StudyIDLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.StudyIDLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StudyIDLabel.setObjectName("StudyIDLabel")
        self.gridLayout.addWidget(self.StudyIDLabel, 5, 4, 1, 2)
        spacerItem11 = QtWidgets.QSpacerItem(161, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 5, 7, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 6, 1, 2, 2)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 3, 1, 1)
        self.GenderLabel = QtWidgets.QLineEdit(Form)
        self.GenderLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.GenderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GenderLabel.setObjectName("GenderLabel")
        self.gridLayout.addWidget(self.GenderLabel, 6, 5, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 7, 8, 2, 1)
        spacerItem14 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 8, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 3, 1, 1)
        self.WeightLabel = QtWidgets.QLineEdit(Form)
        self.WeightLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.WeightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WeightLabel.setObjectName("WeightLabel")
        self.gridLayout.addWidget(self.WeightLabel, 8, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 3, 1, 1)
        self.HeightLabel = QtWidgets.QLineEdit(Form)
        self.HeightLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.HeightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HeightLabel.setObjectName("HeightLabel")
        self.gridLayout.addWidget(self.HeightLabel, 9, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 10, 3, 1, 1)
        self.PhnNumberLabel = QtWidgets.QLineEdit(Form)
        self.PhnNumberLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.PhnNumberLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PhnNumberLabel.setObjectName("PhnNumberLabel")
        self.gridLayout.addWidget(self.PhnNumberLabel, 10, 5, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 10, 8, 1, 1)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 11, 3, 1, 1)
        self.EmailLabel = QtWidgets.QLineEdit(Form)
        self.EmailLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.EmailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EmailLabel.setObjectName("EmailLabel")
        self.gridLayout.addWidget(self.EmailLabel, 11, 5, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 12, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 12, 3, 1, 1)
        self.AddrLabel = QtWidgets.QLineEdit(Form)
        self.AddrLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.AddrLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AddrLabel.setObjectName("AddrLabel")
        self.gridLayout.addWidget(self.AddrLabel, 12, 5, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 12, 8, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem18, 13, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 13, 3, 1, 2)
        self.MonitorPeriodLabel = QtWidgets.QLineEdit(Form)
        self.MonitorPeriodLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.MonitorPeriodLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MonitorPeriodLabel.setObjectName("MonitorPeriodLabel")
        self.gridLayout.addWidget(self.MonitorPeriodLabel, 13, 5, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem19, 13, 8, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem20, 14, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 14, 3, 1, 1)
        self.TrackerLabel = QtWidgets.QLineEdit(Form)
        self.TrackerLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.TrackerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TrackerLabel.setObjectName("TrackerLabel")
        self.gridLayout.addWidget(self.TrackerLabel, 14, 5, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(161, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem21, 14, 7, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem22, 15, 0, 1, 1)
        self.ButtonSearch = QtWidgets.QPushButton(Form)
        self.ButtonSearch.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;\n"
"")
        self.ButtonSearch.setObjectName("ButtonSearch")
        self.gridLayout.addWidget(self.ButtonSearch, 15, 5, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(161, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem23, 15, 7, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 0, 2, 1, 1)
        self.BtnDescribe = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.BtnDescribe.setFont(font)
        self.BtnDescribe.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;\n"
"")
        self.BtnDescribe.setObjectName("BtnDescribe")
        self.gridLayout_2.addWidget(self.BtnDescribe, 0, 3, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 2, 1, 1, 4)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 16, 0, 1, 9)
        spacerItem24 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem24, 17, 3, 1, 1)
        self.MainMenu = QtWidgets.QPushButton(Form)
        self.MainMenu.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;\n"
"")
        self.MainMenu.setObjectName("MainMenu")
        self.gridLayout.addWidget(self.MainMenu, 17, 5, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Record"))
        self.ButtonOpen.setText(_translate("Form", "Load Records"))
        self.label_2.setText(_translate("Form", "First Name"))
        self.label_10.setText(_translate("Form", "Last Name"))
        self.label_5.setText(_translate("Form", "Age"))
        self.label_3.setText(_translate("Form", "Participant ID"))
        self.label_14.setText(_translate("Form", "Study ID"))
        self.label_4.setText(_translate("Form", "Gender"))
        self.label_6.setText(_translate("Form", "Weight (Kgs)"))
        self.label_7.setText(_translate("Form", "Height (cm)"))
        self.label_8.setText(_translate("Form", "Phone Number"))
        self.label_11.setText(_translate("Form", "Email"))
        self.label_12.setText(_translate("Form", "Address"))
        self.label_13.setText(_translate("Form", "Monitoring Period"))
        self.label_9.setText(_translate("Form", "Tracker ID"))
        self.ButtonSearch.setText(_translate("Form", "Search"))
        self.label.setText(_translate("Form", "Rows"))
        self.BtnDescribe.setText(_translate("Form", "Filter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Data"))
        self.MainMenu.setText(_translate("Form", "Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
