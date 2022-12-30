class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
        self.__jmbg = ""  # privatno svojstvo!
    
    @property
    def jmbg(self): 
        if self.__jmbg != "":
            prvi_deo = self.__jmbg[0:9]
            izlaz = prvi_deo + "****"
            return izlaz
        else:
            print("nije postavljen jmbg")

    @jmbg.setter
    def jmbg(self, vrednost): # dodela jmbg
        if isinstance(vrednost, str):
            if len(vrednost) == 13:
                self.__jmbg = vrednost
            else:
                print("jmbg mora 13 karaktera")
        else:
            print('mora da bude string tipa')


o1 = Osoba('sofija', 'sofilic')
o1.jmbg = "1234567891011"
print(o1.jmbg)
