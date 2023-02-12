import random
import time

class Team:
    def __init__(self, naziv_tima):       #inicijalizator je isto sto i konstruktor!!!
        self.naziv_tima = naziv_tima

class Score:
    domaci = 0
    gosti = 0
                       # TIPOVI PROMENJLJIVIH
class Match:         # Team()Team() Int,   Score   - ....povlaci iz tih clasa
    def __init__(self, tim1, tim2, minuti, score):
        self.domaci = tim1
        self.gosti = tim2
        self.minuti = minuti
        self.score = score

    def start(self):
        print('zapoceta je utakmica')
        while True:
            
            # self.score.domaci = random.randint(0,10)    #ovo daje random boj golova
            # self.score.gosti = random.randint(0,10)     #ovo daje random boj golova
            
            nas_broj = 5
            if nas_broj == random.randint(0,10):
                self.score.domaci += 1
            elif nas_broj == random.randint(0,10):
                self.score.gosti +=1


                #    iz Match()   iz Team()     iz Match()   iz Team()
            print(f'{self.domaci.naziv_tima} - {self.gosti.naziv_tima}')
            print(f'{self.score.domaci} - {self.score.gosti}')

            time.sleep(0.3) # sekund pravi pauziizmedju izvrsavanja

            self.minuti +=1

            if self.minuti >= 90:
                print('utakmica je gotova')
                return

tim1 = Team('crvena zvezda')
tim2 = Team('partizan')

utakmica = Match(tim1, tim2, 0, Score())
utakmica.start()