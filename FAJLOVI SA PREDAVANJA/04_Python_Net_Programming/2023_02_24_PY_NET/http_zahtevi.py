import http.server as server  # NE RAD I oD

class ObradaZahteva(server.SimpleHTTPRequestHandler):
    def do_Get(self):
        
        print(self.path)

        parametri = self.path.split("?")[1]

        sadrzaj = "pozdrav"

        sadrzaj = open("neki.html", "r").read()
        sadrzaj = sadrzaj.replace("BOJAA",'lime')
  
        self.wfile.write(f"HTTP/1.1 200 Ok\r\nContent-type: text/html\r\nddf: fdsfsd\r\ndsjdf: sdfdf\r\n\r\n{sadrzaj}".encode())
        print("hello")


s = server.HTTPServer(("0.0.0.0", 8000),ObradaZahteva)
s.serve_forever()