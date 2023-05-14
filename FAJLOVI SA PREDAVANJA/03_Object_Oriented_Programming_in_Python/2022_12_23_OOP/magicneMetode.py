x = 100
poruka = 'hello'

print(x)
print(poruka)


class Proizvod:
    def __init__(self, naziv, cena) -> None:
        self.naziv = naziv
        self.cena = cena
    
    def __str__(self) -> str:
        return f"proizvod: {self.naziv}, cena: {self.cena}"
    
    def __add__(self, drugi):
        return self.cena + drugi.cena


p1 = Proizvod('Laptop', 50000)
p2 = Proizvod('Laptop', 40000)
print(p1)
print(p1 +p2)