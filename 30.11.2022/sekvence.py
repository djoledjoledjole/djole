#######################################################################
# brojevi = [9, 1, 3, 2,5, 8, 7]

# brojevi.sort()
# brojevi.reverse()

# print(brojevi)
######################################################################
        #  0  1  
# brojevi = [9, 1, 3, 2, 5, 8, 7]
# while True:
#     izvrsenaZamena = False
#     for i in range(1, len(brojevi)):
#         print(brojevi[i], 'poredim sa', brojevi[i-1])
#         if brojevi[i] < brojevi[i-1]:
#             privremena = brojevi[i]
#             brojevi[i] = brojevi[i-1]
#             brojevi[i-1] = privremena
#             izvrsenaZamena = True
#     if izvrsenaZamena == False:
#         break

# print(brojevi)
#######################################################################
# products = ['Phone', 'Tv', 'computer']
# prices = [155, 180, 250]

# for i in range(len(products)):
#     print(products[i], ':', prices[i])
#######################################################################
# automobili = ['audi', 'bmw', 'yugo', 'citroen', 'kia', 'peugeot']

# for i in automobili:
#     print('automobil: ', i)
#     if i == automobili[3]:
#         print('^aleksandrin auto^')
#######################################################################
proizvodi = [
                ['ajfon 11', 'samsung s22', 'saomi x3'],
                ['acer', 'mack', 'dell'],
                ['ajped', 'samsung tab', 'saomi tab']
            ]

telefoni  = ['ajfon 11', 'samsung s22', 'saomi x3']
laptopovi = ['acer', 'mack', 'dell']
tableti   = ['ajped', 'samsung tab', 'saomi tab']

print(proizvodi[0][0])
print(proizvodi[1][1])
proizvodi = [telefoni, laptopovi, tableti]

for i in proizvodi:
    for x in i:
        print(x)

for i in range(len(proizvodi)):
    print(proizvodi[i])
    for x in range(len(proizvodi[i])):
        print(proizvodi[i][x])
#######################################################################
# hrana = [
#             ['cokolada', 'bombone', 'palacinke'],
#             ['sarma', 'musaka', 'kiseli kupus'],
#             ['pecena paprika', 'ajvar', 'sopska']
#         ]

# for kategorija in hrana:
#     for jelo in kategorija:
#         print(jelo)
#######################################################################
# biblioteka = []

# while True:
#     print('komande: 1-unos, 2-prikaz, 3-brisanje, >3-izlaz')
#     komanda = int(input('unesite komandu: '))

#     if komanda == 1:
#         naslov = input('unesi naslov: ')
#         autor = input('unesi autora: ')
#         isbn = input('unesi isbn: ')
#         biblioteka.append([naslov, autor, isbn])
#         print('dodata knjiga: ')

#     if komanda == 2:
#         for knjiga in biblioteka:
#             for detalj in knjiga:
#                 print(detalj)
    
#     if komanda == 3:
#         kljucnaRec = input("naziv knjige koju brises? ")
#         for knjiga in biblioteka:
#             for detalj in knjiga:
#                 if detalj == kljucnaRec:
#                     biblioteka.remove(knjiga)
#                     print('knjiga je obrisana!')
#######################################################################