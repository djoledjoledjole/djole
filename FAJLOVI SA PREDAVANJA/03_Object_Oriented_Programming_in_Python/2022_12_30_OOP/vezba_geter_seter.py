# #--------------------------------------#
# #   PRIMER GETTER SETTER PYTHOIN WAY   #
# #--------------------------------------#
class Automobil:
    def __init__(self, boja, model):
        self.boja = boja
        self.model = model
        self.__registracija = 0

    @property
    def registracija(self):
       return self.__registracija

    @registracija.setter
    def registracija(self, registracija):
        self.__registracija = registracija

a1 = Automobil('crvena', 'tesla')
a1.registracija = 123456
print(a1.registracija)
#---------------------------------------#

# class Automobil:
#     def __init__(self, boja):
#         self.boja = boja
#         self.__registracija = ''

#     @property
#     def registracija(self):
#         return self.__registracija
#     @registracija.setter
#     def registracija(self, vrednost):
#         self.__registracija  = vrednost

# automobil1 = Automobil("crvena")
# automobil1.registracija = '123'
# print(automobil1.registracija)

#---------------------------------------#
class Auto:
    def __init__(self, boja):
        self.boja = boja
        self.__registracija = ''
    
    def get_registracija(self):
        return self.__registracija

    def set_registracija(self, vrednost):
        self.__registracija = vrednost

auto1 = Auto('zuta')
auto1.set_registracija('123')
print(auto1.get_registracija())
#---------------------------------------#