class Automobil:
    def __init__(self, boja, model):
        self.boja = boja
        self.model = model
        self.__registracija = 0

    @property
    def registracija(self):
       return self.__registracija

    @registracija.setter
    def registracija(self, registracija):
        self.__registracija = registracija

a1 = Automobil('crvena', 'tesla')
a1.registracija = 123456
print(a1.registracija)