"""
@ Process
1. Load PNG in img folder
2. if click the play button, stream 10 png images
3. if click the stop button, stop streaming
"""

import os, sys
from PIL import Image
import numpy as np
import argparse
import threading

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
        
    def stream(self):
        pass
    
if __name__ == '__main__':
    Stream()