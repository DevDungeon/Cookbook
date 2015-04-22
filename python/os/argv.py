import sys

print(len(sys.argv))

print(sys.argv[0])

for index, arg in enumerate(sys.argv): # enumerate needed to get index
    print("Arg[" + repr(index) + "]: " + repr(arg))
