# shrink_image.py
import sys
from tkinter import *
root = Tk()

# First command line arg is image path. PNG format
base_img = PhotoImage(file=sys.argv[1])

# Take only every 3rd pixel from x and y resulting in an image of 1/3 size
img1 = base_img.subsample(3, 3) 

# Take every pixel from x but only every other from y. Shrinks y by half
img2 = base_img.subsample(1, 2) 

base_img_label = Label(root, image=base_img)
img1_label = Label(root, image=img1)
img2_label = Label(root, image=img2)

base_img_label.pack()
img1_label.pack()
img2_label.pack()

root.mainloop()