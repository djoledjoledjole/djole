import socket

s = socket.socket()
s.bind(("0.0.0.0", 9000))
s.listen()

c,a = s.accept()

odabrani_fajl = c.recv(1024).decode()
fajl = open(odabrani_fajl, "rb")      #r binarno
sadrzaj_fajla = fajl.read()
c.send(sadrzaj_fajla)