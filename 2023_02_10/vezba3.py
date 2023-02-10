import socket


server = socket.socket(type=socket.SOCK_DGRAM)
server.bind(("0.0.0.0", 9000))

while True:
    paket,adresa = server.recvfrom(128)
    print(paket,adresa)