#---------------------------------------------#
#            E N U M E R A C I J A            #
#---------------------------------------------#
import enum

class Boje(enum.Enum):
    #name          #value
    OKVIR       = '#897984'
    NAVIGACIJA  = '#879779'
    MAIN        = '#898076'
    
    def __str__(self):
        return f"Naziv: {self.name}, vrednost: {self.value}" 
        #self.name i self.value se automatski dodeljuje

print(Boje.MAIN.value)  # .value ili .name daje vrednost ili ime

for boja in Boje:
    print(boja)
#--------------------------------------------------------------#
# Enumeracije - 
# 20.1.2023. 2min
#--------------------------------------------------------------#
# • Enumeracija predstavlja posebnu strukturu čiji je zadatak 
# isključivo skladištenje konstanti nekog tematskog konteksta
#--------------------------------------------------------------#
