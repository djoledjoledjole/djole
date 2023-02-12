# brojevi = [1,3,5]
# try:
#     print(brojevi[6])
#     print('ispisan je broj')
# except:
#     print('greska')

# print('nastavak programa')
# print('kraj programa')

########################################################

#uzimam od korisnika 2 broja
#delimo
try:
    broj1 = int(input('prvi broj: '))
    broj2 = int(input('drugi broj: '))
    print('deljenje')
    print(broj1/broj2)
    print('rezultat: ', broj1/broj2)
# except:
#     print('error, izuzetak je uhvacen')
except ZeroDivisionError as greska1:
    print('ne mozete deliti sa nulom')
except ValueError as greska2:
    print('ne mozete uneti tekst')
except Exception as greska3:
    print(greska3)
    print('izgleda da je neka greska')