import importlib

# Contrived example of generating a module named as a string
full_module_name = "mypackage." + "mymodule"

# The file gets executed upon import, as expected.
mymodule = importlib.import_module(full_module_name)

# Then you can use the module like normal
mymodule.func1()
mymodule.func2()