class Automobil:
    marka      =''
    model =''
    godiste=0
    alufelne = False

    brojTockova = 4 # staticko svojstvo

    #metode:  unutar tela se naziva ne funkcija nego metod
    def vozi(self):
        print('auto je u pokretu')
        print(self.model)

    def postaviFelne(self):
        if self.alufelne == True:
            print('imate vec alufelne')
        else:
            self.alufelne = True
        print('postavljene su')

auto1 = Automobil() #objekat/ instanca - instanciranje klase
print(auto1.model, auto1.marka, auto1.godiste, auto1.alufelne)
auto1.marka = 'citroen'
auto1.model = 'c3'
auto1.godiste = 2017
auto1.alufelne = False
print(auto1.model, auto1.marka, auto1.godiste, auto1.alufelne)

print(Automobil.brojTockova)



auto1.vozi()
auto1.postaviFelne() #metoda automobila




#########################################################################
#string tip
slova = 'AbcD'
slova = str() #""
slova = 'AbcD'

slova.upper() #metoda stringa
slova.lower()
