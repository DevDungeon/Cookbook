# modify_widget.py
from tkinter import *
root = Tk()

# Create a plain label that says "Hello, world!"
label = Label(root, text='Hello, world!')
label.pack()

# Modify a widget with config(). Widgets can be modified after packing.
label.config(foreground='yellow', background='black', text='Updated text!')    

root.mainloop()