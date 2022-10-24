"""
@ Process
1. Load PNG in img folder
2. if click the play button, stream 10 png images
3. if click the stop button, stop streaming
"""

import os, sys
from PIL import Image
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
                # self.img.show()
                return self.img
            
    def stream(self):
        pass
if __name__ == '__main__':
    Stream()