# display_image.py
import sys
from tkinter import *
root = Tk()

# First command line arg is image path. PNG format
img = PhotoImage(file=sys.argv[1])
my_image = Label(root, image=img)
my_image.pack()

root.mainloop()