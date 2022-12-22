import random
import time
class Tim:
    def __init__(self, nazivTima):
        self.nazivTima = nazivTima

class Skor:
    domaci = 0
    gosti =  0

class Mec:     #       tim   tim   int     skor
    def __init__(self, tim1, tim2, minuti, skor): #ovo se zove konstruktor
        self.domaci = tim1
        self.gosti = tim2
        self.minuti = minuti
        self.skor = skor.Skor()

    def start(self):
        print('utakmica je pocela')
        
        while True:
            self.skor.domaci = random.randint(0,10)
            self.skor.gosti = random.randint(0, 10)

            nas_broj_tim_1 = 5
            nas_broj_tim_2 = 7

            if nas_broj_tim_1 == random.randint(0,10):
                self.skor.domaci +=1
                self.skor.gosti +=0

            if nas_broj_tim_2 == random.randint(0,10):
                self.skor.domaci +=0
                self.skor.gosti +=1

            print(f'{self.domaci.nazivTima}-{self.gosti.nazivTima}')
            print(f'{self.domaci.skor}:{self.gosti.skor}')
            
            time.sleep(5)
            
            self.minuti += 1
            
            if self.minuti >= 90:
                print('utakmica je gotova')
                return
    
tim1 = Tim('Partizan')
tim2 = Tim('Crvena zvezda')

utakmica = Mec(tim1, tim2, 0, Skor())
utakmica.start()
