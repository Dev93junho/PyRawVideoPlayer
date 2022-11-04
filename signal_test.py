from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PIL import Image


import sys, os
import json

class Stream(QThread):
    image_signal = pyqtSignal(QImage)
    # get image from img folder
    def __init__(self):
        super().__init__()
        self.read_pngs()
        
    def read_pngs(self):
        # read img folder
        for png in os.listdir('img'):
            if png.endswith('.png'):
                self.img = Image.open(png)
                
                return self.img
    
    def run(self):
        # stream png images
        for i in range(10):
            self.img = self.read_pngs()
            print(self.img)
            self.image_signal.emit(self.img)

class Worker(QThread):
    trajectory_set = pyqtSignal(list)
    def __init__(self):
        super().__init__()

    def run(self):
        # get json file path
        # label text is data path
        json_path = self.label.text() + '/' + self.label.text().split('/')[-1] + '.json'
        print(json_path)
        
        # read json file
        with open(json_path, 'r') as f:
            json_data = json.load(f)
            trajectory_set = json_data['trajectory_set']
            self.trajectory_set.emit(trajectory_set)
    
class MySignal(QObject):
    signal = pyqtSignal()
    
    def run(self):
        self.signal.emit()

class test_app(QMainWindow):
    def __init__(self):
        super(test_app, self).__init__()
        # uic.loadUi('./ui/main.ui', self)
        
        mysignal = MySignal()
        mysignal.signal.connect(self.signal_emmitted)
        mysignal.run()
        
        self.worker = Worker()
        self.worker.trajectory_set.connect(self.trajectory_set)
        QPushButton('test', self).clicked.connect(self.open_file)
        
        self.lbl = QLabel(self)
        self.lbl.setGeometry(50, 50, 800, 15)
        self.lbl.setText('text')
        self.lbl.move(5, 50)
               
        self.setGeometry(500,500,1000,800)
        
        self.show()
    
    @pyqtSlot()
    def signal_emmitted(self):
        print("본 스레드 이상 무")
        
    # if click open button, open file dialog
    @pyqtSlot()
    def open_file(self):
        print("open file")
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        input_file_path = fname[0]
        print(input_file_path)  
        # if get fname[0], write fname[0] to textedit
        self.lbl.setText(input_file_path)   
    
    # @pyqtSlot()
    # def draw_graph(self):
    #     # get traj_info from json file
    #     mx = self.worker.trajectory_set[0]
    #     my = self.worker.trajectory_set[1]
    #     mz = self.worker.trajectory_set[2]
    #     fx = self.worker.trajectory_set[3]
    #     fy = self.worker.trajectory_set[4]
    #     fz = self.worker.trajectory_set[5]
    #     # print(mx, my, mz, fx, fy, fz)
        
    #     # Qchart draw graph 10 frames
    #     # create series
    #     series1 = QLineSeries()
    #     series2 = QLineSeries()
    #     series3 = QLineSeries()
    #     series4 = QLineSeries()
    #     series5 = QLineSeries()
    #     series6 = QLineSeries()
        
    #     # add data to series
    #     for i in range(len(mx)):
    #         series1.append(i, mx[i])
    #         series2.append(i, my[i])
    #         series3.append(i, mz[i])
    #         series4.append(i, fx[i])
    #         series5.append(i, fy[i])
    #         series6.append(i, fz[i])
        
    #     # create chart
    #     chart = QChart()
    #     chart.addSeries(series1)
    #     chart.addSeries(series2)
    #     chart.addSeries(series3)
    #     chart.addSeries(series4)
    #     chart.addSeries(series5)
    #     chart.addSeries(series6)
    #     chart.createDefaultAxes()
    #     chart.setTitle("Trajectory")
        
    #     # create chart view
    #     chartView = QChartView(chart)
    #     chartView.setRenderHint(QPainter.Antialiasing)
        
    #     # set chart view to layout
    #     layout = QGridLayout()
    #     layout.addWidget(chartView, 0, 0)
    #     self.setLayout(layout)
        
    #     pass
        
        
    
    @pyqtSlot()
    def png_viewer(self):
        # get png file path
        png_path = self.lbl.text() + '/' + self.lbl.text().split('/')[-1] + '/img/' + self.lbl.text().split('/')[-1] + '.png'
        print(png_path)
        
        # set png file to label
        self.lbl.setPixmap(QPixmap(png_path))
        
        # set label to layout
        layout = QGridLayout()
        layout.addWidget(self.lbl, 0, 0)
        self.setLayout(layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = test_app()
    win.show()
    app.exec_()
    