import sqlite3 as sl
from python_pyqt.bed_graph import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyqtgraph as pg
import pandas as pd
import sys
from os.path import dirname, realpath
import os
'''Graph handler handles the graph window along with its appearance and format'''
scriptDir = dirname(realpath(__file__))


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
        print(base_path)
    except Exception:
        base_path = scriptDir

    return os.path.join(base_path, relative_path)


db_path = resource_path('BED.db')


class UI_GraphView(QMainWindow, Ui_GraphWindow):
    def __init__(self, MainWindow):
        super(UI_GraphView, self).__init__()
        QMainWindow.__init__(self)
        self.MainWindow = MainWindow
        self.setupUi(self)
        self.HeartGraph.setFixedHeight(31)
        self.StepsGraph.setFixedHeight(31)
        self.ActivityGraph.setFixedHeight(31)
        self.HeartGraph.setFixedWidth(150)
        self.StepsGraph.setFixedWidth(150)
        self.ActivityGraph.setFixedWidth(150)
        self.HeartGraph.clicked.connect(self.OpenHeart)
        self.StepsGraph.clicked.connect(self.OpenSteps)
        self.ActivityGraph.clicked.connect(self.OpenActivity)

    def OpenHeart(self):
        try:
            self.GraphWidget.clear()
            # Access dataview table from BED database
            con = sl.connect(db_path)
            sql_query = pd.read_sql(
                'SELECT TIME, HEARTRATE FROM DATAVIEW', con)
            # Convert SQL to DataFrame
            df = pd.DataFrame(sql_query)
            df = df.sort_values(by="Time")  # To plot smooth graph
            TimeAxis = df['Time']
            HeartRate = df["HeartRate"]
            # ==================================================#
            # Extracting hour for easy plot for POC
            # ==================================================#
            PlotTime = []
            for i in TimeAxis:
                t = i.split(':')
                time_hour = float(t[0])
                time_min = float(t[1])
                # Logic for extracting and only plotting time in hour
                if (time_min > 20 and time_hour <= 40):  # Assume 1:20 is 1 and 1:40 is 2
                    time_hour += 0.5
                elif (time_min > 40):
                    time_hour += 1
                PlotTime.append(time_hour)
            self.plot(PlotTime, HeartRate, name='Heart Rate', color='#FF5B02')
        except Exception as Error:
            print(Error)

    def OpenSteps(self):
        try:
            self.GraphWidget.clear()
            # Access dataview table from BED database
            con = sl.connect(db_path)
            sql_query = pd.read_sql('SELECT TIME, STEPS FROM DATAVIEW', con)
            # Convert SQL to DataFrame
            df = pd.DataFrame(sql_query)
            df = df.sort_values(by="Time")  # To plot smooth graph
            TimeAxis = df['Time']
            Steps = df['Steps']
            # ==================================================#
            # Extracting hour for easy plot for POC
            # ==================================================#
            PlotTime = []
            for i in TimeAxis:
                t = i.split(':')
                time_hour = float(t[0])
                time_min = float(t[1])
                # Logic for extracting and only plotting time in hour
                if (time_min > 20 and time_hour <= 40):  # Assume 1:20 is 1 and 1:40 is 2
                    time_hour += 0.5
                elif (time_min > 40):
                    time_hour += 1
                PlotTime.append(time_hour)
            self.plot(PlotTime, Steps, name='Steps', color='#1D8DF1')
        except Exception as Error:
            print(Error)

    def OpenActivity(self):
        try:
            self.GraphWidget.clear()
            # Access dataview table from BED database
            con = sl.connect(db_path)
            sql_query = pd.read_sql(
                'SELECT TIME, ACTIVITYTIMEMINS FROM DATAVIEW', con)
            # Convert SQL to DataFrame
            df = pd.DataFrame(sql_query)
            df = df.sort_values(by="Time")  # To plot smooth graph
            TimeAxis = df['Time']
            ActivityTime = df['ActivityTimeMins']
            # ==================================================#
            # Extracting hour for easy plot for POC
            # ==================================================#
            PlotTime = []
            for i in TimeAxis:
                t = i.split(':')
                time_hour = float(t[0])
                time_min = float(t[1])
                # Logic for extracting and only plotting time in hour
                if (time_min > 20 and time_hour <= 40):  # Assume 1:20 is 1 and 1:40 is 2
                    time_hour += 0.5
                elif (time_min > 40):
                    time_hour += 1
                PlotTime.append(time_hour)
            self.plot(PlotTime, ActivityTime,
                      name='Activity time (mins)', color='#B809D6')
        except Exception as Error:
            print(Error)

    def plot(self, PlotTime, Yaxis, name, color):
        self.GraphWidget.setBackground('#221F1F')
        pen = pg.mkPen(color, width=2, style=QtCore.Qt.DotLine)
        self.GraphWidget.setTitle("Data View graph")
        styles = {'color': '#FFFFFF', 'font-size': '15px'}
        self.GraphWidget.setLabel('left', name, **styles)
        self.GraphWidget.setLabel('bottom', 'Time (Hour)', **styles)
        self.GraphWidget.showGrid(x=True, y=True)
        self.GraphWidget.addLegend()
        self.GraphWidget.plot(PlotTime, Yaxis, name=name,  pen=pen)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_GraphView(MainWindow)
    ui.show()
    sys.exit(app.exec_())
