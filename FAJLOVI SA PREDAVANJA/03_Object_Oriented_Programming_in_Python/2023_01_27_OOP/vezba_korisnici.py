import csv

fajl = open('vezba_korisnici.csv')

reader = csv.reader(fajl)

ime = input("ime? ")
pin = input('pin? ')

for podatak in reader:
    if ime == podatak[0]:
        if pin == podatak[1]:
            print('stanje:', podatak[2])
