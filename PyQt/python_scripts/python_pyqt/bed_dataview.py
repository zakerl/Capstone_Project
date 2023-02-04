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
        DataView.resize(995, 927)
        DataView.setStyleSheet("background-color: rgb(34, 31, 31);")
        self.gridLayout_3 = QtWidgets.QGridLayout(DataView)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 10, 6, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 13, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 5, 1, 1)
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
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(255, 255, 255)")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
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
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget, 2, 1, 1, 4)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 11, 0, 1, 7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(DataView)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(DataView)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 6, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(DataView)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(DataView)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.PainLevelLabel = QtWidgets.QLineEdit(DataView)
        self.PainLevelLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.PainLevelLabel.setObjectName("PainLevelLabel")
        self.gridLayout.addWidget(self.PainLevelLabel, 9, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 4, 0, 1, 1)
        self.HeartGraph = QtWidgets.QPushButton(DataView)
        self.HeartGraph.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.HeartGraph.setObjectName("HeartGraph")
        self.gridLayout.addWidget(self.HeartGraph, 13, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 4, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(DataView)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(DataView)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.TimeLabel = QtWidgets.QLineEdit(DataView)
        self.TimeLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.TimeLabel.setObjectName("TimeLabel")
        self.gridLayout.addWidget(self.TimeLabel, 4, 3, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 3, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 10, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 5, 5, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 13, 5, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 9, 5, 1, 1)
        self.MainMenu = QtWidgets.QPushButton(DataView)
        self.MainMenu.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.MainMenu.setObjectName("MainMenu")
        self.gridLayout.addWidget(self.MainMenu, 12, 3, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 5, 1, 1, 1)
        self.ButtonSearch = QtWidgets.QPushButton(DataView)
        self.ButtonSearch.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.ButtonSearch.setObjectName("ButtonSearch")
        self.gridLayout.addWidget(self.ButtonSearch, 10, 3, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 12, 5, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem18, 12, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem19, 7, 5, 1, 1)
        self.LoadData = QtWidgets.QPushButton(DataView)
        self.LoadData.setStyleSheet("font-size: 14pt;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254,79,78,255), stop:1 rgba(51,15,15,255));\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-radius: 15px;")
        self.LoadData.setObjectName("LoadData")
        self.gridLayout.addWidget(self.LoadData, 0, 3, 1, 1)
        self.ActivityTypeLabel = QtWidgets.QLineEdit(DataView)
        self.ActivityTypeLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.ActivityTypeLabel.setObjectName("ActivityTypeLabel")
        self.gridLayout.addWidget(self.ActivityTypeLabel, 5, 3, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem20, 9, 0, 1, 1)
        self.PromptLabel = QtWidgets.QLineEdit(DataView)
        self.PromptLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.PromptLabel.setObjectName("PromptLabel")
        self.gridLayout.addWidget(self.PromptLabel, 6, 3, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem21, 2, 1, 1, 1)
        self.StepsLabel = QtWidgets.QLineEdit(DataView)
        self.StepsLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.StepsLabel.setObjectName("StepsLabel")
        self.gridLayout.addWidget(self.StepsLabel, 2, 3, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem22, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(DataView)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.HeartRateLabel = QtWidgets.QLineEdit(DataView)
        self.HeartRateLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.HeartRateLabel.setObjectName("HeartRateLabel")
        self.gridLayout.addWidget(self.HeartRateLabel, 3, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(DataView)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 2, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem23, 0, 4, 1, 1)
        self.IDLabel = QtWidgets.QLineEdit(DataView)
        self.IDLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.IDLabel.setObjectName("IDLabel")
        self.gridLayout.addWidget(self.IDLabel, 1, 3, 1, 1)
        self.PainLabel = QtWidgets.QLineEdit(DataView)
        self.PainLabel.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"border-radius: 11px;")
        self.PainLabel.setObjectName("PainLabel")
        self.gridLayout.addWidget(self.PainLabel, 7, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(DataView)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DataView)

    def retranslateUi(self, DataView):
        _translate = QtCore.QCoreApplication.translate
        DataView.setWindowTitle(_translate("DataView", "Data View"))
        self.label.setText(_translate("DataView", "Rows"))
        self.BtnDescribe.setText(_translate("DataView", "Filter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DataView", "Data"))
        self.label_5.setText(_translate("DataView", "Steps"))
        self.label_6.setText(_translate("DataView", "Type of Activity"))
        self.label_7.setText(_translate("DataView", "Prompt generated"))
        self.label_4.setText(_translate("DataView", "Active time (mins)"))
        self.HeartGraph.setText(_translate("DataView", "Graph for HeartRate vs Time"))
        self.label_9.setText(_translate("DataView", "Pain level (1-10)"))
        self.label_2.setText(_translate("DataView", "Participant ID"))
        self.MainMenu.setText(_translate("DataView", "Back to Main Menu"))
        self.ButtonSearch.setText(_translate("DataView", "Search"))
        self.LoadData.setText(_translate("DataView", "Load CSV"))
        self.label_3.setText(_translate("DataView", "Heart rate"))
        self.label_8.setText(_translate("DataView", "Are you in pain?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataView = QtWidgets.QWidget()
    ui = Ui_DataView()
    ui.setupUi(DataView)
    DataView.show()
    sys.exit(app.exec_())
