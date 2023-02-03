
import time
import socket

class Heroj: 
    def __init__(self):
        self.health = 100
        self.slusaci_promene_healtha = []
    def hit(self,dmg):
        self.health -= dmg
        for slusac_promene_healtha in self.slusaci_promene_healtha:
            slusac_promene_healtha(self.health)

def hud(health):
    print(f"Izmena na health-u ({health})")

def mreza(health):

    s = socket.socket()
    s.connect(("127.0.0.1", 8000))
    print(f"Slanje healtha za heroja, preko mreze ({health})")

def displej(health):
    print(f"Prikaz izmene health-a na displeju ({health})")

wind = Heroj()
wind.slusaci_promene_healtha.append(hud)
wind.slusaci_promene_healtha.append(mreza)
wind.slusaci_promene_healtha.append(displej)

for i in range(10):
    wind.hit(5)
    time.sleep(1)