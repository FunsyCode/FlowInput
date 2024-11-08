import colorama; colorama.init()

from ._keyboard import *
from ._colors import *
from ._input import *

def input(__prompt: str = "", __default: str = "", __color: any = Color.WHITE) -> str:


    print(f"{__prompt}"); print(f"{__color}{__default}", end='\r')
    
    sys.stdout.write(f"\033[{len(__default)}G")
    sys.stdout.flush()

    collect(__default, __color, (len(__default))) if __color != None else collect(__default, __pos=(len(__default)))

    listener = Listener(on_press=userInput); listener.start()

    __default = get(); return __default
