######################################################################
#----------------------------PRIMER--------------------------------
# class Automobil:
#     #         marka    = ''    OVO JE POSTALO  
#     #         model    = ''    NEPOTREBNO JER SMO
#     #         godiste  = 0     POZVALI U def __init__(self, parametri......)
#     #         alufelne = True
#     brojTockova = 4 # staticko svojstvo, definise celu klasu
#
#     def __init__(self, marka, model, godiste, alufelne):
#         print('pravim automobil sa sledecim karakteristikom:')
#         self.marka = marka
#         self.model = model
#         self.godiste = godiste
#         self.alufelne = alufelne
#
# a = Automobil('citroen', 'c4', 2017, False)
# print(a.model)
######################################################################
#---------------------PRIMER JA RADIO-----------------------------
class Osoba:
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

osoba1 = Osoba('Maja', 'Maric', 30)
osoba2 = Osoba('Marija', 'Popovic', 29)

print('ime :', osoba1.ime)
print('prezime: ', osoba1.prezime)
print('godine', osoba1.godine)

print('ime :', osoba2.ime)
print('prezime: ', osoba2.prezime)
print('godine', osoba2.godine)
#######################################################################