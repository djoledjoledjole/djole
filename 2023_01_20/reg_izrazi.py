import re

sablon = re.compile('ita') # sablon, sta ocekujem ili sta pretrazujem
tekst_za_proveru = 'korisnicko ,ita, ime pocinje sa ita.' # predmet provere

print(sablon.search(tekst_za_proveru)) #trazi gde je
print(sablon.findall(tekst_za_proveru)) #trazi koliko ima
print(sablon.match(tekst_za_proveru)) # da li nesto pocinje sa ...


sablon = re.compile('[a-zA-Z0-9]') #bez razmaka se pise po sintaksi
tekst_za_proveru = 'asd 123'
if sablon.search(tekst_za_proveru):
    print('poseduje slova')
else:
    print('ne poseduje')

# 1234567891011 - mora da ima trinaest brojeva
sablon = re.compile('[0-9]{13}') #{13} da li poseduje 13 brojeva
jmbg = '1231231231231'

if sablon.search(jmbg):
    print('ok je')
else:
    print('proveri opet brt')

#---------------------------------------------------------------------------------

#ita22.proba  -  ovo se trazi

sablon1 = re.compile('^ita[0-9]{2}\.[a-z]{5,}$')
proba = 'ita22.proba'

if sablon1.search(proba):
    print('bravo')
else:
    print('ajmo ponovo')

#---------------------------------------------------------------------------------

# proba.probic2020@gmail.com
sablon = re.compile('^[a-zA-Z0-9]+\.[a-zA-Z0-9]+[0-9]{4}@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$')
proba = 'proba.probic2020@gmail.com'

if sablon.search(proba):
    print('bravo')
else:
    print('ajmo ponovo')

#-------------------------------------------------------------------------------