# def digitron(broj1, broj2, operacija):
#     if operacija == '+':
#         # print(broj1 + broj2)
#         return broj1 + broj2
#     elif operacija == '-':
#         return broj1 - broj2
#     elif operacija == '*':
#         print(broj1 * broj2)
#     elif operacija == '/':
#         print(broj1 / broj2)
#     else:
#         print('pogresna operacija')

# rezultat = digitron(2,3,'*')
# #rezultatSabiranja
# print(rezultat)
# rezultatOduzimanja = digitron(2,3,'-')
# print(rezultatOduzimanja)
# ######################################################
# ime = input('ime? ')
# prezime = input('prezime? ')
# godina = input('godina? ')
# korisnickoIme = ''

# def kreiraj_kor_ime(ulazIme, ulazPrezime, ulazGodina):
#     korIme = f'ita{ulazGodina}.{ulazIme.lower()}{ulazPrezime.lower()}'
#     print('uspesno kreirano')
#     return korIme

# korisnickoIme = kreiraj_kor_ime(ime, prezime, godina)
# print('prikiupljeni podaci o korisniku')
# print(ime, prezime, korisnickoIme)
############################################################
# def menjacnica(eur):
#     return eur * 117

# iznos = menjacnica(int(input('unesi vrednost u evrima: ')))
# print('rezultat u dinarima: ', iznos)
############################################################
# def registracija(licnaKarta, cistAutomobil, saobracajna):
#     if cistAutomobil == False:
#         return 'NEUSPESNO!'
#     if licnaKarta == False:
#         return 'NEUSPESNO!'
#     if saobracajna == False:
#         return 'NEUSPESNO!'
#     return 'USPESNO!'
#                  isto gore i dole
# def registracija(licnaKarta, cistAutomobil, saobracajna):
#     if cistAutomobil == False or licnaKarta == False or saobracajna == False:
#         return 'NEUSPESNO'
#     return 'USPESNO'
# rezultat = registracija(True,True,False)
# print(rezultat)
# ###############################################################
# stanje = 250000
# def bankomat(stanjeNaRacunu, zeljeniIznos):
#     if stanjeNaRacunu >= zeljeniIznos:
#         return f'uspesno! novo stanje je {stanje - zeljeniIznos}'
#     return 'neuspesno!'
# rezultat = bankomat(stanje, int(input('zeljeni iznos? ')))
# print(rezultat)
################################################################
# def registracija(*dokumenti):
#     print('doneli ste dokumenta: ')

#     print(dokumenti)
#     print(type(dokumenti))
#     print(dokumenti[0])

# registracija('vozacka', 'tehnicki', 'lk')
# ##################
# a = 1
# print(type(a))
#####################
#           * pravi tuple
#           ** prave recnik
##########################################
# def upis(**podaci):
#     print('uneli ste')
#     print(podaci['prezime'])

# upis(ime = 'djole', prezime = 'boskovic', ustanova = 'lalala')
###################################################################
#zajaebano je ovo
# def skolovanje(predavac_predaje):
#     print('skolska godina je u toku')
#     print('ucionica a21')
#     predavac_predaje()

# def predavac_vm():
#     print('uvod u mreze')
#     print('danas radimmo novu temu')
#     print('da li ste igrali lol')

# def predavac_al():
#     print('opet imamo predavanje sredom')
#     print('radimo funkcije')

# def predavac_vn():
#     print('krecemo hmml')

# skolovanje(predavac_al)
###################################################
# def pripremaObroka(spremanje):
#     print('dolazak u kuhinju')
#     print("perem ruke")
#     spremanje()

# def dorucak():
#     BUREK
# def rucak():
#     POHOVANJE
# def vecera():
#     TUNJEVINA


# pripremaObroka(dorucak)
######################################################

#------------LAMBDA pogledati-------------
# res = lambda a, b: a+b
# v = res(10, 5)
# print(v)
###############################################

#------------rekurzivna funkcija-------------
# def tajmer(sekunde):
#     print(sekunde)
#     sekunde -= 1
#     if sekunde > 0:
#         tajmer(sekunde)

# tajmer(10)
################################################

#--------------dekorator 8:25-----------------

# def provera(funkcija):
#     def unutrasljaFunkcija(a,b):
#         if b==0:
#             print('nije dozvoljeno deljenje nulom')
#             return
#         funkcija(a,b)
#         return unutrasljaFunkcija
# @provera
# def deljenje(a, b):
#     print(a/b)

# deljenje(10,0)

# OVO NE RADI!!!

##########################################################
#---------------------GENERATOR--------------------------
# def brojevi():
#     yield 1
#     yield 2
#     yield 3
# dobijeniBroj = brojevi()
# print(dobijeniBroj)
# print(next(dobijeniBroj))
# print(next(dobijeniBroj))
# print(next(dobijeniBroj))

# for broj in brojevi():
#     print(broj)
##########################################################