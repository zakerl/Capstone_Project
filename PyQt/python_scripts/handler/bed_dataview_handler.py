import sqlite3 as sl
from python_pyqt.bed_dataview import *
from bed_graph_handler import *

''' Dataview is used to check data generated from device 
    and plot meaningful graphs.
'''

scriptDir = dirname(realpath(__file__))


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
        print(base_path)
    except Exception:
        base_path = scriptDir

    return os.path.join(base_path, relative_path)


db_path = resource_path('BED.db')


class UI_DataView(QWidget, Ui_DataView):
    def __init__(self, MainWindow):
        super(UI_DataView, self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        self.MainWindow = MainWindow
        self.all_data = pd.DataFrame()
        #==================================================#
        # Rounding buttons
        #==================================================#
        self.LoadData.setFixedHeight(31)
        self.LoadData.setFixedWidth(100)
        self.BtnDescribe.setFixedHeight(31)
        self.BtnDescribe.setFixedWidth(100)
        self.ButtonSearch.setFixedHeight(31)
        self.ButtonSearch.setFixedWidth(100)
        self.MainMenu.setFixedHeight(31)
        self.MainMenu.setFixedWidth(100)
        self.SaveAsCsv.setFixedHeight(31)
        self.SaveAsCsv.setFixedWidth(130)
        self.Graph.setFixedHeight(31)
        self.Graph.setFixedWidth(100)
        self.spinBox.setFixedHeight(31)
        #==================================================#
        # Rounding text boxes
        #==================================================#
        self.TimeLabel.setFixedHeight(22)
        self.StudyIDLabel.setFixedHeight(22)
        self.IDLabel.setFixedHeight(22)
        self.StepsLabel.setFixedHeight(22)
        self.HeartRateLabel.setFixedHeight(22)
        self.ActivityTypeLabel.setFixedHeight(22)
        self.ActivityTimeLabel.setFixedHeight(22)
        self.PromptLabel.setFixedHeight(22)
        self.PainLabel.setFixedHeight(22)
        self.PainLevelLabel.setFixedHeight(22)
        #==================================================#
        # Event handlers for buttons
        #==================================================#
        self.LoadData.clicked.connect(self.LoadDb)
        self.BtnDescribe.clicked.connect(self.dataHead)
        self.ButtonSearch.clicked.connect(self.search)
        self.MainMenu.clicked.connect(self.BackToMain)
        self.Graph.clicked.connect(self.OpenGraph)
        self.SaveAsCsv.clicked.connect(self.makeCSV)

    def makeCSV(self):
        if(self.all_data.empty):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No data to save. Please load in data before saving.")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        name = QFileDialog.getSaveFileName(
            self, 'Save File', filter='*.csv')
        if(not(name)): 
            self.all_data.to_csv(name[0], index=False)
        return

    def LoadDb(self):
        try:
            # Access dataview table from BED database
            con = sl.connect(db_path)
            sql_query = pd.read_sql('SELECT * FROM DATAVIEW', con)
            # Convert SQL to DataFrame
            self.all_data = pd.DataFrame(sql_query)
            self.dataHead()
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(
                0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(
                1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(
                2, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(
                3, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(
                4, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(
                5, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(
                6, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(
                7, QtWidgets.QHeaderView.Stretch)
        except Exception as Error:
            print(Error)

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

    def search(self):
        if(len(self.all_data) == 0):
            return
        Time = self.TimeLabel.text()
        StudyID = self.StudyIDLabel.text()
        ParticipantID = self.IDLabel.text()
        Steps = self.StepsLabel.text()
        HeartRate = self.HeartRateLabel.text()
        ActivityTime = self.ActivityTimeLabel.text()
        ActivityType = self.ActivityTypeLabel.text()
        Prompt = self.PromptLabel.text()
        Pain = self.PainLabel.text()
        PainLevel = self.PainLevelLabel.text()
        Time = self.TimeLabel.text()
        ref_dict = {
            "Time": Time,
            "StudyID": StudyID,
            "Steps": Steps,
            "HeartRate": HeartRate,
            "ParticipantID": ParticipantID,
            "ActivityTimeMins": ActivityTime,
            "ActivityType": ActivityType,
            "PromptGenerated": Prompt,
            "InPain": Pain,
            "PainLevel": PainLevel
        }

        headerNames = list(self.all_data.columns)
        filteredData = self.all_data
        if(ParticipantID != ""):
            filteredData = filteredData[filteredData["ParticipantID"]
                                        == ParticipantID]
        for i in headerNames:
            filteredData[i] = filteredData[i].astype(str).str.replace(
                ".0", "", regex=False)
            if i.lower() != "ParticipantID".lower() and ref_dict[i] != "":
                filteredData = filteredData[filteredData[i] ==
                                            ref_dict[i]]

        NumRows = len(filteredData)
        self.tableWidget.setColumnCount(len(filteredData.columns))
        self.tableWidget.setHorizontalHeaderLabels(filteredData.columns)
        self.tableWidget.setRowCount(NumRows)
        for i in range(NumRows):
            for j in range(len(filteredData.columns)):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(filteredData.iat[i, j])))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def BackToMain(self):
        self.MainWindow.show()
        self.hide()

    def OpenGraph(self, type):
        self.GraphView = UI_GraphView(self.MainWindow)
        self.GraphView.show()
        self.MainWindow.hide()
