# #VEZBA PITANJE ODGOVOR
import socket

# klijent = socket.socket() # po difoltu je stimovani sockt(tcp)
# klijent.connect(('gresnik.com', 7878))

# pitanje = b'ko je najlepsi\n'
# klijent.send(pitanje)
# odgovor = klijent.recv(512)
# print(odgovor.decode())
# #-------------------------------------
# #VEZBA KALKULATOR
# c = socket.socket() # po difoltu je stimovani sockt(tcp)
# c.connect(('gresnik.com', 7880))

# broj1 = 6
# broj2 = 8
# znak  = '*'

# pitanje = f"{broj1}|{broj2}|{znak}\n"
# c.send(pitanje.encode())
# odgovor = c.recv(128).decode().strip()
# print(odgovor)
#-------------------------------------

s = socket.socket(type=socket.SOCK_DGRAM) # type=socket.SOCK_DGRAM - UDP protokol
s.bind(('0.0.0.0', 9000)) # SLUSA NA SVIM ADAPTERIMA NA PORTU 9000

while True:
    paket = s.recv(128)
    print(paket)