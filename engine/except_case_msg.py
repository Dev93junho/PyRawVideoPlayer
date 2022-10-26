import os

# check the exist folder named 'img'
def exception_case_msg(path):
    if not os.path.exists(os.path.join(path, 'img')) and os.path.exists(os.path.join(path, '*.img')):
        msg = 'Need to extract the dataset first. Please wait...'
        return msg
    elif not os.path.exists(os.path.join(path, 'img')) and not os.path.exists(os.path.join(path, '*.img')):
        msg = 'Image Dataset not found. Please check if there is any valid data.'
        return msg
    elif not os.path.exists(os.path.join(path, '*.tck')):
        msg = 'Tick file not found. Please check if there is any valid data.'
        return msg
    else:
        # load 
        msg = 'Loaded file!'
        return msg
        