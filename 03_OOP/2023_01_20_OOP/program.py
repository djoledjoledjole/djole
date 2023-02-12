import enum
#enumeracija

class TipoviSkolovanja(enum.Enum):
  # name   = value !!!!!!!     automatski stavlja   self.name   self.value  atribute
    ONLINE = 1
    TRADICIONALNO = 2

print(TipoviSkolovanja.ONLINE.name)
print(TipoviSkolovanja.TRADICIONALNO.value)

class Korisnik:
    def __init__(self, ime, tipSkolovanja):
        self.ime = ime
        self.tipSkolovanja = tipSkolovanja

kor1 = Korisnik('mile', TipoviSkolovanja.ONLINE.name)
print(kor1.tipSkolovanja)

#-----------------------------------------------------------------

class Pol(enum.Enum):
    MUSKI  = 'm'
    ZENSKI = 'z'

odabrani_pol = Pol.MUSKI
#odabran_pol -> name MUSKI value m
print(odabrani_pol.value)

#-----------------------------------------------------------------

for pol in Pol:
    print(pol.name, pol.value)

#-----------------------------------------------------------------

#boje
#navigacija, main, footer
class Boje(enum.Enum):
    NAVIGACIJA = '#284ec9'
    MAIN = '#d8dded'
    FOOTER = '#f7f56f'
 #ovo (enumeracija) ne mora da se instancira!!!!!!
print(Boje.NAVIGACIJA.value)

#----------------------------------------------------------------

class Tipovi_placanja(enum.Enum):
    KES     = 1
    KARTICA = 2
    CEKOVI  = 3

    def __str__(self) -> str:
        return f'naziv: {self.name}, vrednost: {self.value}'

print(Tipovi_placanja.KES)

for tip in Tipovi_placanja:
    print(tip)

odabrano = int(input("odaberite tip placanja  kes-1 kartica-2 cek-3  - "))

for tip in Tipovi_placanja:
    if tip.value == odabrano:
        print(tip)

#----------------------------------------------------------------

