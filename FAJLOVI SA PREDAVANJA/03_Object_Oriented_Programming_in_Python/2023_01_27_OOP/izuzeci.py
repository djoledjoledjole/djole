class WrongOperation(Exception):
    pass


def kalkulator(broj1, broj2, operacija):
    dostuple_operacije = ['+','-','*','/']
    if operacija not in dostuple_operacije:
        raise WrongOperation
    else:
        if operacija == "+":
            print(int(broj1)+int(broj2))
        elif operacija == "-":
            print(broj1-broj2)
        elif operacija == "*":
            print(broj1*broj2)
        elif operacija == "/":
            print(broj1/broj2)

try:
    kalkulator('a',0,'+')
except WrongOperation:
    print('pogresili ste operaciju')
except ZeroDivisionError:
    print('ne moze sa nulom')
except ValueError:
    print('greska vrednost')
except Exception:
    print('nek GRESKA')
