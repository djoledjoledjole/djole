from abc import *
import time

# VEZBA OD PROSLOG PREDAVANJA #

class Trening(ABC):
    def __init__(self, naziv, trajanje, kalorije):
        self.naziv = naziv
        self.trajanje = trajanje
        self.kalorije = kalorije

    def prikazi_opis(self):
        return f'naziv: {self.naziv}\ntrajanje: {self.trajanje}\nkalorije: {self.kalorije} kcal'
    
    @abstractmethod
    def zapocni_trening():
        pass

class Kardio(Trening):
    def zapocni_trening(self):
        print(f"zapocet je trening: {self.naziv}")
        time.sleep(5)
        print(f"zavrsen je trening, potrosili ste {self.kalorije} kcal")


kardio1 = Kardio("trcanje", 60, 300)
kardio1.zapocni_trening()