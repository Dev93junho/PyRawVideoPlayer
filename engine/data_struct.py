import json
import datetime
from engine import *
from engine import img_read_frame

time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def sequence_json(data):
    pass

def frame_json(data):
    
    info_dict = {
        "seq" : None, # need to be changed
        "create_time" : f"{time}",
        "edit_time" : f"{time}",
        "img" : img_read_frame(data),#.tolist(),
        "nums" : None, # need to be changed
        "status" :None, # need to be changed
    }
    return info_dict

