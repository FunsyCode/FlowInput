from ._cursor import *
from ._colors import *

import sys

from colorama import just_fix_windows_console

just_fix_windows_console()

default, color, pos = str, None, int

def user_input(key) -> str:
    global default, color, pos

    if key == 'space':
        default, pos = space(default, pos)
    elif key == 'backspace':
        default, pos = backspace(default, pos)
    elif key == 'right':
        pos = right(default, pos)
    elif key == 'left':
        pos = left(pos)
    else:
        default, pos = go(default, key, pos)

    print(f"\r{color}{default} \r\033[{pos}C", end='')

def collect(__default: str, __color: None = Color.WHITE, __pos = int) -> None: global default, color, pos; default, color, pos = __default, __color, __pos
def get() -> str: return default
