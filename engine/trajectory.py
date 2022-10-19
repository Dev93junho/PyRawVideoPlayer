import numpy as np

class Plot_Trajectory():
    def __init__(self):
        super.__init__()

    # get tck file dir
    def get_tck(self):
        pass
    
    # binary to float
    def decode_tck(self):
        data = np.fromfile(self.get_tck(), dtype=np.float32)
        data = data.reshape(1000, 7)
        min_x = data[:, 0]
        min_y = data[:, 1]
        min_z = data[:, 2]
        fist_x = data[:, 3]
        fist_y = data[:, 4]
        fist_z = data[:, 5]
        label = data[:, 6]
        return min_x, min_y, min_z, fist_x, fist_y, fist_z, label
        
    
        
    
    