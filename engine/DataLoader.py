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
    def __init__(self, root):
        # parse data path
        self.root = self.argParse()
        abs_data_path = os.path.abspath(self.root) 
        splited_path = os.path.dirname(self.root)
        data_name = abs_data_path.split('/')[-1].split('.')[0]
        print("디렉토리 경로 : ", splited_path, "파일(폴더)명 : ", data_name) # print data path & folder name
        
        # 데이터 구조화. 이미 형성되어있으면 pass
        if os.path.isdir(os.path.join(data_name + '/img/')): 
            new_img_path = os.path.join(data_name, 'img/')
            new_trj_path = os.path.join(data_name, '*.tck')
            return new_img_path, new_trj_path
        
        elif os.path.isfile(root, data_name + '.img'):
            new_data_path = os.mkdir(os.path.join(splited_path, data_name)) # if not, make new data folder
            new_img_path = os.mkdir(os.path.join(splited_path, data_name + '/img/')) # and 
            new_trj_path = shutil.copy(splited_path + data_name + f"/{data_name}.tck", new_data_path)
            return new_data_path, new_img_path, new_trj_path
            
        else:
            msg = '입력 값이 올바르지 않습니다.'
            return msg
        
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
    def create_json(img_data_path, traj_data_path, filename):
        # create json array per frame
        make_json = []
        with open(filename + '.json', 'w') as f:
            for i in range(len(img_data_path)):
                {
                    'frame_idx': i,
                    'sequence' : None, # need to be changed
                    'img_path': img_data_path[i],
                    'traj_info': traj_data_path[i],
                    'move_state' : 0, # 0 : stop, 1 : move
                    "status" :None, # need to be changed
                },
            make_json.append(dict) # append dict to json array
        return make_json
        
    def read_json(json_data_path):
        # find json file in data root
        with open(json_data_path, 'r') as f:
            json_data = json.load(f)
            return json_data

    def update_json(path, idx, value):
        with open(path, 'w+') as f:
            pre_data = json.load(f)
            suf_data = pre_data[idx] = value
            return suf_data

    def delete_json(path, idx):
        with open(path, 'w+') as f:
            pre_data = json.load(f)
            suf_data = pre_data[idx] = None
            return suf_data
            
    # define argument parser
    def argParse(self):
        self.parser = argparse.ArgumentParser(description='input data path')
        self.parser.add_argument('--data_path', default=True, help='input data path')
        self.parser.add_argument('--json_path', default=False, help='input json path')
        self.parser.add_argument('--frm_idx', default=False, help='input frame index')
        self.parser.add_argument('--idx', default=False, help='input data index')
        self.parser.add_argument('--value', default=False, help='input change value')
       
        # 입력 인자 args에 저장
        self.args = self.parser.parse_args()
        return self.args
    
if __name__ == '__main__':
    # class instance
    dataloader = DataLoader(__file__)
    dataloader.argParse()
