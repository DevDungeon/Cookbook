# menu_bar.py
from tkinter import *
root = Tk()

# Create a main menu and add a command to it
main_menu = Menu(root, tearoff=0)
main_menu.add_command(label="Quit", command=root.destroy)

root.config(menu=main_menu)
root.mainloop()