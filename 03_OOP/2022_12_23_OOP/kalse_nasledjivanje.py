class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
    
    def predstavi_se(self):
        return f"ja sam {self.ime} {self.prezime}"

osoba1 = Osoba("Sofija", "Sofilic")
print(osoba1.ime)
print(osoba1.predstavi_se())
poruka_osobe1 = osoba1.predstavi_se()
print(poruka_osobe1)

# RODITELJSKA klasa je od koje se nasledjuje
# POTOMAK klasa je ona koja nasledjuje
# PARENT - RODITELJ - SUPER
# CHILD - POTOMAK - SELF

class Student(Osoba):
    def __init__(self, ime, prezime, broj_indeksa): # poziv roditeljskog konstruktora
        super().__init__(ime, prezime)
        self.broj_indeksa = broj_indeksa

    def predstavi_se(self):
        # return 'OVA OSOBA JE STUDENT'
        # return f"ja sam {self.ime} {self.prezime}, moj broj indeksa je {self.broj_indeksa}"
        return f"{super().predstavi_se()}, moj broj indeksa je {self.broj_indeksa}"

student1 = Student("Sofija", "Sofilic", "55/22")
print(student1.predstavi_se())

class Profesor(Osoba):
    def __init__(self, ime, prezime, programski_jezik):
        super().__init__(ime, prezime)
        self.programski_jezik = programski_jezik

    def predstavi_se(self):
        return f"{super().predstavi_se()}, predajem {self.programski_jezik}"

prof = Profesor('aleksandra', 'lazarevic', 'java script')
print(prof.predstavi_se())