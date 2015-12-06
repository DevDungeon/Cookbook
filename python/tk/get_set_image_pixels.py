# get_set_image_pixels.py
import sys
from tkinter import *
root = Tk()

# First command line arg is image path. PNG format
img = PhotoImage(file=sys.argv[1])

red = 255
green = 0
blue = 0
x = 0
y = 0

# Sets the top left pixel of the image to red (difficult to see)
img.put("#%02x%02x%02x" % (red, green, blue), (y, x))

# Get the (red, green, blue) tuple of pixel at 0,0
top_left_pixel = img.get(0, 0)  
print(top_left_pixel)

# Display the image
img_label = Label(root, image=img)
img_label.pack()

root.mainloop()