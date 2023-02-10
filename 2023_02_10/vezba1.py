import socket


klijent = socket.socket()
klijent.connect(('gresnik.com', 7878))

pitanje = b"ko je najlepsi\n"
klijent.send(pitanje)
odgovor = klijent.recv(512)
print(odgovor.decode().strip())

#----------------------------------------------

