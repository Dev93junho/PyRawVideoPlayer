"""
data create, read, edit, delete operations
"""
import json
import datetime

time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# iterable create in json file
def Create(self, json_data_path, img_data_path, traj_data_path):
    # create json array per frame
    for i in range(len(img_data_path)):
        data = {
            'sequence' : None, # need to be changed
            'img_path': img_data_path[i],
            'traj_path': traj_data_path[i],
            "create_time" : f"{time}",
            "edit_time" : f"{time}",
            "nums" : int(i),
            "status" :None, # need to be changed
        }
        
    return json.dumps(data)
    
def Read():
    pass

def Update():
    pass

def Delete():
    pass
