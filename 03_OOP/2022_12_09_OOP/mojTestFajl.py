class Igrac:
    hp = 0
    nick = ''
    weapon = ''
    granate = False
    def bacaBombu(self):  #METODA
        print('bombu je bacio', self.nick)

igracDjole = Igrac()
igracDjole.hp = 99
igracDjole.nick = "MUDA"
igracDjole.weapon = "MK"
igracDjole.granate = True

igracDjole.bacaBombu()
oruzje = igracDjole.weapon
print(igracDjole.nick, 'popseduje', oruzje, 'od oruzja')