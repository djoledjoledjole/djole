class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
        self.__jmbg = ""  # privatno svojstvo!
    
    def get_jmbg(self): 
        if self.__jmbg != "":
            prvi_deo = self.__jmbg[0:9]                    # MENI BOLJI METOD od sledeceg
            izlaz = prvi_deo + "****"
            return izlaz
        else:
            print("nije postavljen jmbg")

    def set_jmbg(self, vrednost): # dodela jmbg
        if isinstance(vrednost, str):
            if len(vrednost) == 13:
                self.__jmbg = vrednost
            else:
                print("jmbg mora 13 karaktera")
        else:
            print('mora da bude string tipa')


o1 = Osoba('sofija', 'sofilic')
print(o1.get_jmbg())
o1.set_jmbg("1234567891011")
print(o1.get_jmbg())