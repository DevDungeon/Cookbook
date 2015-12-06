# display_text.py
from tkinter import *
root = Tk()

# Create a label as a child of root window
my_text = Label(root, text='Hello, world!')
my_text.pack()

root.mainloop()