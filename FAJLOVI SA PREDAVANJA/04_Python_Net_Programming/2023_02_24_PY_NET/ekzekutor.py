import concurrent.futures.thread as t
import time


executor = t.ThreadPoolExecutor(100) # parametar je broj niti

def f():
    print('hello')
    # time.sleep(1)
    print('how are you')

for i in range(1000):
    executor.submit(f)
#-------------------------------------------------------------------------
# Python Net Programming LS1 6/6
# Vreme početka: 24.2.2023.
#
#  EGZEKUTORI 1:12
#  Egzekutori su puleri niti. PULOVI su posebni objekti koji izvrse
#  komplikovane operacie ali ih na kraju ne unistavaju. Pul npr se konektuje 
#  na bazu dvaput, aplikakica koja se konektuje na bazu obraca se pulu koji
#  ima konekcije, kad zavrsi vrati pulu konekciju, pul ne unisti konekciju
#  nego ceka sleddecu.
#-------------------------------------------------------------------------