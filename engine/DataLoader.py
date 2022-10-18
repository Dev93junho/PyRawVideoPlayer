import os, sys
import datetime
import numpy as np
from PIL import Image

time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

class DataLoader():
    def __init__(self):
        self.data_path = os.path.dirname(os.path.abspath(__file__))
        self.img_data_path = os.path.join(self.data_path, 'img/') if os.path.exists(os.path.join(self.data_path, 'img/')) else os.mkdir(os.path.join(self.data_path, 'img/'))
        self.traj_data_path = os.path.join(self.data_path, '*.tck') if os.path.exists(os.path.join(self.data_path, '*.tck')) else print('tck file is not exist')
        # self.label_data_path = os.path.join(self.data_path, '*.label')
        # create dict file named load folder
        
        
        self.img = self.img_data_path
        self.traj = self.traj_data_path
        # self.label = self.label_data_path
        
# uint8 to PIL Image
def imgfile_read_frame(self, imgfile):
    imghdr = np.fromfile(imgfile, dtype=np.int32, count=2)
    if len(imghdr) < 2: return None
    w, h = imghdr
    if w * h <= 0: return None
    img = np.fromfile(imgfile, dtype=np.int16, count=w*h)
    if len(img) < w * h:
        return None
    
    img = Image.fromarray(img.reshape(h, w))
    # img = np.array(img)
    return img  

def export_to_dict(self, data):
    info_dict = {
        "seq" : None, # need to be changed
        "create_time" : f"{time}",
        "edit_time" : f"{time}",
        "img" : imgfile_read_frame(data),#.tolist(),
        "nums" : None, # need to be changed
        "status" :None, # need to be changed
    }
    return info_dict

