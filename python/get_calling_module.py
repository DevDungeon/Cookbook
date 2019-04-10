import inspect


# Import this to other module and call it
def print_caller_info():
    # Get the full stack
    stack = inspect.stack()

    # Get one level up from current
    previous_stack_frame = stack[1]
    print(previous_stack_frame.filename)  # Filename where caller lives

    # Get the module object of the caller
    calling_module = inspect.getmodule(stack_frame[0])
    print(calling_module)
    print(calling_module.__file__)


if __name__ == '__main__':
    print_caller_info()