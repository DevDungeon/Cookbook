import threading
import time
from tkinter import *

root = Tk()

def just_wait(seconds):
    print('Waiting for ', seconds, ' seconds...')
    time.sleep(seconds)
    print('Done sleeping.')

def button_callback():
    # Without the thread, the button will stay depressed and the
    # program will respond until the function has returned
    my_thread = threading.Thread(target=just_wait, args=(5,))
    my_thread.start()

button = Button(root, text='Run long thread.', command=button_callback)
button.pack()

# Without them pressing a button that performs
# a long action will pause the entire program and it 
# Will appear as if the program froze - Note about the GIL and only maximizing one cpu

root.mainloop()