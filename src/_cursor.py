def Right(pos: int) -> int:
    pos += 1; return pos

def Left(pos: int) -> int:
    if pos == 0: return pos
    pos -= 1; return pos

def Go(pos: int) -> int:
    pos += 1; return pos

def Backspace(pos: int) -> int:
    if pos == 0: return pos
    pos -= 1; return pos
