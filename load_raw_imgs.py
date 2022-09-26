import numpy as np
from PIL import Image

# load raw rgb image class
class LoadRawImgs:
    def __init__(self, img_path):#, img_size):
        self.img_path = img_path
        # self.img_size = img_size

    # 640 x 480 raw rgb image
    def show_frame(file, start, end):
        src_max_depth = 5000 # mm
        try:
            with open(file, 'rb+') as img: # -> automatic tch finder
                # save_bin = open( savefile +".img", "wb") -> save raw image
                for i in range(start - 1, end):
                    try:
                        img_size = np.fromfile(img, dtype='int', count=2)#, sep='', offset=offset) # 2*4byte
                        shape = int((img_size[0]*img_size[1]))
                        print(shape)
                        imgs = np.fromfile(img, dtype='uint16', count=shape)#, sep='', offset=offset) # 640*480*2byte
                        print(len(imgs))

                        # save_bin.write(bytearray(img_size))
                        newFileByteArray = bytearray(img)
                        # save_bin.write(newFileByteArray)
                        return newFileByteArray
                    
                    except:
                        err_msg = str("Do not coincide frame length with input value")
                        return err_msg
        except:
            err_msg = str("Can not open file")
            return err_msg
        
        

if __name__ == '__main__':
    img_path = 'D://AirTouch2/Gen/DataStore/click/0101_20220214135700_0001_00.img'
    # load_raw_imgs = LoadRawImgs(img_path)
    img = LoadRawImgs.show_frame(img_path, 1, 999)
    # print(img.shape)
    print(len(img))



