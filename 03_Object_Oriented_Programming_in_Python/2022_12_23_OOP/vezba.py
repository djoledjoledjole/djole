class Oblik:
    def __init__(self, boja):
        self.boja = boja

    def izracunaj_povrsinu(self):
        return "racunam povrsinu"


class Kvadrat(Oblik):
    def __init__(self, boja, a):
        super().__init__(boja)
        self.a = a
    
    def izracunaj_povrsinu(self):
        povrsina = self.a * self.a
        return super().izracunaj_povrsinu(), povrsina


class Krug(Oblik):
    def __init__(self, boja, r):
        super().__init__(boja)
        self.r = r
    
    def izracunaj_povrsinu(self):
        return super().izracunaj_povrsinu(), self.r*self.r*3.14 # ovo sam ja stavio bez promenjljive



kvadrat1 = Kvadrat('zuta', 5)
print(kvadrat1.izracunaj_povrsinu())

precnik_kruga1 = Krug('zuta', 5)
print(precnik_kruga1.izracunaj_povrsinu())