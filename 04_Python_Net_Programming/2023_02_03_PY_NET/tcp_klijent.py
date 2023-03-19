import socket

client = socket.socket()
client.connect(("127.0.0.1", 9000))
fajl = client.recv(2000)
print(fajl.decode())