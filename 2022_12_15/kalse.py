class Automobil:
    brojTockova = 4
    
    def __init__(self,marka,model,godiste,parkiran=False): #ovo je ono sto ce biti u zagradama: Automobili( ovde )
        self.marka = marka
        self.model = model
        self.godiste = godiste
        self.parkiran = parkiran
    
    def informacije(self):
        status = 'parkiran' if self.parkiran else 'u pokretu'
        return f'marka: {self.marka}\nmodel: {self.godiste}\ngodiste: {self.godiste}\n{status}'

    @staticmethod #staticki metod
    def info_o_automobilima():
        print('automobili imaju cetiri tocka')
        print('registracija jednom godisnje')

    def parkiranje(self):
        if self.parkiran == True:
            print('vec ste parkirani')
        else:
            self.parkiran = True
            print('parkirani ste')

# print('marka: ', a1.marka)
# print('model: ', a1.model)

a1 = Automobil('audi', 'a3', 2017, True)
print(a1.informacije())

a2 = Automobil('citroen', 'c5', 2012, False)
print(a2.informacije())

Automobil.info_o_automobilima() #staticki metod - opisuje ceo pojam, a instancne pojedinacno

print(a1.parkiranje())
print(a2.parkiranje())
