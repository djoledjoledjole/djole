import time
from datetime import datetime
import random

odd = [i for i in range(1, 60, 2)]

this_minute = datetime.today().minute

for i in range(5):
    if this_minute in odd:
        print('This is an odd minute')
    else:
        print('This is not an odd minute')
    pause = random.randint(1, 20)
    time.sleep(pause)