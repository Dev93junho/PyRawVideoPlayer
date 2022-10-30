"""
@ Process
1. Load PNG in img folder
2. if click the play button, stream 10 png images
3. if click the stop button, stop streaming
"""

import os
from PIL import Image
import numpy as np

class Stream:
    def __init__(self):
        super().__init__()
        self.read_pngs()
        self.stream()
        
    def read_pngs(self):
        # read img folder
        for png in os.listdir('img'):
            if png.endswith('.png'):
                self.img = Image.open(png)
                
                return self.img
    
    # binary to float
    def tck2traj(self):
        data = np.fromfile(self.get_tck(), dtype=np.float32)
        data = data.reshape(1000, 7)
        min_x = data[:, 0]
        min_y = data[:, 1]
        min_z = data[:, 2]
        fist_x = data[:, 3]
        fist_y = data[:, 4]
        fist_z = data[:, 5]
        label = data[:, 6]
        return min_x, min_y, min_z, fist_x, fist_y, fist_z, label
    
    @staticmethod
    def stream_png(self):
        # if signal is true, stream next 10 png images
        if self.signal is True:
            for i in range(10):
                self.img = self.read_pngs()
                print(self.img)
                
        # if signal is false, stop streaming
        elif self.signal is False:
            pass
        
        # if signal is none, pass
        elif self.signal is None:
            pass

    @staticmethod
    def stream_traj(self):
        # if signal is true, stream next 10 frames trajectory
        if self.signal is True:
            for i in range(10):
                self.min_x, self.min_y, self.min_z, self.fist_x, self.fist_y, self.fist_z, self.label = self.tck2traj()
                print(self.min_x, self.min_y, self.min_z, self.fist_x, self.fist_y, self.fist_z, self.label)
                
        # if signal is false, stop streaming
        elif self.signal is False:
            pass
        
        # if signal is none, pass
        elif self.signal is None:
            pass
    
if __name__ == '__main__':
    Stream()