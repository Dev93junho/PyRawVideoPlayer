import sys, os
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QFileDialog, QProgressBar, QMessageBox)


class DataOps(QWidget, QThread):
    def __init__(self):
        super().__init__()
        self.load_data()
    
    def load_data(self):
        # find the data folder path
        self.data_path = os.path.dirname(os.path.abspath(__file__))

        try:
            self.img_data_path = os.path.join(self.data_path, 'img/')
            self.traj_data_path = os.path.join(self.data_path, '*.tck')    
        except:
            print ('error')

class ImageOps(QWidget, QThread):
    def __init__(self):
        super().__init__()
        
    def load_Image():
        pass

class TrajOps(QThread):
    def __init__(self):
        super().__init__()
        
    def load_Traj():
        pass

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.img_viewer = ImageOps()
        
        grid.addWidget(QLabel(), 0, 0)
        grid.addWidget(QPushButton('Load Data'), 0, 1)
        # grid.addWidget(QPixmap().QImages, 1, 0)
        grid.addWidget(QLineEdit(), 2, 0)
        

        self.setWindowTitle('AirTouch-Annotation')
        self.setGeometry(300, 300, 1440, 1200)
        self.show()

    def btn_load_data(self):
        pass
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())