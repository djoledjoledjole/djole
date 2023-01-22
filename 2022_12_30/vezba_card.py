#--------------------------------------#
#   PRIMER GETTER SETTER PYTHOIN WAY   #
#--------------------------------------#
                                     
class Card:
    def __init__(self):
        self.__boja = ''
        
    @property
    def boja(self):
        return self.__boja
    @boja.setter
    def boja(self, vrednost):
        self.__boja = vrednost

karta1 = Card()
karta1.boja = "crvena"
print(karta1.boja)

#--------------------------------------#



# class Card:
#     def __init__(self):
#         self.__broj = 0
#         self.__boja = ''
#         self.__sifra = ''

#     @property
#     def broj(self):
#         return self.__broj
    
#     @property
#     def boja(self):
#         return self.__boja

#     @property
#     def sifra(self):
#         return self.__sifra

#     @broj.setter
#     def broj(self, vrednost):
#         self.__broj = vrednost
    
#     @boja.setter
#     def boja(self, vrednost):
#         self.__boja = vrednost

#     @sifra.setter
#     def sifra(self, vrednost):
#         self.__sifra = vrednost

# karta1 = Card()
# karta1.broj = 13
# print(karta1.broj)


# class Card:
#     def __init__(self):
#         self.__broj = 0
#         self.__boja = ''
#         self.__znak = ''

#     @property
#     def broj(self):
#         return self.__broj
#     @broj.setter
#     def broj(self, vrednost):
#         self.__broj = vrednost

#     @property
#     def boja(self):
#         return self.__boja
#     @boja.setter
#     def boja(self, vrednost):
#         self.__boja = vrednost

#     @property
#     def znak(self):
#         return self.__znak
#     @znak.setter
#     def znak(self, vrednost):
#         self.__znak = vrednost




# karta1 = Card()
# karta1.boja = 'crvena'
# karta1.znak = "herc"
# karta1.broj = '13'

# print(karta1.boja)


#--------------------------------------#
#   PRIMER GETTER SETTER PYTHOIN WAY   #
#--------------------------------------#