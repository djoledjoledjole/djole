import http.server as srv
import datetime
import urllib.parse as parse

model = {
    "1":{
        "naziv":"Fender Stratocaster YJM WH",
        "slika":"https://images.static-thomann.de/pics/bdb/145461/7318383_800.jpg",
        "cena":2300
    },
    "5":{
        "naziv":"Ibanez Jem Jr",
        "slika":"https://mixmusiccompany.com/wp-content/uploads/2021/05/Ibanez-JEMJR-WH-2.jpg",
        "cena":500
    },
    "12":{
        "naziv":"Gibson LesPaul Slash",
        "slika":"http://images.musicstore.de/images/1280/gibson-slash-les-paul-standard-appetite-burst_1_GIT0051804-000.jpg",
        "cena":2800
    }
}

class Rukovalac(srv.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()  
        parametri = self.path.split("?")
        izlaz = "" 
        if len(parametri) > 1:
            parametri = dict(parse.parse_qsl(parametri[1]))
            pid = parametri["id"]
            gitara = model[pid]
            izlaz = f"<h3>{gitara['naziv']}</h3><img width=200 src='{gitara['slika']}'/><br><strong>Cena: </strong>{gitara['cena']}<br><br><a href='/'>Nazad</a>"
        else: 
            for kljuc, vrednost in model.items():
                izlaz += f"<a href='?id={kljuc}'>{vrednost['naziv']}</a><br>"

        self.wfile.write(izlaz.encode())



srv.HTTPServer(("0.0.0.0",8000),Rukovalac).serve_forever()