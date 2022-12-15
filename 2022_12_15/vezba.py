#proizvod     naziv opis cena
#korpa        spisaProizvoda ukupna cena

class Proizvod:
    def __init__(self, naziv, opis, cena):
        self.opis = opis
        self.cena = cena
        self.naziv = naziv

class Korpa:
    def __init__(self, spisakProizvoda):
        self.spisakProizvoda = spisakProizvoda #svojstvo 1
        res = 0
        for pr in spisakProizvoda:
            res += pr.cena
        self.ukupnaCena = res #svojstvo 2

pr1 = Proizvod('patike', 'fudbalske patike', 27000)
pr2 = Proizvod('patike', 'kosarkaske patike', 25000)
pr3 = Proizvod('papuce', 'cross', 5000)

listaPr = []
listaPr.append(pr2)
listaPr.append(pr1)

korpa = Korpa(listaPr)
print(korpa.ukupnaCena)