import os, sys
import datetime
import numpy as np
from PIL import Image

time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

class DataLoader():
    def __init__(self):
        super().__init__()
    
    # 입력된 데이터 경로 형식 파악
    
    def valid_data_format(self, data_path):
        # 로드 경로 입력받기
        
    
        # *.img 파일형식 일 경우 파일 명과 동일한 폴더 생성
        if self.data_path == 'img':
            self.change_data_path = os.path.join(self.data_path, self.data_name)
            if not os.path.exists(self.data_path):
                os.makedirs(self.data_path)
    
        # 폴더 형식일 경우 폴더 내 구조 파악
        
        
        
            # img 폴더, tck 파일 존재 여부 확인
            # img 폴더 없을 경우 img 폴더 생성
        pass
    
    # 변경 중 로딩 메세지 출력
    
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
