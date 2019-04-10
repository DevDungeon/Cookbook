import sys
"""
System information
For details about resource usage like memory, disk, and processes see psutil lib
"""

print("Built in modules: ", sys.builtin_module_names)
print("Loaded modules: ", sys.modules)
print("Don't Write Bytecode: ", sys.dont_write_bytecode)
print("Python executable: ", sys.executable)
print("Python flags: ", sys.flags)
print("Check Internval: ", sys.getcheckinterval())
try:
    print("dlopen() flags: ", sys.getdlopenflags())  # Linux only
except:
    pass
print("Recursion limit: ", sys.getrecursionlimit())

print("Floating points: ", sys.float_info)
print("Float repr style: ", sys.float_repr_style)
try:
    print("Long integer: ", sys.long_info)
except:
    pass
print("Max integer: ", sys.maxsize)
print("Max size: ", sys.maxsize)
print("Max unicode: ", sys.maxunicode)

print("Byte order: ", sys.byteorder)
print("Platform: ", sys.platform)
#print "Windows version: ", sys.getwindowsversion()
print("File system encoding: ", sys.getfilesystemencoding())
print("Default encoding: ", sys.getdefaultencoding())
print("C API version: ", sys.api_version)
print("Python version: ", sys.version)  # Human readable
print("Python version info", sys.version_info)  # As a data struct