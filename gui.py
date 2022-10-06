from tkinter import *
from PIL import ImageTk, Image
from img_read_frame import imgfile_read_frame

root = Tk()
root.title('사진불러오기')
root.geometry('800x600')

path = '/Volumes/SJH/DataStore/click/0101_20220214135700_0001_00.img'


# plot image
img = ImageTk.PhotoImage(imgfile_read_frame(path))
label = Label(image=img)
label.pack()
 
quit = Button(root, text='종료하기', command=root.quit)
quit.pack()
 
root.mainloop()