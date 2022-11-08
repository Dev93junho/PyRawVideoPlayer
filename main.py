import sys, os
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import json

from engine.DataLoader import DataLoader
import engine.AutoLabel as albl

class AirNote(QWidget):
    global root
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setLayout(self.layout)
        self.setGeometry(200, 200, 500, 800)

    def initUI(self):
        # self.btn_file_load = QPushButton("Load")
        # self.btn_file_load.clicked.connect(self.open_file)        
        # # self.btn_draw_graph = QPushButton("DRAW Graph")
        # self.btn_draw_graph.clicked.connect(self.draw_graph)
        # self.btn_update_data = QPushButton("Update")
        # self.btn_update_data.clicked.connect(self.image_viewer)
        # self.btn_prev_data = QPushButton("Prev")
        # self.btn_prev_data.clicked.connect(self.prev_frame)
        # self.btn_next_frame = QPushButton("next")
        # self.btn_next_frame.clicked.connect(self.next_frame)
        
        # frame Layout
        img_sample = QPixmap('./static/init_black.png')
        self.frm = QLabel(self)
        self.frm.setGeometry(18, 25, 640, 480)
        self.frm.setPixmap(img_sample)
        
        # graph layout        
        self.fig = plt.Figure()
        self.graph = FigureCanvas(self.fig)
        self.graph.setGeometry(18, 900, 400, 100)
        
        # canvas layout
        canvasLayout = QVBoxLayout()
        canvasLayout.addWidget(self.frm)
        canvasLayout.addWidget(self.graph)

        # button Layout
        # btnLayout = QVBoxLayout()
        # btnLayout.addWidget(self.btn_file_load)
        # btnLayout.addWidget(self.btn_draw_graph)
        # btnLayout.addWidget(self.btn_update_data)
        # btnLayout.addWidget(self.btn_prev_data)
        # btnLayout.addWidget(self.btn_next_frame)
        # btnLayout.addStretch(1)

        # merge layout
        self.layout = QHBoxLayout()
        self.layout.addLayout(canvasLayout)
        # self.layout.addLayout(btnLayout)        

    def open_file(self):
        global root, frame
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        root = fname[0]
        DataLoader(root)
        frame = 0
        print("current frame : ", frame)
        # self.draw_graph()
        
    def draw_graph(self):
        global root, frame
        
        # get json
        root = root.replace('\\', '/')
        splited_path = os.path.dirname(root)
        data_name = root.split('/')[-1].split('.')[0]
        json_path = splited_path + '/' + data_name + '/' + data_name + '.json'
        ax = self.fig.add_subplot(1,1,1)  
        
        # draw axis
        with open(json_path, 'r') as f_json:
            data = json.load(f_json)
            m_x = []
            m_y = []
            m_z = []
            f_x = []
            f_y = []
            f_z = []
            for frm in range(len(data)):
                m_x.append(data[frm].get('traj')[0])
                m_y.append(data[frm].get('traj')[1])
                m_z.append(data[frm].get('traj')[2])
                f_x.append(data[frm].get('traj')[2])
                f_y.append(data[frm].get('traj')[2])
                f_z.append(data[frm].get('traj')[2])
                
        ax_t = np.linspace(0, 10, 10)

        ax.plot(ax_t, m_z[frame : frame + 10])
        self.graph.draw() 

    def image_viewer(self):
        global root, frame
        # get json
        root = root.replace('\\', '/')
        splited_path = os.path.dirname(root)
        data_name = root.split('/')[-1].split('.')[0]
        img_path = splited_path + '/' + data_name + '/img/' + data_name + '_' + str(frame) + '.png'
        if os.path.isfile(img_path):
            img_sample = QPixmap(img_path)
            self.frm.setPixmap(img_sample)
            print("image updated")       

    def next_frame(self):
        global frame
        if frame == 990:
            print("last frame")
        else:
            self.fig.clear()
            frame = frame + 1
            print("current frame : ", frame)
            self.image_viewer()
            self.draw_graph() # redraw graph
    
    def prev_frame(self):
        global frame
        if frame == 0:
            print("Can't go back, Here is First Frame")
        else:
            self.fig.clear()
            frame = frame - 1
            print("current frame : ", frame)
            self.image_viewer()
            self.draw_graph() # redraw graph
            
    def label_move_state(self, value):
        global root, frame
        # get json
        root = root.replace('\\', '/')
        splited_path = os.path.dirname(root)
        data_name = root.split('/')[-1].split('.')[0]
        json_path = splited_path + '/' + data_name + '/' + data_name + '.json'
        albl.update_json(json_path, frame, "state", value)
        
    def label_detail_motion(self, value):
        global root, frame
        # get json
        root = root.replace('\\', '/')
        splited_path = os.path.dirname(root)
        data_name = root.split('/')[-1].split('.')[0]
        json_path = splited_path + '/' + data_name + '/' + data_name + '.json'
        albl.update_json(json_path, frame, "label", value)
        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Left:
            self.prev_frame()
        elif e.key() == Qt.Key_Right:
            self.next_frame()
        elif e.key() == Qt.Key_Space: 
            # set the move True or False
            self.draw_graph()
            self.image_viewer()
        elif e.key() == Qt.Key_I: # Open Inventory
            self.open_file()
        if e.key() == Qt.Key_0:
            self.label_detail_motion(0)
        if e.key() == Qt.Key_1:            
            self.label_detail_motion(1)
            print("marked as down")
        if e.key() == Qt.Key_2:
            self.label_detail_motion(2)
            print("marked as click")
        if e.key() == Qt.Key_3:
            self.label_detail_motion(3)
            print("marked as up")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    airnote = AirNote()
    airnote.show()
    app.exec_()