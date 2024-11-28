import colorama

from ._keyboard import *
from ._colors import *
from ._input import *

colorama.just_fix_windows_console()

def input(prompt: str = '', default: str = '', color: Color | BgColor = Color.WHITE) -> str:

    """Проверяем prompt и default"""
    if not prompt and default:
        print(f'\r{color}{default}\r\033[{len(default)}C', end='')
    
    elif prompt and not default:
        print(f'{prompt}')
        print(f'\r{color}\r\033[{(len(default)) - 1}C', end='')
    
    elif prompt and default:
        print(f'{prompt}')
        print(f'\r{color}{default}\r\033[{len(default)}C', end='')

    else:
        print(f'\r{color}\r\033[{(len(default)) - 1}C', end='')

    """Отслеживание ввода с клавиатуры"""
    collect(default, color, len(default))

    listener = Listener(on_press=user_input)
    listener.start()

    print('\u001b[0m')

    __default = get(); return __default
