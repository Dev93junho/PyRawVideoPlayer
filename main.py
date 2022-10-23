import sys, os
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, 
                             QTextEdit, QPushButton, QFileDialog, QProgressBar, QMessageBox,
                             QCheckBox)
from pyqtgraph import PlotWidget, plot

from engine import DataLoader

VALID_FORMAT = ('.JPG', '.JPEG', '.PNG')
# VALID_FORMAT = ('.BMP', '.GIF', '.JPG', '.JPEG', '.PNG', '.PBM', '.PGM', '.PPM', '.TIFF', '.XBM')  # Image formats supported by Qt

class DataOps(QWidget, QThread):
    def __init__(self):
        super().__init__()
        self.load_data()
        
    def load_data(self):
        # find the data folder path
        self.data_path = os.path.dirname(os.path.abspath(__file__))

        try:
        # if img folder exists, load the first image
        # but if *.img file exists, make new img folder and decompress the *.img file in it
            self.img_data_path = os.path.join(self.data_path, 'img/')
            self.traj_data_path = os.path.join(self.data_path, '*.tck')    
        except:
            print ('error')
        
class ImageOps(QWidget):
    def __init__(self):
        super().__init__()
        self.load_Image()
        self.width()
        self.height()
        
    def load_Image(self):
        QPixmap('./ui/images.jpeg').scaled(self.width(), self.height())
    
class TrajOps(QThread):
    def __init__(self):
        super().__init__()
        self.load_Traj()
        
    def load_Traj(self):
        pass

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.database = DataOps()
        self.Img_Viewer = ImageOps()
        self.Plot_Viewer = TrajOps()

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

        grid.addWidget(self.line_load_data, 0, 0)
        grid.addWidget(self.btn_load, 0, 1)
        grid.addWidget(self.Img_Viewer, 1, 0)
        # grid.addWidget(self.Plot_Viewer, 2, 0)

        # 패널 요소 정의 및 출력
        self.setWindowTitle('AirTouch-Annotation')
        self.setGeometry(100, 100, 1440, 700)
        self.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())