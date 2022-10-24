import sys, os
<<<<<<< HEAD
import random
from PyQt5 import QtWidgets
=======
from PyQt5 import QtWidgets, QtGui, QtCore, uic
>>>>>>> ef313d58c9dd8a63d067b64034d6a9b47319d103
from PyQt5.QtCore import QThread

from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, 
                             QAction, QPushButton, QFileDialog, QProgressBar, QMessageBox,
                             QCheckBox)
<<<<<<< HEAD

=======
from pyqtgraph import PlotWidget, plot
import json
>>>>>>> ef313d58c9dd8a63d067b64034d6a9b47319d103
from engine import DataLoader

#  graph library
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



VALID_FORMAT = ('.JPG', '.JPEG', '.PNG')
# VALID_FORMAT = ('.BMP', '.GIF', '.JPG', '.JPEG', '.PNG', '.PBM', '.PGM', '.PPM', '.TIFF', '.XBM')  # Image formats supported by Qt

class DataOps(QWidget, QThread):
    def __init__(self):
        super().__init__()
<<<<<<< HEAD
        self.filedialog()
=======
        self.load()
        self.update()
        
    def load(self):
        # find the data folder path
        self.data_path = os.path.dirname(os.path.abspath(__file__))

        try:
        # if img folder exists, load the first image
        # but if *.img file exists, make new img folder and decompress the *.img file in it
            self.img_data_path = os.path.join(self.data_path, 'img/')
            self.traj_data_path = os.path.join(self.data_path, '*.tck')    
        except:
            print ('error')
            
    def update(self):
        pass
>>>>>>> ef313d58c9dd8a63d067b64034d6a9b47319d103
        
    def filedialog(self):
        DataLoader.export_to_dict(self, DataLoader.imgfile_read_frame(self, DataLoader.img_data_path))
    
    
class ImageOps(QWidget):
    def __init__(self):
        super().__init__()
        self.ImagePlayer()
        self.ImageSeq()
        
    def ImagePlayer(self):
        pass
    
class TrajOps(QThread):
    def __init__(self):
        super().__init__()
    

# QMainWidow can be call  ui file
class AirNote(QtWidgets.QMainWindow):

    def __init__(self):
        super(AirNote, self).__init__()
        uic.loadUi('./ui/main.ui', self)
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.DataOps = DataOps()
        self.ImgViewer = ImageOps()
        self.PlotViewer = TrajOps()

        # 데이터 로드
        self.line_load_data = QLineEdit()
        self.line_load_data.setPlaceholderText('데이터 폴더 경로를 입력하세요')
        # self.line_load_data.mouseDoubleClickEvent = QFileDialog.getExistingDirectory(self, '데이터 폴더 경로를 선택하세요')
        self.btn_load = QPushButton('Load Data')
        # self.btn_load.clicked.connect(self.DataOps)
        
        # 그래프 요소 선택
        self.m_x_checkbox = QCheckBox('min_x')
        self.m_y_checkbox = QCheckBox('min_y')
        self.m_z_checkbox = QCheckBox('min_z')
        self.f_x_checkbox = QCheckBox('fix_x')
        self.f_y_checkbox = QCheckBox('fix_y')
        self.f_z_checkbox = QCheckBox('fix_z')
        
        
        # grid layout
        grid.addWidget(self.line_load_data, 0, 0)
        grid.addWidget(self.btn_load, 0, 1)
        grid.addWidget(self.ImgViewer, 1, 0)
        # grid.addWidget(self.Plot_Viewer, 2, 0)

        # 패널 요소 정의 및 출력
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AirNote()
    sys.exit(app.exec_())