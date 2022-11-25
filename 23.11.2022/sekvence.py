# osoba = ['sofija', 20, 'plava', True]
# print(osoba)

# print(osoba[0])
# print('godine:', osoba[1])


# automobil = ['opel', 'citroen', 'mercedes']

# print(automobil[1])

# for x in range(1, 10, 2):
#     print(x)




# kurs = 'python'
# print(kurs[0])

# for i in kurs:
#     print(i)

# for x in range(6):
#     print(kurs[x])

    
# for x in range(len(kurs)):
#     print('na poziciji', x, kurs[x])

# ustanova = 'it academy'

# for i in range(len(ustanova)):
#     print(ustanova[i])



# primer = 'zadatak1'

# for i in range(len(primer)):
#     print(primer[i])



# brojKaraktera = len(primer)
# indeks = 0

# while indeks < len(primer):
#     print(primer[indeks])
#     indeks += 1

korisnickoIme = 'admin'
unetoKorisnickoIme = input('unesi korisnicko ime:')

if korisnickoIme == unetoKorisnickoIme.lower():
    print('dobrodosli')
else:
    print('pogresni podaci')
