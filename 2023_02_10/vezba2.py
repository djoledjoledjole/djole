import socket

client = socket.socket()
client.connect(('gresnik.com', 7880))

broj1 = 6
broj2 = 8
znak = '*'

poruka = f"{broj1}|{broj2}|{znak}\n"

client.send(poruka.encode())

odgovor = client.recv(512).decode().strip()
print(odgovor)