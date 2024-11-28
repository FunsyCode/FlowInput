import colorama

colorama.just_fix_windows_console()

def backspace(default: str, pos: int) -> list:
    if pos != 1: return [default[:pos - 1] + default[pos:], pos - 1]
    elif pos == 1: return [default[:pos - 1] + default[pos:], -1]
    else: return [default, pos]

def right(default: str, pos: int) -> int:
    if pos <= -1: return 1
    elif pos != len(default): return pos + 1
    else: return pos

def left(pos: int) -> int:
    if pos != 1: return pos - 1
    elif pos == 1: return -1
    else: return pos

def space(default: str, pos: int) -> list:
    return [default[:pos] + ' ' + default[pos:], pos + 1]

def go(default: str, key: str, pos: int) -> list:
    if pos <= -1: return [default[:pos] + key + default[pos:], 1]
    else: return [default[:pos] + key + default[pos:], pos + 1]
