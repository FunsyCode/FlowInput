from ._cursor import *
from ._colors import *

from colorama import init; init()
import sys

default, color, pos = str, None, int

def userInput(key) -> str:
    global default, color, pos

    if key == 'space':
        default += ' '
    elif key == 'backspace':
        pos = Backspace(pos)
        if pos == 0: default = default
        else: default = default[:pos-1] + default[pos+1:] + ' '
    elif key == 'right':
        pos = Right(pos)
    elif key == 'left':
        pos = Left(pos)
    elif key == 'enter':
        print(f"{color}{default} ")
    else:
        default += key; pos = Go(pos)

    sys.stdout.write(f"\033[{0}G"); sys.stdout.flush() # Move cursor to start
    print(f"{color}{default}", end='\r')
    sys.stdout.write(f"\033[{pos - 1}G"); sys.stdout.flush() # Move cursor to pos

def collect(__default: str, __color: None = Color.WHITE, __pos = int) -> None: global default, color, pos; default, color, pos = __default, __color, __pos + 1
def get() -> str: return default
