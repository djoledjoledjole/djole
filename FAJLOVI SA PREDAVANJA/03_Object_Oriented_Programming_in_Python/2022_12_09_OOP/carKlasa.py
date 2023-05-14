class Automobil:
    marka    = ''    # instancno svojstvo
    model    = ''    # instancno svojstvo
    godiste  = 0     # instancno svojstvo
    alufelne = True # instancno svojstvo, ono sto je svima drugacije

    brojTockova = 4 # staticko svojstvo, definise celu klasu 

    # METODE
    def vozi(self):
        print('auto je u pokretu')
        print(self.model)
    
    def postviFelne(self):
        if self.alufelne == True:
            print('imate vec alufelne')
        else:
            print('alufelne su postavljene')



auto1 = Automobil() # objekat/instanca - instanciranje klase
print(auto1.model, auto1.marka, auto1.godiste, auto1.alufelne) #nema nista
auto1.marka = 'citroen'
auto1.model = 'c3'
auto1.godiste = 2017
auto1.alufelne = False
print(auto1.model, auto1.marka, auto1.godiste, auto1.alufelne)

print(Automobil.brojTockova)

auto1.vozi()
auto1.postviFelne() # a ovo je nasa metoda(MI SMO PRAVILI)

#################################################################
# STRING TIP
slova = str()
slova = 'AbcD'
slova.upper() # OVO JE METODA STRINGA (OVA JE UGRADJENA)
slova.lower()