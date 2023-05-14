#importuje se ime fajla
import car 

from car import * #imporuje se sve ne mora vise ime fajla
#auto1 = car.Automobil()
# auto1 = Automobil()
# print(auto1.model, auto1.marka, auto1.godiste, auto1.alufelne)

class Automobil:
    # marka = ''
    # model = ''
    # godiste = 0
    # alufelne = False

    brojTockova = 4 # staticko svojstvo
    def __init__(self, zelejnaMarka, zeljeniModel, god, alufelne=False):
        print('pravim automobil')
        self.marka = zelejnaMarka
        self.zelejnaMarka = zeljeniModel
        self.model = god
        self.alufelne = alufelne

a = Automobil('citroen', 'c4', 2018)
##################################
#mi radimo
#osoba
#ime, prezime, godine

class Osoba:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

osoba = Osoba('anja', 'nikolic', 25)
print(osoba.ime)

osoba2 = Osoba('marko', 'jovanovic', 45)
print(osoba2.prezime)