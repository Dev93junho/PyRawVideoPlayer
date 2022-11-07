import sys, os
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QObject, pyqtSignal, pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import json
from pynput import keyboard

from engine.DataLoader import DataLoader
from engine.interactive_graph import SnaptoCursor
import engine.AutoLabel as albl

class MyWindow(QWidget):
    global root
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setLayout(self.layout)
        self.setGeometry(200, 200, 500, 800)

    def initUI(self):
        self.btn_draw_graph = QPushButton("DRAW Graph")
        self.btn_draw_graph.clicked.connect(self.btnClicked)
        self.btn_file_load = QPushButton("Load Data")
        self.btn_file_load.clicked.connect(self.open_file)
        self.btn_update_data = QPushButton("Update Data")
        self.btn_update_data.clicked.connect(self.image_viewer)
        self.btn_label_data = QPushButton("Label Data")
        self.btn_label_data.clicked.connect(self.label_data)
        
        # frame Layout
        img_sample = QPixmap('/Users/shinjunho/workspace/AirTouch/test_data/0101_20220214135700_0001_00/img/0101_20220214135700_0001_00_0.png')
        self.frm = QLabel(self)
        self.frm.setGeometry(18, 25, 640, 480)
        self.frm.setPixmap(img_sample)
        
        # graph layout        
        self.fig = plt.Figure()
        self.graph = FigureCanvas(self.fig)
        self.graph.setGeometry(18, 700, 400, 100)
        
        # canvas layout
        canvasLayout = QVBoxLayout()
        canvasLayout.addWidget(self.frm)
        # canvasLayout.addWidget(self.Seqfrm)
        canvasLayout.addWidget(self.graph)

        # button Layout
        btnLayout = QHBoxLayout()
        btnLayout.addWidget(self.btn_file_load)
        btnLayout.addWidget(self.btn_draw_graph)
        btnLayout.addWidget(self.btn_update_data)
        btnLayout.addWidget(self.btn_label_data)
        btnLayout.addStretch(1)

        # merge layout
        self.layout = QVBoxLayout()
        self.layout.addLayout(btnLayout)
        self.layout.addLayout(canvasLayout)

    def btnClicked(self):
        global root
        # get json
        splited_path = os.path.dirname(root)
        data_name = root.split('/')[-1].split('.')[0] or root.split('\\')[-1].split('.')[0] 
        json_path = splited_path + '/' + data_name + '/' + data_name + '.json'
        
        # SnaptoCursor(self.fig, self.graph, json_path)
        
        ax = self.fig.add_subplot(1,1,1)  # fig를 1행 1칸으로 나누어 1칸안에 넣어줍니다      
        
        # 그래프의 축을 그려넣습니다.
        with open(json_path, 'r') as f_json:
            data = json.load(f_json)
            traj_info = data
            y = []
            z = []
            
            for frm in range(len(traj_info)):
                y.append(traj_info[frm].get('traj')[1])
                z.append(traj_info[frm].get('traj')[2])
                
        ax_t = np.linspace(0, 10, 10)
        # ax.plot(ax_t, z, 'r')
        for i in range(len(z)):
            i = 0
            ax.plot(ax_t, z[i : i + 10])
            # if press space bar, move to next 1 frames
            # if event.key() == Qt.Key_Space:
            #     ax.clear()
            #     i += 1
 
        self.graph.draw() 
                
    def open_file(self):
        global root
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        root = fname[0]
        DataLoader(root)
        
    def image_viewer(self):
        global root
        # get json
        splited_path = os.path.dirname(root)
        data_name = root.split('/')[-1].split('.')[0] or root.split('\\')[-1].split('.')[0] 
        img_path = splited_path + '/' + data_name + '/img/' + data_name + '_' + str(0) + '.png'
        if os.path.isfile(img_path):
            img_sample = QPixmap(img_path)
            self.frm.setPixmap(img_sample)
            print("image updated")       

    def label_data(self):
        global root
        # get json
        splited_path = os.path.dirname(root)
        root = root.replace('\\', '/')
        data_name = root.split('/')[-1].split('.')[0] or root.split('\\')[-1].split('.')[0] 
        json_path = splited_path + '/' + data_name + '/' + data_name + '.json'
        
        albl.update_json(json_path)#, 0, "label", 2)
        print("완료!")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()