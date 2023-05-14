from abc import *

class Kartica(ABC):
    def __init__(self, broj, stanje) -> None:
        self.broj = broj
        self.stanje = stanje
    @abstractmethod
    def plati(self, suma):
        pass

# k = Kartica() # OVO NE MOZE JER JE KARTICA APSTRAKTNA METODA!!!

class Visa(Kartica):
    def plati(self, suma):
        self.suma = suma * 1.05
        print(self.stanje - self.suma) #return ne stampa vrednost


visa = Visa('111', 5000000)

visa.plati(2000)