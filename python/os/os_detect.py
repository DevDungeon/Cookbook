import platform

print "Platform Stuff\n"
print platform.system() # Windows, Linux, Java
print "Release " + platform.release()
print platform.python_version()
print platform.uname()