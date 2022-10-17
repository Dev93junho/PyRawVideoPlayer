import sys, os
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread, QObject, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
# from pyqtgraph import PlotWidget, plot
# import pyqtgraph as pg 
# from engine import img_read_frame, data_struct
import numpy as np

from PyQt5 import QtWidgets, QtCore, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

# Window Size
WIDTH = 1024
HEIGHT = 768

# uic.loadUiType('./ui/main.ui')

class ImgViewer(QtWidgets.QWidget):
    # png sequence player
    def __init__(self, parent=None):
        super(ImgViewer, self).__init__(parent)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        # self.toolbar = NavigationToolbar(self.canvas, self)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.axis('off')
        self.ax.imshow(np.zeros((480, 640, 3)))
        layout = QtWidgets.QVBoxLayout()
        # layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.show()

    def update_figure(self, img):
        self.ax.clear()
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.axis('off')
        self.ax.imshow(img)
        self.canvas.draw()
        
class SequenceViewer(QtWidgets.QWidget):
    pass

class PlotViewer(QtWidgets.QWidget):
    
    doubleClickAction = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        super(PlotViewer, self).__init__(parent)

        self.figure = plt.figure(figsize=(3, 1)) # w, h
        self.figureCanvas = FigureCanvas(self.figure)
        # self.navigationToolbar = NavigationToolbar(self.figureCanvas, self)

        # create main layout
        layout = QtWidgets.QVBoxLayout()
        # layout.addWidget(self.navigationToolbar)
        layout.addWidget(self.figureCanvas)
        self.setLayout(layout)

        # create an axis
        x = range(0, 10)
        y = range(0, 20, 2)
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)

        # show canvas
        self.figureCanvas.show()

class EventHandle(QtWidgets.QWidget):
        def ShortcutKeyOps(self):
            # ctrl+ s : save
            if self.key == Qt.Key_S:
                if self.modifiers == Qt.ControlModifier:
                    print('save')
                    self.save()
            
            # ctrl + w : close
            if self.key == Qt.Key_W:
                if self.modifiers == Qt.ControlModifier:
                    print('exit')
                    self.exit()



class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setGeometry(300, 300, WIDTH, HEIGHT) # x, y, width, height
        self.setWindowTitle('Touch Annotation') 
        # self.ImageOps = ImgViewer(self)
        # self.GraphOps = PlotViewer(self)
        # self.show()
        
        # grid layout with 3 rows and 3 columns
        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.ImageOps, 0, 0, 1, 1)
        grid.addWidget(self.GraphOps, 0, 1, 1, 1)
        self.setLayout(grid)
        
        
    def DataOps(self):
        pass
    
    def ImageOps(self):
        ImgViewer = ImgViewer()
        # SeqViewer = SequenceViewer()
        
    def GraphOps(self):
        PlotViewer = PlotViewer()
        

if __name__ == '__main__':
    """
    app = QApplication(sys.argv) will go wrong.
    """
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
        
    player = MyApp()
    player.show()
    
    """
    sys.exit(app.exec_()) will go wrong.
    """
    app.exec_()
