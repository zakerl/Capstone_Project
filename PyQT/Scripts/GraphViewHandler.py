from GraphView import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PyQt5 import QtWidgets, uic
import numpy as np
import pandas as pd
from os.path import dirname, realpath, join


class UI_GraphView(QMainWindow, Ui_GraphWindow):
    def __init__(self,MainWindow):
        super(UI_GraphView, self).__init__()
        QMainWindow.__init__(self)
        self.MainWindow = MainWindow
        self.setupUi(self)
        self.all_data = []
        self.OpenDataFile()

    def OpenDataFile(self):
        try:
            scriptDir = dirname(realpath(__file__))
            FileName = scriptDir + "\DailyData.csv"
            df = pd.read_csv(FileName)
            df_temp = df
            time = df["Time"]
            HeartRate = df_temp["Heart rate"]
            # Extracting hour for easy plot for POC
            time_hour = []
            for i in time:
                t=i.split(':')
                time_hour.append(int(t[0]))\
            # color of plot line
            self.plot(time_hour,HeartRate)
        except Exception as Error:
            print (Error)


    def plot(self, time, HeartRate):
        self.GraphWidget.setBackground('#221F1F')
        pen = pg.mkPen(color=(255, 0, 0),width=2, style=QtCore.Qt.DotLine)
        self.GraphWidget.setTitle("HeartRate vs Time (hour)")
        styles = {'color':'#FFFFFF', 'font-size':'15px'}
        self.GraphWidget.setLabel('left', 'Heart rate (bpm)', **styles)
        self.GraphWidget.setLabel('bottom', 'Time (Hour)', **styles)
        self.GraphWidget.showGrid(x=True, y=True)
        self.GraphWidget.plot(time, HeartRate, pen=pen)