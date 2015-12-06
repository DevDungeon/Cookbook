# set_icon_and_title.py
import sys
from tkinter import *
root = Tk()

# Image path provided as first command line arg. PNG format
root.iconphoto(root, PhotoImage(file=sys.argv[1])) 
root.title("Tkinter Test")

root.mainloop()