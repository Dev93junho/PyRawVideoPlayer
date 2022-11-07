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
import json
import pandas as pd

time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") # get current time

class DataLoader:
    def __init__(self, __file__):
        super().__init__()
        # parse data  path
        # self.root = self.argParse(__file__)
        abs_data_path = os.path.abspath(__file__) 
        splited_path = os.path.dirname(__file__)
        data_name = abs_data_path.split('/')[-1].split('.')[0] or abs_data_path.split('\\')[-1].split('.')[0] 
        print("디렉토리 경로 : ", splited_path,"\n","파일(폴더)명 : ", data_name) # print data path & folder name
               
        # if img folder not exist
        if os.path.exists(splited_path + '/' + data_name + '/img'):
            return 
        if not os.path.isdir(splited_path + '/' + data_name):
            print("데이터 폴더가 존재하지 않습니다. 데이터 폴더를 생성합니다.")
            
            os.mkdir(splited_path + '/' + data_name) # create img folder
            shutil.copyfile(splited_path + '/' + data_name + '.tck', splited_path + '/' + data_name + '/' + data_name + '.tck')
            
            new_data_path = splited_path + '/' + data_name  
            new_tck_path = splited_path + '/' + data_name + '/' + data_name + '.tck' # get tck file path
            
            
            if os.path.exists(new_data_path + '/img'):
                return 
            else:
                os.mkdir(new_data_path + '/' + 'img') # create img folder
                new_img_path = new_data_path + '/' + 'img' # get img folder path
            
                # # save png file to img folder from img file
                img_root = splited_path + '/' + data_name + '.img' # get img file path
                
                raw_image = np.fromfile(img_root, dtype = np.uint8, count = 640*480)
                for i in range(0, len(raw_image), 640*480):
                    img = raw_image[i:i+640*480].reshape(480, 640)
                    img = Image.fromarray(img)
                    self.imgfile_read_frame(img_root, new_img_path) # read img file 
                    print("이미지 파일을 저장합니다.")
                    img.save(new_img_path + '/' + data_name + '_' + str(i // (640*480)) + '.png')
                    
                
                
            # savd json
            trajectory_set = self.tck_to_trj(new_tck_path)[0] # convert tck to trj
            label_set = self.tck_to_trj(new_tck_path)[1] # convert tck to trj
            
            # convert numpy array to float
            trajectory_set_convert = trajectory_set.tolist() # convert numpy array to float
            label_set_convert = label_set.tolist() # convert numpy array to float
            self.create_json(new_data_path, trajectory_set_convert, label_set_convert, data_name) 
        return new_img_path, 
            
    # uint8 to PIL Image
    def imgfile_read_frame(self, bin_path, img_folder):
        imghdr = np.fromfile(bin_path, dtype=np.int32, count=2)
        if len(imghdr) < 2: return None
        w, h = imghdr
        if w * h <= 0: return None
        img = np.fromfile(bin_path, dtype=np.int16, count=w*h)
        if len(img) < w * h:
            return None
        
        img = Image.fromarray(img.reshape(h, w)) 
        img = img.convert('RGB')
        return img  

    # iterable create in json file
    def create_json(self, data_path, traj_data_path, label, filename):
        # create json array per frame
        make_json = []
        with open(data_path + '/' + filename + '.json', 'w') as f:
            for i in range (len(traj_data_path)):
                make_json.append({
                        # pandas dataframe to json
                        "frame" : filename + "_" + str(i) + ".png",
                        "traj" : traj_data_path[i],
                        "state" : None,
                        "label" : label[i],
                })
            # save json file to data folder
            result = json.dump(make_json, f, indent=4) # save json file to data folder
        return result
        
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
    
    def tck_to_trj(self, tck_path):
        # read tck file
        raw = np.fromfile(tck_path, dtype=np.float32)
        trj_set = raw.reshape(-1, 7)[:, 0:6] # get trajectory data
        lbl_set = raw.reshape(-1, 7)[:, -1] # get label data
        return trj_set, lbl_set 
    
if __name__ == '__main__':
    # class instance
    dataloader = DataLoader(__file__)
    
