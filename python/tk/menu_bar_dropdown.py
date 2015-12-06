# menu_bar_dropdown.py
from tkinter import *
root = Tk()

# Create main menu bar
menu_bar = Menu(root)

# Create the submenu (tearoff is if menu can pop out)
file_menu = Menu(menu_bar, tearoff=0)

# Add commands to submenu
file_menu.add_command(label="Quit!", command=root.destroy)
file_menu.add_command(label="Exit!", command=root.destroy)
file_menu.add_command(label="End!", command=root.destroy)

# Add the "File" drop down sub-menu in the main menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()