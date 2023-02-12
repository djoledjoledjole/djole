##########################################################
# class Animal:
#     colour  = ''
#     legs = 0

# zirafa = Animal()                 # OVO JE BEZ KONSTRUKTORA (__init__)
# zirafa.colour = 'yellow'
# zirafa.legs = 4

# print(zirafa.colour, zirafa.legs)
#-------------------------------------------------
# class Animal:
#     def __init__(self, colour, legs):
#         self.colour = colour
#         self.legs = legs                        # OVO JE SA KONSTRUKTOROM, MNOGO LAKSE

# zirafa = Animal('yellow', 4)
# print(zirafa.colour, zirafa.legs)
###########################################################
# class Igrac:
#     def __init__(self, oruzje, helti, metkovi):
#         self.oruzje = oruzje
#         self.helti = helti
#         self.metkovi = metkovi

#     def kolicina_metkova(self, broj_metkova):
#         self.broj_metkova = self.metkovi
#     ...            ..........     .......
###########################################################################
# lista = [1, 4564, 'fghgfjgfhj']
# lista2 = 1
# for i in lista:
#     lista2 += 2
# print(lista2)
######################################################################
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class B:
    def __init__(self, c, d):
        self.a = c
        self.b = d
        print(c)

object1 = B('malo a', 'malo b')
print(object1.a) 

print()