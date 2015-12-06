# entry_widget.py
from tkinter import *
root = Tk()

# Create single line text entry box
entry = Entry(root)
entry.pack()

# Specifying character position in entry
# - END: After last character of entry widget
# - ANCHOR: The beginning of the current selection
# - INSERT: Current text cursor position
# - "@x": Mouse coordinates

# Insert some default text
entry.insert(INSERT, 'Hello, world!')

# Print the contents of entry widget to console
def print_content():
    print(entry.get())

# Create a button that will print the contents of the entry
button = Button(root, text='Print content', command=print_content)
button.pack()

root.mainloop()