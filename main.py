import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread, QObject, Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg 
from engine import img_read_frame, data_struct


WIDTH = 1024
HEIGHT = 768

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, WIDTH, HEIGHT) # x, y, width, height
        self.setWindowTitle('Touch Annotation') 
        self.img = img_read_frame() # plot png image
        self.show()
        
    def load_data(self):
        pass
    
    def Image_manager(self):
        # 1. image read with img_read_frame
        
        # 2. image show with pillow
        
        # 3. if click next button, then show next image
       pass 
    
    def Graph_manager(self):
        pass
    
    def system_ops(self):
        #  shortcut keys
        # ctrl+ s : save

        pass
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())