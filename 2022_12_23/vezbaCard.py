class Card:
    def __init__(self, broj, stanje):
        self.broj = broj
        self.stanje = stanje
    
    def pay(self, suma):
        self.stanje -= suma

class Visa(Card):
    porez = 1.05

    def pay(self, suma):
        if isinstance(suma, int): # proverava kog je tipa, u ovom slucaju da li je broj(int)
            self.stanje -= suma * self.porez

class Master(Card):
    porez = 1.08

    def pay(self, suma):
        self.stanje -= suma * self.porez

visacard1 = Visa(123, 500)
visacard1.pay(200)
print(visacard1.stanje)

print(isinstance(visacard1, Card)) #proverava da li je tipa Card ### isinstance(ono sta proverava, ove klase) daje True or False