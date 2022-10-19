import sys, os
import random
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread

from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, 
                             QAction, QPushButton, QFileDialog, QProgressBar, QMessageBox,
                             QCheckBox)

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
        self.filedialog()
        
    def filedialog(self):
        DataLoader.export_to_dict(self, DataLoader.imgfile_read_frame(self, DataLoader.img_data_path))
    
    
class ImageOps(QWidget):
    def __init__(self):
        super().__init__()
        self.ImagePlayer()
        self.ImageSeq()
        
    def ImagePlayer(self):
        pass
    
    def ImageSeq(self):
        pass
    
class MyApp(QtWidgets.QMainWindow, DataOps, ImageOps):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.database = DataOps()
        self.Img_Viewer = ImageOps()
        
        # 데이터 로드
        self.line_load_data = QLineEdit()
        self.line_load_data.setPlaceholderText('데이터 폴더 경로를 입력하세요')
        # self.line_load_data.mouseDoubleClickEvent = QFileDialog.getExistingDirectory(self, '데이터 폴더 경로를 선택하세요')
        self.btn_load = QPushButton('Load Data')
        self.btn_load.clicked.connect(self.database.load_data)
        
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
        

        # 패널 요소 정의 및 출력
        self.setWindowTitle('AirTouch-Annotation')
        self.setGeometry(300, 300, 1440, 1200)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())