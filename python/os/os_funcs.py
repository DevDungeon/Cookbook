import os

# Get OS name and environment vars
print os.name
print os.environ 

# Get and change directories
print os.getcwd()
os.chdir("/")
print os.getcwd()

# Execute programs
os.system("dir")
os.system("ls")

dirList = os.listdir()
for filename in dirList:
    print filename
