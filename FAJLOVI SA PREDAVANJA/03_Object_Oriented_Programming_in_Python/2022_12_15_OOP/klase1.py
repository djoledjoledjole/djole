# tip, broj korisnika, mockup, preuzeta za rad
# primer:
class Aplikacija:
    def __init__(self, tip, brojKorisnika, mockup, preuzetaZaRad):
        self.tip = tip
        self.brojKorisnika = brojKorisnika
        self.mockup = mockup
        self.preuzetaZaRad = preuzetaZaRad

fitApp = Aplikacija('FITNES', 25000, False, True)
webApp = Aplikacija('web', 40000000, True, True)

##############

class Firma:
    def __init__(self, naziv, brojZaposlenih, registrovana=False):
        self.naziv = naziv
        self.brojZaposlenih = brojZaposlenih
        self.registrovana = registrovana
    
    def zaposliNove(self, brojnovih):
        if brojnovih <= 0:
            print('ne moze manje od nula ili nula')
        else:
            self.brojZaposlenih += 100
            print(f'novi broj zaposlenih: {brojnovih}, trenutni broj zaposlenih je: {self.brojZaposlenih}')

    def otkazi(self, brojOtkaza):
        if brojOtkaza > self.brojZaposlenih:
            print('ne moze')
        else:
            if brojOtkaza > 0:
                self.brojZaposlenih -= brojOtkaza
                print(f'broj novih zaposlenih je {self.brojZaposlenih}')
            else:
                print('proverite broj mora biti veci od nule')

    def preuzmiProekat(self, projekat): # ode se poziva nesto iz Aplikacije, nisam skapirao
        if projekat.mockup: #mockup.. ocekuje da poseduje ono sto cemo da mu prosledimo
            print('preuzet projekat: ', {projekat.tip})
        else:
            print('donestite i mockup')


firma1 = Firma("djole", 2000, True)
firma1.zaposliNove(100)
print(firma1.brojZaposlenih)
firma1.otkazi(3)
print(firma1.brojZaposlenih)
firma1.preuzmiProekat(fitApp)
firma1.preuzmiProekat(webApp)
print(webApp.preuzetaZaRad) #provera da li je preuzmiprokat uspelo