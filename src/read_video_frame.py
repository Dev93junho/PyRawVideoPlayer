from calendar import c
import cv2
import os

video_path = '/path/to/video'
create_folder = 'frames'

vcap = cv2.VideoCapture(video_path)
open, img = vcap.read()
count = 0


os.mkdir(create_folder, exist_ok = True)

while open:
    cv2.imwrite("frames/frame%d.jpg" % count, img)
    open, img = vcap.read()
    print("read a new frame: %d done" %count, open)
    count += 1