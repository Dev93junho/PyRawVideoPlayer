"""
1. get data file path
2. convert binary to numpy array per 10 frames
3. print 10 frame's trajectory
4. if get update request, windowing to next 10 frames trajectory
"""

import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import numpy as np
import json

graph_path = '/Users/shinjunho/workspace/AirTouch/test_data/0101_20220214135700_0001_00/0101_20220214135700_0001_00.json' # D2107

class SnaptoCursor(object):
    def __init__(self, ax, x, y):
        self.ax = ax
        self.ly = ax.axvline(color='k', alpha=0.2)  # the vert line
        self.marker, = ax.plot([0],[0], marker="o", color="crimson", zorder=3) 
        self.x = x
        self.y = y
        self.txt = ax.text(0.7, 0.9, '')

    def mouse_move(self, event):
        if not event.inaxes: return
        x, y = event.xdata, event.ydata
        indx = np.searchsorted(self.x, [x])[0] # find index of x
        x = self.x[indx]
        y = self.y[indx]
        self.ly.set_xdata(x)
        self.marker.set_data([x],[y])
        self.txt.set_text('x=%1.2f, y=%1.2f' % (x, y))
        self.txt.set_position((x,y))
        self.ax.figure.canvas.draw_idle()

    def plot_graph(path):
        # read json file and plot traj_info row 
        with open(path, 'r') as f:
            data = json.load(f)
            traj_info = data['traj_info']
            x = []
            y = []
            for i in range(len(traj_info)):
                x.append(traj_info[i]['x'])
                y.append(traj_info[i]['y'])
            fig, ax = plt.subplots()
            ax.plot(x, y, 'o', ms=3)
            snap_cursor = SnaptoCursor(ax, x, y)
            fig.canvas.mpl_connect('motion_notify_event', snap_cursor.mouse_move)
            plt.show()
            
            
            
        
SnaptoCursor.plot_graph(graph_path)

