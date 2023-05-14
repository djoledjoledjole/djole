import time, threading # NIJE URADJENO

brava = threading.Lock()

class Vozilo:
    def __init__(self, tip, brzina):
        self.tip = tip
        self.brzina = brzina
        self.trenutna_pozicija = 0
        self.destinacija = 1000

    def kreni(self):
        print("vozilo je krenulo..")
        while self.trenutna_pozicija < self.destinacija:
            brava.acquire()
            print(f"{self.tip} : {self.trenutna_pozicija}m")
            brava.release()
            time.sleep(0.3)
            self.trenutna_pozicija += self.brzina
        else:
            brava.acquire()
            print("vozilo je stiglo")
            brava.release()

auto1 = Vozilo('auto', 10)
auto1.kreni()
bedzigl1 = Vozilo('bedzigl', 2)
bedzigl1.kreni()