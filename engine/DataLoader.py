"""
@ Author : Junho Shin 
@ Last Update : 2022.11
"""
import os, shutil
import datetime
import numpy as np
from PIL import Image
import json

# time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") # get current time

class DataLoader:
    def __init__(self, __file__):
        super().__init__()
        abs_data_path = os.path.abspath(__file__) 
        abs_data_path = abs_data_path.replace('\\', '/')
        
        splited_path = os.path.dirname(__file__)
        data_name = abs_data_path.split('/')[-1].split('.')[0]
        print("디렉토리 경로 : ", splited_path,"\n","파일(폴더)명 : ", data_name) # print data path & folder name
        
        self.create_folder(splited_path, data_name)
        print("데이터 구성이 완료되었습니다.")
               
    def create_folder(self, splited_path, data_name):
        # if img folder not exist
        if os.path.exists(splited_path + '/' + data_name + '/img'):
            return None
        if not os.path.isdir(splited_path + '/' + data_name):
            print("데이터 폴더가 존재하지 않습니다. 데이터 폴더를 생성합니다.")
            os.mkdir(splited_path + '/' + data_name) # create img folder
            shutil.copyfile(splited_path + '/' + data_name + '.tck', splited_path + '/' + data_name + '/' + data_name + '.tck') # copy tck file to data folder
            new_data_path = splited_path + '/' + data_name  
            new_tck_path = splited_path + '/' + data_name + '/' + data_name + '.tck' # get tck file path
            
            if os.path.exists(new_data_path + '/img'):
                return None
            else:
                os.mkdir(new_data_path + '/' + 'img') # create img folder
                new_img_path = new_data_path + '/' + 'img' # get img folder path
                # save png file to img folder from img file
                img_root = splited_path + '/' + data_name + '.img' # get img file path
                raw_image = np.fromfile(img_root, dtype = np.uint16)#, count = 640*480) # read img file
                print(len(raw_image))
                for i in range(0, len(raw_image), 640*480):
                    print("이미지 파일 생성 중... ", i, "/", len(raw_image))
                    if len(raw_image[i:i+640*480]) < 640*480:
                        return None
                    else:
                        img = raw_image[i:i+640*480].reshape(480, 640)
                        img = Image.fromarray(img)
                        img = img.convert('RGB')
                        self.imgfile_read_frame(img_root)
                        img.save(new_img_path + '/' + data_name + '_' + str(i // (640*480)) + '.png')
                        print(f"{i} 번째 이미지 파일을 저장합니다.")
                    print("이미지 파일 저장이 완료되었습니다.")
                        
                    trajectory_set = self.tck_to_trj(new_tck_path)[0] # convert tck to trj
                    label_set = self.tck_to_trj(new_tck_path)[1] # convert tck to trj
                    trajectory_set_convert = trajectory_set.tolist() # convert numpy array to float
                    label_set_convert = label_set.tolist() # convert numpy array to float
                    self.create_json(new_data_path, trajectory_set_convert, label_set_convert, data_name) 
                
    # uint8 to PIL Image
    def imgfile_read_frame(self, bin_path):
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
                make_json.append(
                    {
                        # pandas dataframe to json
                        "frame" : filename + "_" + str(i) + ".png",
                        "traj" : traj_data_path[i],
                        "state" : False,
                        "label" : label[i],
                }, )

            result = json.dump(make_json, f, indent=4) # save json file to data folder
        return result
        
    def tck_to_trj(self, tck_path):
        # read tck file
        raw = np.fromfile(tck_path, dtype=np.float32)
        trj_set = raw.reshape(-1, 7)[:, 0:6] # get trajectory data
        lbl_set = raw.reshape(-1, 7)[:, -1] # get label data
        return trj_set, lbl_set 
    
if __name__ == '__main__':
    # class instance
    dataloader = DataLoader(__file__)
    
