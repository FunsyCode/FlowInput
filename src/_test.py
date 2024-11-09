import time
import sys

time.sleep(0.5)

for i in range(5):
    
    print(f'hello{i}', end='\r')
    sys.stdout.write(f"\033[{i}G")
    sys.stdout.flush()

    time.sleep(0.5)

    sys.stdout.write("\033[0G")
    sys.stdout.flush()

    time.sleep(0.5)
