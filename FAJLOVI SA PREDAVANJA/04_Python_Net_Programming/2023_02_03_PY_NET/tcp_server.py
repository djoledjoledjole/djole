import socket

server = socket.socket()
server.bind(("0.0.0.0", 9000))
server.listen()

client, adresa = server.accept() # Kada se neko nakaci na ovaj server obavi se hendsejk i iz njega se izvuce IP adresa i port, stavi se u soket, adresa se stavi u promenjljivu, to vrati ova metoda accept. Time je ostvarena TCP konekcija. Mozete da pisete, mozete da citate, odvojena dva strima..
# Dalje se komunicira preko aplikativnog protokola. APLIKATIVNI PROTOKOL je set pravila koji postuju dva sagovornika, koja prethodno imaju uspostavljen neki odnos uz pomoc tansportnog protokola (profine reci).

fajl = open("tcp_fajl_za_slanje.txt", "rb") #ovo je samo string dok se ne uradi sledeci korak.. sadrzaj_fajla = fajl.read()
sadrzaj_fajla = fajl.read() # ovo je sad binarni sadrzaj procitanog fajla
client.send(sadrzaj_fajla)
