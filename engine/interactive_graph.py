import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import numpy as np


graph_path = '/Volumes/SJH/DataStore/click/0101_20220214135917_0004_00.tck' # D2107

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
        indx = np.searchsorted(self.x, [x])[0]
        x = self.x[indx]
        y = self.y[indx]
        self.ly.set_xdata(x)
        self.marker.set_data([x],[y])
        self.txt.set_text('x=%1.2f, y=%1.2f' % (x, y))
        self.txt.set_position((x,y))
        self.ax.figure.canvas.draw_idle()

    def plot_graph(path):
        data = np.fromfile(path, dtype=np.float32)
        data = data.reshape(1000, 7)
        return data

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*2*np.pi*t)
fig, ax = plt.subplots()

#cursor = Cursor(ax)
cursor = SnaptoCursor(ax, t, s)
cid =  plt.connect('motion_notify_event', cursor.mouse_move)

ax.plot(t, s,)
plt.axis([0, 1, -1, 1])
plt.show()