# get_screen_size.py
from tkinter import *
root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print("Screen width:", screen_width)
print("Screen height:", screen_height)