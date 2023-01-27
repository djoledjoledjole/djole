fajl = open("podaci1.txt", 'r+') # otvaranje fajla
sadrzaj_fajla = fajl.read() # citanje fajla
print(sadrzaj_fajla)

fajl.write('\nproba write')


fajl.close() # zatvaranje fajla