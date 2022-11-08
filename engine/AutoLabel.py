import json

def read_json(json_data_path):
   with open(json_data_path, 'r') as f:
      data = json.load(f)
      return data   
   
def update_json(path, frame_nums, idx, value):
   with open(path, 'r') as f:
      data = json.load(f)
      # print("변경 전 :",pre_data[frame_nums], pre_data[frame_nums][idx], value)
      with open(path, 'w') as f:
         data[frame_nums][idx] = value
         json.dump(data, f, indent=4)
         # print("변경 후 :",pre_data[frame_nums], pre_data[frame_nums][idx], value)
         return data

def delete_json(path, idx):
   with open(path, 'r') as f:
      pre_data = json.load(f)
      suf_data = pre_data[idx] = None
      return suf_data


