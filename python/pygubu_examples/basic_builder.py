import Tkinter
import pygubu


builder = pygubu.Builder()
builder.add_from_file('testgubu.ui')  # ui file

root = Tkinter.Tk()
main_window = builder.get_object('Frame_1', root)  # Name of main widget to open
root.mainloop()
