import numpy as np
from PIL import Image

def load_image(path):
    with open(path, 'rb') as f:
        data = f.read()
        image_size = np.frombuffer(data, dtype=np.uint32, count=2)
        size = image_size[0] * image_size[1]
        
        # iterate over the image data
        for i in range (0, size, 4):
            
            image = np.frombuffer(data, dtype=np.uint16, count=size) # offset=8
            
            print(image.shape)
            
            # show image
            image = image.reshape(image_size[1], image_size[0])
            image = Image.fromarray(image)
    return image
