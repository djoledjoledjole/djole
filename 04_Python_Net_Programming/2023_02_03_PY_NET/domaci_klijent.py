import socket

c = socket.socket(type=socket.SOCK_DGRAM) # type=socket.SOCK_DGRAM - UDP protokol

for i in range(999):
    c.sendto(f"dobardan {i}".encode(),("127.0.0.1", 9000))
c.close()