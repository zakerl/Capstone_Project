from GraphView import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PyQt5 import QtWidgets, uic

class UI_GraphView(QMainWindow, Ui_GraphWindow):
    def __init__(self,MainWindow):
        super(UI_GraphView, self).__init__()
        QMainWindow.__init__(self)
        self.MainWindow = MainWindow
        self.setupUi(self)
        self.all_data = []
        self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])

    def plot(self, hour, temperature):
        self.GraphWidget.plot(hour, temperature)