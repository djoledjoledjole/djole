import os 
print(os.cpu_count())
os.system('cls')


import sys
print(sys.platform)


import time
time.sleep(0.1)
print(time.time())

vreme = time.gmtime()
print(vreme.tm_wday)
print(vreme.tm_year)

datum = time.localtime()
print(time.strftime('Mesec: %m Godina: %Y Dan u nedelji: %w', datum))

