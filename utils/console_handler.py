import os

#from termcolor import colored


def clear() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')