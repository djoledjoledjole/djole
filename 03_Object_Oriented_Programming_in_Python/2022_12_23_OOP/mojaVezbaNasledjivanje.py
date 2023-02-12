# IGRAC   -   ORUZJE    HELTI    VEST    BOMBA

class Igrac:
    def __init__(self, name, nick, godine):
        self.name = name
        self.nick = nick
        self.godine = godine

    def baca_bombu(self):
        print('baca bombu')

class Oruzje:
    def __init__(self, oruzje):
        self.oruzje = oruzje

class Helti:
    def __init__(self, helti):
        self.helti = helti
    def puca_na_njega(self, puca):
        self.helti -= 1


p1 = Igrac('marko', 'mare', 25), Oruzje('m4'), Helti(100)
p1.puca_na_njega()
