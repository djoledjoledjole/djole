import http.server as srv

class Rukovalac(srv.SimpleHTTPRequestHandler):
    pass

srv.HTTPServer(("0.0.0.0", 8000), Rukovalac).serve_forever()

