#    Proizvod:
#     naziv
#     opis
#     cena
class Proizvod:
    def __init__(self,naziv,opis,cena):
        self.naziv=naziv
        self.opis=opis
        self.cena=cena
        
# korpa spisak proizvada ukupna cena
class Korpa: # 2 17
    def __init__(self, spisak_proizvoda):
        self.spisak_proizvoda = spisak_proizvoda   # svojstvo 1
        rezultat = 0
        for pr in spisak_proizvoda:
            rezultat += pr.cena
        self.ukupna_cena = rezultat   # svojstvo 2

p1 = Proizvod('patike', 'za trcanje', 10000)
p2 = Proizvod('patike', 'za setnju', 12000)
p3 = Proizvod('patike', 'za trening', 6000)

lista_pr = []
lista_pr.append(p1)
lista_pr.append(p2)

korpa = Korpa(lista_pr)
print(korpa.ukupna_cena)

