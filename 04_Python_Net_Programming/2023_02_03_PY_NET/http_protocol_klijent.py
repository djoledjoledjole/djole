# Vreme početka: 10.2.2023. 2:08

import socket

client = socket.socket()
client.connect(("127.0.0.1", 9000))
               #              ZAHTEV              #
client.send((b"GET /http_protocol_fajlovi/fajl1.txt HTTP/1.1"))  #GET je opis zahteva  #HTTP/1.1 je verzija protokola
zaglavlje = client.recv(2000)
print(zaglavlje)
telo = client.recv(2000)
print(telo)