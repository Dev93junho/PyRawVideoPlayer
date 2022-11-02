from signal import signal
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

import sys, os

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
        
        QPushButton('test', self).clicked.connect(self.open_file)
        self.show()
    
    @pyqtSlot()
    def signal_emmitted(self):
        print("signal emmitted")
        
    # if click open button, open file dialog
    @pyqtSlot()
    def open_file(self):
        print("open file")
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        print(fname[0])
        
        # draw graph
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = test_app()
    win.show()
    app.exec_()
    