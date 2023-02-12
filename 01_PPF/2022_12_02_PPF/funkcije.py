def ispisi_poruke(): # potpis funkcije
    # telo funkcije
    print("Zdravo")
    print("Danasnji datum je 2.12")
    print("Predavanje pajton")

# poziv funkcije
ispisi_poruke()



                     # -   ulazni parametar funkcije
def pozdravna_poruka(ime):
    print(f"Hello {ime}")


pozdravna_poruka("Sofija")



def prikazi_informacije(ime="", poeni=10):
    print(f"Student: {ime}, poeni: {poeni}")


prikazi_informacije("Sofija", 80)

prikazi_informacije()

def saberi(a = 0, b = 0):
    print(a, b)
    print(a + b)

saberi(b = 20)

#prvi sabirak, drugi, operacija
def kalkulator(a, b, o):
    a = int(input("Unesite prvi broj:"))
    if o == "+":
        print(a + b)
        return a + b
    elif o == "-":
        print(a - b)
        return a - b 
    elif o == "*":
        print(a * b)
        return a * b 
    elif o == "/":
        if b == 0:
            print("Nije dozvoljeno deljenje sa nulom")
        else:
            print(a / b)
            return a * b 
    else:
        print("Proverite opreciju (+, -, *, /)")


kalkulator(int(input("Unesite prvi broj:")), int(input("Unesite drugi broj:")), input("Unesite operaciju broj (+, -, *, /):"))


def info_o_automobilima(automobili):
    pass

lista = ["a", "b", "c"]

len(lista)