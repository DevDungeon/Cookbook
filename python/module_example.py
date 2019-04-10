# some_module.py

# Define a function for use later
def some_func():
    print("Hi")

# If run directly with `python some_module.py`
if __name__ == '__main__':  # Optional, not needed for library only modules
    # Use the functions and classes defined earlier in this .py file
    print("Module '%s' was invoked." % __file__)
    some_func()