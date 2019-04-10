# Threads in Python
# Async? Threadpool?
from threading import Thread
import time


def go(func_name, *args):
	Thread(target=func_name, args=args).start()


def say_hi(name):
	print(f"Hello, {name}!")

def background_task(*args):
	print(f"Received argument: {args}")
	print("Processing...")
	time.sleep(3)
	print("Done processing.")

def calculate(a, b):
	return a * b


go(background_task, 1, 2, 3)
go(say_hi, "dano")

print("We can continue")
print("It will wait until threads are all done.")

print("Getting value of calculate(2,3)...")
print(calculate(2,3))
product = go(calculate,2,3)
print(f"Product: {product}")





# What about a threadpool for large number of jobs?