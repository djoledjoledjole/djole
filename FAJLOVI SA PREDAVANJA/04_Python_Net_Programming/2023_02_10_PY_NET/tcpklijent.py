import socket


c = socket.socket()
c.connect(("127.0.0.1", 9000))
c.semd(b"dota.txt")
fajl = c.recv(2000)
print(fajl)