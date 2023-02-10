import socket


c = socket.socket(type=socket.SOCK_DGRAM)

for i in range(1000):
    c.sendto(f"dobar dan {i}".encode(),("gresnik.com", 9000))