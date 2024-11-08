from colorama import just_fix_windows_console, init 
from random import randint

just_fix_windows_console(); init()

class Color:
    RED =        f"\u001b[38;5;{1}m"
    ORANGE =     f"\u001b[38;5;{166}m"
    YELLOY =     f"\u001b[38;5;{11}m"
    GREEN =      f"\u001b[38;5;{34}m"
    DARK_GREEN = f"\u001b[38;5;{64}m"
    TURQUOISE =  f"\u001b[38;5;{30}m"
    BLUE =       f"\u001b[38;5;{39}m"
    DARK_BLUE =  f"\u001b[38;5;{20}m"
    PINK =       f"\u001b[38;5;{210}m"
    PURPLE =     f"\u001b[38;5;{125}m"
    VIOLET =     f"\u001b[38;5;{55}m"
    BROWN =      f"\u001b[38;5;{94}m"
    WHITE =      f"\u001b[38;5;{255}m"
    LIGHT_GRAY = f"\u001b[38;5;{243}m"
    GRAY =       f"\u001b[38;5;{239}m"
    BLACK =      f"\u001b[38;5;{16}m"
    RESET = 	 f"\u001b[0m"

    def __new__(self, ANSICode = randint(0, 255)) -> str: return f"\u001b[38;5;{ANSICode}m"

class BgColor:
    RED =        f"\u001b[48;5;{1}m"
    ORANGE =     f"\u001b[48;5;{166}m"
    YELLOY =     f"\u001b[48;5;{11}m"
    GREEN =      f"\u001b[48;5;{34}m"
    DARK_GREEN = f"\u001b[48;5;{64}m"
    TURQUOISE =  f"\u001b[48;5;{30}m"
    BLUE =       f"\u001b[48;5;{39}m"
    DARK_BLUE =  f"\u001b[48;5;{20}m"
    PINK =       f"\u001b[48;5;{210}m"
    PURPLE =     f"\u001b[48;5;{125}m"
    VIOLET =     f"\u001b[48;5;{55}m"
    BROWN =      f"\u001b[48;5;{94}m"
    WHITE =      f"\u001b[48;5;{255}m"
    LIGHT_GRAY = f"\u001b[48;5;{243}m"
    GRAY =       f"\u001b[48;5;{239}m"
    BLACK =      f"\u001b[48;5;{16}m"
    RESET = 	 f"\u001b[0m"

    def __new__(ANSICode = randint(0, 255)) -> str: return f"\u001b[48;5;{ANSICode}m"
        

def Coloring(keywords: dict, Str: str):
    for name in keywords:
        match name:
            case "__all__":   return keywords[name] + Str
            case "__start__": return keywords[name] + Str[:1] + "\u001b[0m" + Str[1:]
            case "__end__":   return Str[:-1] + keywords[name] + Str[-1:] + "\u001b[0m"
            case "__mid__":   i = len(Str) // 2; return Str[:i] + keywords[name] + Str[i] + "\u001b[0m" + Str[i + 1:] if len(Str) % 2 == 1 else Str[:i - 1] + keywords[name] + Str[i - 1:i + 1] + "\u001b[0m" + Str[i + 1:]
    
    index = Str.find(name) if name in Str.split() else -1

    returnStr = Str[:index] + keywords[name] + name + "\u001b[0m" + Str[index + len(name):] if index != -1 else Str

    return returnStr
