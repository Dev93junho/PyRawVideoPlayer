"""
@ Data Loader 
1. get data folder / file path
2. read data folder / file convert to folder
3. create & save json
4. if find editorial data from main.py, then load json

@ Author : Junho Shin, 2022.10
"""
import os, shutil
import datetime
import numpy as np
from PIL import Image
import argparse

time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

class DataLoader:
    def __init__(self, __file__):
        super().__init__()
        self.imgfile_read_frame()
        self.MainOps()
        self.argParse()
        
    # uint8 to PIL Image
    def imgfile_read_frame(self):
        imghdr = np.fromfile(__file__, dtype=np.int32, count=2)
        if len(imghdr) < 2: return None
        w, h = imghdr
        if w * h <= 0: return None
        img = np.fromfile(__file__, dtype=np.int16, count=w*h)
        if len(img) < w * h:
            return None
        
        img = Image.fromarray(img.reshape(h, w))
        return img  


    def MainOps(root):
        abs_data_path = os.path.abspath(root) # data path is current path
        splited_path = os.path.dirname(root)
        data_name = abs_data_path.split('/')[-1].split('.')[0] # folder name is current path
        print(splited_path, data_name) # print data path & folder name
        
        
        # if img folder exists, load the first image
        if os.path.isdir(os.path.join(data_name + '/img/')): 
            img_data_path = os.path.join(data_name, 'img/')
            traj_data_path = os.path.join(data_name, '*.tck')
            return img_data_path, traj_data_path
        else:
            new_data_path = os.mkdir(os.path.join(splited_path, data_name)) # if not, make new data folder
            org_new_data = os.mkdir(os.path.join(splited_path, data_name + '/img/')) and shutil.move(splited_path + data_name + ".tck", splited_path + data_name)
            
            # if json folder exists, load the first json file. if not, create json folder
            # json_data_path = os.path.join(splited_path + data_name + '.json') if os.path.exists(os.path.join(splited_path + data_name + '.json')) else os.mkdir(os.path.join(splited_path + data_name + '.json'))
            return new_data_path, org_new_data
        
        
    # define argument parser
    def argParse(self):
        self.parser = argparse.ArgumentParser(description='input data path')
        self.parser.add_argument('--data_path', required=True, help='input data path')
        
        # 입력 인자 args에 저장
        self.args = self.parser.parse_args()
        
        # 입력 인자값 출력
        print(self.args.data_path)

if __name__ == '__main__':
    # class instance
    dataloader = DataLoader(__file__)
    dataloader.argParse()
