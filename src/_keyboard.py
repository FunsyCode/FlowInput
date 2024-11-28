import msvcrt

class Listener: 
    def __init__(self, on_press = None):
        self.on_press = on_press
        self.running = True

    
    def start(self):
        while self.running:
            key = msvcrt.getwch()
            num = ord(key)

            if num in (0, 224):  # Проверяем на специальные клавиши
                symbol = msvcrt.getwch()  # Получаем следующий символ
                if symbol == 'K': self.on_press('left')
                elif symbol == 'M': self.on_press('right')

            if key == '\r': self.running = False
            elif key == ' ': self.on_press('space')
            elif key == '\x08': self.on_press('backspace')
            elif key == 'à': pass
            elif key.isprintable(): self.on_press(key)
