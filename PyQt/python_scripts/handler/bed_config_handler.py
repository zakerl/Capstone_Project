from os.path import dirname, realpath
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from python_pyqt.bed_config import *


''' This handler script saves config information that
    can later be used to upload data to device.
'''
#==================================================#
# Current method dumps config txt to CWD
#==================================================#
scriptDir = dirname(realpath(__file__))


class UI_ConfigWindow(QWidget, Ui_Form):
    def __init__(self, MainWindow):
        super(UI_ConfigWindow, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        self.MainWindow = MainWindow
        self.MainMenuBtn.clicked.connect(self.BackToMain)
        self.SaveTxt.clicked.connect(self.saveAsTxt)
        #==================================================#
        # Setting fixed button sizes for UI
        #==================================================#
        self.MainMenuBtn.setFixedHeight(31)
        self.MainMenuBtn.setFixedWidth(170)
        self.SaveTxt.setFixedHeight(31)
        self.SaveTxt.setFixedWidth(170)

        self.ActivitiesLabel.setFixedHeight(22)
        self.PromptsLabel.setFixedHeight(22)
        self.ThreshVelLabel.setFixedHeight(22)
        self.ThreshStepsLabel.setFixedHeight(22)
        self.MovementSensLabel.setFixedHeight(22)
        self.StudyIDLabel.setFixedHeight(22)

    def saveAsTxt(self):
        ActiveLabel = self.ActivitiesLabel.text()
        PromptsLabel = self.PromptsLabel.text()
        ThreshVelLabel = self.ThreshVelLabel.text()
        ThreshStepsLabel = self.ThreshStepsLabel.text()
        MovementSensLabel = self.MovementSensLabel.text()
        StudyIDLabel = self.StudyIDLabel.text()

        ref_dict = {
            "Number of Activities": ActiveLabel,
            "Prompts Generated": PromptsLabel,
            "Threshold for velocity measurement": ThreshVelLabel,
            "Threshold for Steps in a day": ThreshStepsLabel,
            "Sensitivity of movement detected": MovementSensLabel,
            "Study ID":  StudyIDLabel
        }

        configTxtToWrite = []
        for key in ref_dict:
            if(ref_dict[key] != ""):
                configTxtToWrite.append(key + ":" + str(ref_dict[key]) + "\n")
        if(len(configTxtToWrite) != 0):
            with open(scriptDir + "\\Config.txt", "w") as configTxtFile:
                print(scriptDir)
                for i in range(len(configTxtToWrite)):
                    sentences = configTxtToWrite[i]
                    configTxtFile.write(sentences)

    def BackToMain(self):
        self.MainWindow.show()
        self.hide()
