from django.http import HttpResponse
from django.shortcuts import render

# def naslovnastrana(req):    OVO JE SAMO DOK JE HTML BIO TEKS
#     odgovor =  HttpResponse()
#     odgovor.content = 'opa evo je naslovna strana <br> <a href="/detalji">idi na detalje</a>'
#     return odgovor

def naslovnastrana(request):
    odgovor = render(request, 'index.html')    # ovo ucitava sablone iz templates
    return odgovor

def detalji(req):
    odgovor = HttpResponse()
    odgovor.content = 'pozdrav iz detalja <br> <a href="/">idi nazad</a>'
    return odgovor

def proba(request):
    odgovor = render(request, 'proba.html')
    return odgovor