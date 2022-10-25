"""
data create, read, edit, delete operations
"""
import json
import datetime
import engine.DataLoader

time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# "create_time" : f"{time}",
# "edit_time" : f"{time}",


# iterable create in json file
def Create(img_data_path, traj_data_path, filename):
    # create json array per frame
    for i in range(len(img_data_path)):
        filename = {
            'frame_id': i,
            'sequence' : None, # need to be changed
            'img_path': img_data_path[i],
            'traj_info': traj_data_path[i],
            "status" :None, # need to be changed
        },
    return json.dumps(filename)
    
def Read(json_data_path):
    # find json file in data root
    with open(json_data_path, 'r') as f:
        json_data = json.load(f)
        return json_data

def Update(path, idx, value):
    with open(path, 'w+') as f:
        pre_data = json.load(f)
        suf_data = pre_data[idx] = value
        return suf_data

def Delete(path, idx):
    with open(path, 'w+') as f:
        pre_data = json.load(f)
        suf_data = pre_data[idx] = None
        return suf_data
