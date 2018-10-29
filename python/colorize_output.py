from colorama import Fore, Back, Style, init
init()

print(Fore.CYAN)
print("Text will continue to be cyan")
print("until it is told otherwise")
print(Style.RESET_ALL)

print(Fore.RED + 'You can colorize a single line.' + Style.RESET_ALL)
print('Or a single ' + Back.GREEN + 'words' + Style.RESET_ALL + ' can be highlighted')

print(Fore.RED + Back.GREEN + 'Foreground and background colors can be combined' + Style.RESET_ALL)

print(Style.DIM + 'and in dim text' + Style.RESET_ALL)

print(Style.RESET_ALL)
print('Reset everything back to normal.')

