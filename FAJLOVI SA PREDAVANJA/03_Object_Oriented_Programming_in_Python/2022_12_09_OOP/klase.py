#-----------------------------K L A S E------------------------------------
# # osoba
# ime, prezime, godine - osobine
# trci, predstavi se - funkcionalnosti 

class Osoba:
    ime = ""
    prezime = ''        # definisali sta klasa poseduje
    godine = 0       


osoba1 = Osoba()
osoba1.ime = 'sofija'
osoba1.prezime = 'maric'           # naporavili objekat (ako sam dobro razumeo..)   
osoba1.godine = 25
print(osoba1.ime, osoba1.prezime, osoba1.godine)


print(type(osoba1)) # type() - pokazuje koji je tip vrednosti


osoba2 = Osoba()
osoba2.ime = 'sava'
osoba2.prezime = 'djoric'          # napravili drugi objekat (ako sam dobro razumeo..)
osoba2.godine = 30
print(osoba2.ime, osoba2.prezime, osoba2.godine)


osobe = [osoba1, osoba2]
for i in osobe:
    print('ime: ', i.ime)
    print('prezime: ', i.prezime)


#####################################################################
# OVO JE PROIBA I PITANJE KOJE BI TREBALO DA POSTAVIM NJOJ, ZASTO
#      PRINTA SVE STO JE  NAVEDENO U KLASI NA DRUGOM MODULU

# from mojTestFajl import Igrac
# dobrivoje = Igrac
# dobrivoje.nick = 'DOCA'
# print(dobrivoje.nick)
#####################################################################