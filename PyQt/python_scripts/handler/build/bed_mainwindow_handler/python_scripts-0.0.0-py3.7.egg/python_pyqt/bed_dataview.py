# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_ui/bed_dataview.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataView(object):
    def setupUi(self, DataView):
        DataView.setObjectName("DataView")
        DataView.resize(1313, 1080)
        DataView.setStyleSheet("background-color: rgb(1,0,1);")
        self.gridLayout_3 = QtWidgets.QGridLayout(DataView)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(DataView)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 3)
        self.TimeLabel = QtWidgets.QLineEdit(DataView)
        self.TimeLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.TimeLabel.setObjectName("TimeLabel")
        self.gridLayout.addWidget(self.TimeLabel, 1, 5, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 8, 1, 3)
        self.label_11 = QtWidgets.QLabel(DataView)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 3)
        self.StudyIDLabel = QtWidgets.QLineEdit(DataView)
        self.StudyIDLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.StudyIDLabel.setText("")
        self.StudyIDLabel.setObjectName("StudyIDLabel")
        self.gridLayout.addWidget(self.StudyIDLabel, 2, 5, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 8, 1, 3)
        self.label_5 = QtWidgets.QLabel(DataView)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 3, 1, 2)
        self.StepsLabel = QtWidgets.QLineEdit(DataView)
        self.StepsLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.StepsLabel.setObjectName("StepsLabel")
        self.gridLayout.addWidget(self.StepsLabel, 3, 5, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 8, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 8, 2, 3)
        self.HeartRateLabel = QtWidgets.QLineEdit(DataView)
        self.HeartRateLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.HeartRateLabel.setObjectName("HeartRateLabel")
        self.gridLayout.addWidget(self.HeartRateLabel, 5, 5, 1, 3)
        self.label_2 = QtWidgets.QLabel(DataView)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 2, 1, 3)
        self.IDLabel = QtWidgets.QLineEdit(DataView)
        self.IDLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.IDLabel.setObjectName("IDLabel")
        self.gridLayout.addWidget(self.IDLabel, 6, 5, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 6, 8, 1, 3)
        self.label_4 = QtWidgets.QLabel(DataView)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 2, 1, 3)
        self.ActivityTimeLabel = QtWidgets.QLineEdit(DataView)
        self.ActivityTimeLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.ActivityTimeLabel.setObjectName("ActivityTimeLabel")
        self.gridLayout.addWidget(self.ActivityTimeLabel, 7, 5, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 7, 9, 1, 2)
        self.label_6 = QtWidgets.QLabel(DataView)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 2, 1, 3)
        self.ActivityTypeLabel = QtWidgets.QLineEdit(DataView)
        self.ActivityTypeLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.ActivityTypeLabel.setObjectName("ActivityTypeLabel")
        self.gridLayout.addWidget(self.ActivityTypeLabel, 8, 5, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 8, 9, 1, 2)
        self.label_7 = QtWidgets.QLabel(DataView)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 2, 1, 3)
        self.PromptLabel = QtWidgets.QLineEdit(DataView)
        self.PromptLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.PromptLabel.setObjectName("PromptLabel")
        self.gridLayout.addWidget(self.PromptLabel, 9, 5, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 9, 9, 1, 2)
        self.label_8 = QtWidgets.QLabel(DataView)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 10, 2, 1, 3)
        self.PainLabel = QtWidgets.QLineEdit(DataView)
        self.PainLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.PainLabel.setObjectName("PainLabel")
        self.gridLayout.addWidget(self.PainLabel, 10, 5, 1, 3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 10, 9, 1, 2)
        self.label_9 = QtWidgets.QLabel(DataView)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 11, 2, 1, 3)
        self.PainLevelLabel = QtWidgets.QLineEdit(DataView)
        self.PainLevelLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.PainLevelLabel.setObjectName("PainLevelLabel")
        self.gridLayout.addWidget(self.PainLevelLabel, 11, 5, 1, 3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 11, 9, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 12, 7, 1, 3)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 14, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 14, 10, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 15, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 15, 10, 1, 1)
        self.label_3 = QtWidgets.QLabel(DataView)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 4, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(DataView)
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
"border-radius: 15px;")
        self.BtnDescribe.setObjectName("BtnDescribe")
        self.gridLayout_2.addWidget(self.BtnDescribe, 0, 3, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 0, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 2, 1, 1, 4)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(255, 255, 255)")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 13, 0, 1, 11)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 1, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 2, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 3, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem18, 5, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem19, 6, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem20, 7, 0, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem21, 8, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem22, 9, 0, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem23, 10, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem24, 11, 0, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem25, 0, 10, 1, 1)
        self.LoadData = QtWidgets.QPushButton(DataView)
        self.LoadData.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.LoadData.setObjectName("LoadData")
        self.gridLayout.addWidget(self.LoadData, 0, 6, 1, 1)
        self.ButtonSearch = QtWidgets.QPushButton(DataView)
        self.ButtonSearch.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.ButtonSearch.setObjectName("ButtonSearch")
        self.gridLayout.addWidget(self.ButtonSearch, 12, 6, 1, 1)
        self.Graph = QtWidgets.QPushButton(DataView)
        self.Graph.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.Graph.setObjectName("Graph")
        self.gridLayout.addWidget(self.Graph, 14, 6, 1, 1)
        self.MainMenu = QtWidgets.QPushButton(DataView)
        self.MainMenu.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.MainMenu.setObjectName("MainMenu")
        self.gridLayout.addWidget(self.MainMenu, 15, 6, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(DataView)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DataView)

    def retranslateUi(self, DataView):
        _translate = QtCore.QCoreApplication.translate
        DataView.setWindowTitle(_translate("DataView", "Data View"))
        self.label_10.setText(_translate("DataView", "Time"))
        self.label_11.setText(_translate("DataView", "Study ID"))
        self.label_5.setText(_translate("DataView", "Steps"))
        self.label_2.setText(_translate("DataView", "Participant ID"))
        self.label_4.setText(_translate("DataView", "Active time (mins)"))
        self.label_6.setText(_translate("DataView", "Type of Activity"))
        self.label_7.setText(_translate("DataView", "Prompt generated"))
        self.label_8.setText(_translate("DataView", "Are you in pain?"))
        self.label_9.setText(_translate("DataView", "Pain level (1-10)"))
        self.label_3.setText(_translate("DataView", "Heart rate"))
        self.BtnDescribe.setText(_translate("DataView", "Filter"))
        self.label.setText(_translate("DataView", "Rows"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DataView", "Data"))
        self.LoadData.setText(_translate("DataView", "Load Data"))
        self.ButtonSearch.setText(_translate("DataView", "Search"))
        self.Graph.setText(_translate("DataView", "Plot data"))
        self.MainMenu.setText(_translate("DataView", "Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataView = QtWidgets.QWidget()
    ui = Ui_DataView()
    ui.setupUi(DataView)
    DataView.show()
    sys.exit(app.exec_())