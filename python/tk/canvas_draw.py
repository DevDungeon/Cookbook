# canvas_draw.py
from tkinter import *
root = Tk()

canv = Canvas(root, width=200, height=100)
canv.pack()

# Draw blue line from top left to bottom right with wide dashes
canv.create_line(0, 0, 200, 100, fill='blue', dash=(5, 15))

# Draw green rectangle at (100,50) to (120,55)
canv.create_rectangle(100, 50, 120, 55, fill='green')

# Draw oval(cirlce) from (20,20) to (40,40)
canv.create_oval(20, 20, 40, 40)

root.mainloop()