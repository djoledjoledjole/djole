import time


class Vozilo:
    def __init__(self, tip, brzina):
        self.tip            = tip
        self.brzina         = brzina
        self.destinacija    = 0
        self.trenutna_tacka = 0

    def korak(self):
        self.trenutna_tacka += self.brzina
        print(self.tip, "je na poziciji", self.trenutna_tacka)
        if self.trenutna_tacka >= self.destinacija:
            self.stigao = True
            print(self.tip, "je stigao")
    
    def kreni(self,destinacija):
        self.destinacija = destinacija
        self.trenutna_tacka = 0

class Auto(Vozilo):
    def __init__(self):
        super().__init__("Auto", 20)

class Bicikl(Vozilo):
    def __init__(self):
        super().__init__("Bicikl", 5)

a = Auto()
b = Bicikl()
a.kreni(400)
b.kreni(400)
vozila = [a,b]
while True:
    for v in vozila:
        v.korak()
        if v.stigao:
            vozila.remove(v)
    time.sleep(0.5)
