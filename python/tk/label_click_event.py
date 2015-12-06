# label_click_event.py
from tkinter import *
root = Tk()

# Labels do not have a command option like buttons
# but you can manually attach the click event to a callback
label = Label(root, text='I am a label. Click me.')
label.pack()

def my_callback():
    print('Label was clicked.')

# Bind mouse button 1 click on label
label.bind("<Button-1>", lambda e:my_callback())

# A lambda with parameters looks like this:
# lambda event, a=12, b=34:my_callback(a, b))

root.mainloop()