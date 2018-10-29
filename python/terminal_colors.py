# pip install colorama
# Works in Windows and Linux! woohoo

import colorama
from colorama import Fore, Style

colorama.init()

print(f'This is {Fore.GREEN}green{Style.RESET_ALL}!')
