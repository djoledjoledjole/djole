import http.server as srv
import datetime
import urllib.parse as parse


class Rukovalac(srv.SimpleHTTPRequestHandler):
    #pass     #ako je pass onda samo nasledjuje roditeljsku klasu
    def do_GET(self):   #do_GET metoda je roditeljskai ako je ovim prepisemo onda roditeljska nece funkcionisati
        self.send_response(200)
        self.end_headers()
        vreme = datetime.datetime.now()

        parametri = self.path.split('?')[1]
        parametri = dict(parse.parse_qsl(parametri))
        pol = parametri["pol"]
        print(parametri)
        
        #self.path #izdvaja iz zahteva samo parametre, localhost:8000?pol=m  ovo ?pol=m  su parametri
        
        izlaz = f"tacno vreme je {vreme} "
        izlaz += 'gospodine' if pol == "m" else 'gospodjice'
        self.wfile.write(izlaz.encode()) #sta ovde napisemo bice prosledjeno onome koji se povezao na ovaj server



                #adresa    #port #klasa koja rukuje zahtevima
srv.HTTPServer(("0.0.0.0", 8000),Rukovalac).serve_forever()
# ovo je server i kakko god stigne koji zahtev on prosledi Rukovaocu
#kadgod stigne zahtev napravi novu instancu