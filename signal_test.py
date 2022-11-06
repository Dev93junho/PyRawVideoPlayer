from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
# from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PIL import Image


import sys, os
import json
from engine.DataLoader import DataLoader

"""
1. 데이터 파일 선택하면 json 파일 불러와야함
2. json 파일 선택하면 이미지랑 좌표정보 불러와야함
3. 이미지 띄우고 좌표정보 프레임 10개씩 matplotlib로 그려야함
"""

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
        # self.worker.trajectory_set.connect(self.trajectory_set)
        self.btn_get_path = QPushButton('test', self).clicked.connect(self.open_file)
        
        self.lbl = QLabel(self)
        self.lbl.setGeometry(50, 50, 800, 15)
        self.lbl.setText('text')
        self.lbl.move(5, 50)
        
        self.setGeometry(500,300,1000,800)
        self.show()
    
    @pyqtSlot()
    def signal_emmitted(self):
        print("본 스레드 이상 무")
        
    # if click open button, open file dialog
    @pyqtSlot()
    def open_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        print("open file")
        input_file_path = fname[0]
        print(input_file_path)  
        # if get fname[0], write fname[0] to textedit
        self.lbl.setText(input_file_path)
        DataLoader(input_file_path)
        return input_file_path

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
        self.show()
    
    @pyqtSlot()
    def graph_viewer(self):
        from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
        from matplotlib.figure import Figure
        import matplotlib.pyplot as plt
        
        # get json
        json_path = self.lbl.text() + '/' + self.lbl.text().split('/')[-1] + '.json'
        print("json path :", json_path)
        
        # read json, get 10 frames traj_info value
        with open(json_path, 'r')  as f_json:
            json_data = json.load(f_json)
            trajectory_set = json_data['traj_info']
            print("trajectory_set :", trajectory_set)
            # get 10 frames traj_info value
            for i in range(10):
                traj_info = trajectory_set[i]
                print("traj_info :", traj_info)
                
            
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = test_app()
    win.show()
    app.exec_()
    