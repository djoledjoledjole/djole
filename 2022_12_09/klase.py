class Osoba:
    ime = ''
    prezime = ''
    godine = 0

osoba1 = Osoba()
print(osoba1.godine)
osoba1.ime = 'sofija'
osoba1.prezime = 'sofilic'
osoba1.godine = 25

print(osoba1.ime, osoba1.prezime, osoba1.godine)
print(osoba1) #ne moze
print(type(osoba1))

osoba2 = Osoba()
osoba2.ime = 'milovan'
osoba2.prezime = 'ciric'
osoba2.godine = 30

print(osoba2.ime, osoba2.prezime, osoba2.godine)

prisutni = [osoba1, osoba2]

for o in prisutni:
    print(f'ime: {o.ime}')
    print(f'prezime: {o.prezime}')


