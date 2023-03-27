import http.server as server


def proveri(uname,password):
    fajl = open('users.txt','r')
    while linija := fajl.readline():
        un,pw = linija.split(',')
        if un == uname:
            if password == pw:
                return 0
            else:
                return -1
    else:
        return -2
    

class Hender(server.SimpleHTTPRequestHandler):
    def do_POST(self):
        duzina = int(self.headers["Content-Lenght"])
        podaci = self.rfile.read(duzina).decode()
        res = proveri(podaci['username'],podaci["password"])
        if res == 0:
            pass
        elif res == -1:
            pass
        else:
            pass
    
print(proveri('djole','zec'))

class Hendler(server.SimpleHTTPRequestHandler):
    pass

server.HTTPServer(("0.0.0.0", 8000), Hendler).serve_forever()