import numpy as np
from PIL import ImageTk, Image

# uint8 to PIL Image
def imgfile_read_frame(imgfile):
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