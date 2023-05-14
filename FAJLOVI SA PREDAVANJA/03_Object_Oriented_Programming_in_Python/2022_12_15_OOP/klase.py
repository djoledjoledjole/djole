class Automobil:
    brojTockova = 4
    #  marka,model,godiste,parkiran
    def __init__(self, marka, model, godiaste, parkiran=False):
        self.marka = marka
        self.model = model
        self.godiste = godiaste
        self.parkiran = parkiran

    # Marka: ... , model: ... , godiste: ... , parkiran \ u pokretu
    def informacije(self):      # INSTANCNI METOD
        status = 'parkiran je' if self.parkiran else 'u pokretu'
        return f'marka: {self.marka}\nmodel: {self.model}\ngodiste: {self.godiste}\nstatus: {status}'

    @staticmethod        # STATICKI METOD
    def info_o_automobilima():
        print('ima cetiti tocka')
        print('registruje se jednom godisnje')

    # parkiraj,     proveri da li je auto prakiran - ako je parkiran: vec ste parkirani
    # u suprotnom - svostvo parkiran prebaciti u true
    def parkiraj(self):
        if self.parkiran == False:
            print('u pokretu ste')
        else:
            self.parkiran == True
            print('parkirani ste')

automobil1 = Automobil('citroen', 'c5', 2021, True)
print(automobil1.marka, automobil1.model)
print(automobil1.informacije())

automobil2 = Automobil('Ford', 'Focus',  2020, False)
print(automobil2.informacije())

Automobil.info_o_automobilima()
automobil1.parkiraj()
automobil2.parkiraj()