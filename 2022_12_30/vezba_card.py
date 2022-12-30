class Card:
    def __init__(self):
        self.__broj = 0
        self.__boja = ''
        self.__sifra = ''

    @property
    def broj(self):
        return self.__broj
    
    @property
    def boja(self):
        return self.__boja

    @property
    def sifra(self):
        return self.__sifra

    @broj.setter
    def broj(self, vrednost):
        self.__broj = vrednost
    
    @boja.setter
    def boja(self, vrednost):
        self.__boja = vrednost

    @sifra.setter
    def sifra(self, vrednost):
        self.__sifra = vrednost

karta1 = Card()
karta1.broj = 13
print(karta1.broj)