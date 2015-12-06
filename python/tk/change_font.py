# change_font.py
from tkinter import *
root = Tk()

msg = Message(root, text='Hello, world!')

# Font is a tuple of (font_family, size_in_points, style_modifier_string)
msg.config(font=('times', 48, 'italic bold underline'))

msg.pack()

root.mainloop()