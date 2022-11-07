"""

1. 요청이 들어오면
2. 요청을 받은 시점의 커서 위치와 json 파일위치를 받아온다.
3. 커서위치를 json 파일에서 찾는다
4. json 파일에서 해당하는 index의 status를 변경한다.

"""

import numpy as np
import json
import os, sys

def read_json(json_data_path):
   # find json file in data root
   file = json.loads(json.dumps(json_data_path))
   return file

def update_json(path, idx, value):
      file = json.loads(json.dumps(path))
      file[idx] = value
      return file

def delete_json(path, idx):
   with open(path, 'r+') as f:
      pre_data = json.load(f)
      suf_data = pre_data[idx] = None
      return suf_data


