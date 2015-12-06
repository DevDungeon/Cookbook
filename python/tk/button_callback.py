# button_callback.py
from tkinter import *
root = Tk()

# Create a button that will destroy the main window when clicked
exit_button = Button(root, text='Exit Program', command=root.destroy)
exit_button.pack()

# Create a button with a custom callback
def my_callback():
    print("The button was clicked!")  # Prints to console not the GUI

print_button = Button(root, text='Click me!', command=my_callback)
print_button.pack()

root.mainloop()