"""
@ Data Loader 
1. get data folder / file path
2. if read data file convert to folder, check data folder structure
3. create & save json
4. if find editorial data from main.py, then load json

input : data path 
output : data folder with img folder, copied tck, 

@ Author : Junho Shin, 2022.10
"""
"""
@ image update rule
1. get data file path
2. read 
3. print 10 frame's trajectory
4. if get update request, windowing to next 10 frames trajectory
"""
"""
@ trajectory update rule
1. get data file path
2. convert binary to numpy array per 10 frames
3. print 10 frame's trajectory
4. if get update request, windowing to next 10 frames trajectory
"""


import os, shutil
import datetime
import numpy as np
from PIL import Image
import argparse
import json

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

    # iterable create in json file
    def Create(img_data_path, traj_data_path, filename):
        # create json array per frame
        for i in range(len(img_data_path)):
            filename = {
                'frame_id': i,
                'sequence' : None, # need to be changed
                'img_path': img_data_path[i],
                'traj_info': traj_data_path[i],
                "status" :None, # need to be changed
            },
        return json.dumps(filename)
        
    def Read(json_data_path):
        # find json file in data root
        with open(json_data_path, 'r') as f:
            json_data = json.load(f)
            return json_data

    def Update(path, idx, value):
        with open(path, 'w+') as f:
            pre_data = json.load(f)
            suf_data = pre_data[idx] = value
            return suf_data

    def Delete(path, idx):
        with open(path, 'w+') as f:
            pre_data = json.load(f)
            suf_data = pre_data[idx] = None
            return suf_data

    def MainOps(root):
        abs_data_path = os.path.abspath(root) # data path is current path
        splited_path = os.path.dirname(root)
        data_name = abs_data_path.split('/')[-1].split('.')[0]
        print(splited_path, data_name) # print data path & folder name
        
        
        # if img folder exists, load the first image
        if os.path.isdir(os.path.join(data_name + '/img/')): 
            img_data_path = os.path.join(data_name, 'img/')
            traj_data_path = os.path.join(data_name, '*.tck')
            return img_data_path, traj_data_path
        else:
            new_data_path = os.mkdir(os.path.join(splited_path, data_name)) # if not, make new data folder
            org_new_data = os.mkdir(os.path.join(splited_path, data_name + '/img/')) # and shutil.copy(splited_path + data_name + f"/{data_name}.tck", new_data_path)
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
