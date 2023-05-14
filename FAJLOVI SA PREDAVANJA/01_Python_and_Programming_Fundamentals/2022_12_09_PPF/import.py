import random 
import racunanjePaket.kalkulator as kalkulator # poziva moj fajl prethodno naprevljen
from racunanjePaket.kalkulator import * # ne mora da se poziva kalkulator._______
import racunanjePaket.kalkulator as k # menja naziv sa kojima mozemo da pristupamo



random.randint(5, 10)

print(kalkulator.sabiranje(5,2))

rezultatOduzimanja = kalkulator.oduzimanje(8,5)
print(rezultatOduzimanja)

sabiranje(14,12)
oduzimanje(14,4)


k.oduzimanje(15,12)