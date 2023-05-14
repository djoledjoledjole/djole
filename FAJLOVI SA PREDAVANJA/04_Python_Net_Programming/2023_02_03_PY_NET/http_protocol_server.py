import socket

server = socket.socket()
server.bind(("0.0.0.0", 9000))
server.listen()

while True:
    client, adresa = server.accept()

    opis = client.recv(1024).decode()
    metod, opis_fajla, verzija = opis.split(" ")
    opis_fajla = opis_fajla.lstrip("/")


    fajl = open(opis_fajla, "rb")
    sadrzaj_fajla = fajl.read()

    opis_odgovora = f"{verzija} 200 Ok\r\n\r\n" # 200 je nesto Ok znaci da je sve u redu

    client.send(opis_odgovora.encode())
    client.send(sadrzaj_fajla)
