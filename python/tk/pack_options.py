# pack_options.py
from tkinter import *
root = Tk()

label1 = Label(root, text='Yellow!', background='yellow')
label2 = Label(root, text='Orange?', background='orange')

# Some of the packing options:
# - fill: tells the widget to expand to take up any extra space (X, Y, or BOTH)
# - padx/pady: outter padding
# - ipadx/ipady: inner padding
# - side: which side to stack from. Default is TOP (to bottom)

label1.pack(fill=Y, padx=25, ipady=15, side=RIGHT)  # Pack from right to left
label2.pack(fill=Y, padx=25, ipady=15, side=RIGHT)

root.mainloop()