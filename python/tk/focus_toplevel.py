# focus_toplevel.py
from tkinter import *
root = Tk()

second_window = Toplevel()
second_window.title('Second window')

# Focus on window
second_window.focus_force()

root.mainloop()