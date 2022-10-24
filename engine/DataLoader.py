import os, sys
import datetime
import numpy as np
from PIL import Image
import argparse

time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

class DataLoader:
    def __init__(self, __file__):
        super().__init__()
        self.imgfile_read_frame()
        self.export_to_json()
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
    def export_to_json(self, json_data_path, img_data_path, traj_data_path):
        # create json array per frame
        for i in range(len(img_data_path)):
            json_data = {
                'sequence' : None, # need to be changed
                'img_path': img_data_path[i],
                'traj_path': traj_data_path[i],
                "create_time" : f"{time}",
                "edit_time" : f"{time}",
                "nums" : int(i), # need to be changed
                "status" :None, # need to be changed
            }
            
            return json_data

    # define argument parser
    def argParse(self):
        self.parser = argparse.ArgumentParser(description='input data path')
        self.parser.add_argument('--data_path', required=True, help='input data path')
        
        # 입력 인자 args에 저장
        self.args = self.parser.parse_args()
        # 입력 인자값 출력
        print(self.args.data_path)


    def MainOps(self):
        self.data_path = os.path.dirname(os.path.abspath(__file__)) # data path is current path
        self.folder_name = self.data_path.split('/')[-1] # folder name is current path
        # if img folder exists, load the first image
        if os.path.isdir(os.path.join(self.data_path, 'img/')): 
            self.img_data_path = os.path.join(self.data_path, 'img/')
            self.traj_data_path = os.path.join(self.data_path, '*.tck')
        else:
            print('img folder does not exist')
            sys.exit()
        
        # if img folder doesn't exist, create img folder 
        self.img_data_path = os.path.join(self.data_path, 'img/') if os.path.exists(os.path.join(self.data_path, 'img/')) else os.mkdir(os.path.join(self.data_path, 'img/')) and self.imgfile_read_frame('*.img', self.img_data_path)
        self.traj_data_path = os.path.join(self.data_path, '*.tck') if os.path.exists(os.path.join(self.data_path, '*.tck')) else print('tck file is not exist')
        
        # if json folder exists, load the first json file. if not, create json folder
        self.json_data_path = os.path.join(self.data_path, self.folder_name + '.json') if os.path.exists(os.path.join(self.data_path, '.json')) else os.mkdir(os.path.join(self.data_path, '.json'))
        
        #  write json file
        self.export_to_json(self, self.json_data_path, self.img_data_path, self.traj_data_path)

if __name__ == '__main__':
    # class instance
    dataloader = DataLoader(__file__)
    dataloader.argParse()
