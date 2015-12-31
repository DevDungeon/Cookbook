try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2

import pygubu


class Application:
    def __init__(self, master):
        # 1: Create a builder
        self.builder = builder = pygubu.Builder()
        # 2: Load an ui file
        builder.add_from_file('testgubu.ui')
        # 3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('Frame_1', master)
        print(builder.get_variable())


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
