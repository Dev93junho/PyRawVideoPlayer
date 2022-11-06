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

# import os
# from PIL import Image
# import numpy as np

# class Stream:
#     def __init__(self):
#         super().__init__()
#         self.read_pngs()
#         self.stream()
        
#     def read_pngs(self):
#         # read img folder
#         for png in os.listdir('img'):
#             if png.endswith('.png'):
#                 self.img = Image.open(png)
                
#                 return self.img
    
#     # binary to float
#     def tck2traj(self):
#         data = np.fromfile(self.get_tck(), dtype=np.float32)
#         data = data.reshape(1000, 7)
#         min_x = data[:, 0]
#         min_y = data[:, 1]
#         min_z = data[:, 2]
#         fist_x = data[:, 3]
#         fist_y = data[:, 4]
#         fist_z = data[:, 5]
#         label = data[:, 6]
#         return min_x, min_y, min_z, fist_x, fist_y, fist_z, label
    
    
#     def stream_png(self):
#         # if pyqtsignal is true, stream next 10 png images
#         if self.signal is True:
#             for i in range(10):
#                 self.img = self.read_pngs()
#                 print(self.img)
                
#         # if signal is false, stop streaming
#         elif self.signal is False:
#             pass
        
#         # if signal is none, pass
#         elif self.signal is None:
#             pass

#     def stream_traj(self):
#         # if signal is true, stream next 10 frames trajectory
#         if self.signal is True:
#             for i in range(10):
#                 self.min_x, self.min_y, self.min_z, self.fist_x, self.fist_y, self.fist_z, self.label = self.tck2traj()
#                 print(self.min_x, self.min_y, self.min_z, self.fist_x, self.fist_y, self.fist_z, self.label)
                
#         # if signal is false, stop streaming
#         elif self.signal is False:
#             pass
        
#         # if signal is none, pass
#         elif self.signal is None:
#             pass
    
# if __name__ == '__main__':
#     Stream()
    
    
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
    