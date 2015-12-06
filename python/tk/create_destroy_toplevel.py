# create_destroy_toplevel.py
from tkinter import *
root = Tk()

# Create new top level window. Opens immediately
second_window = Toplevel()
second_window.title('Second window')

# Destroy window
def destroy_second_window():
    second_window.destroy()

close_button = Button(
    root,
    text='Close second window',
    command=destroy_second_window
)
close_button.pack()

root.mainloop()