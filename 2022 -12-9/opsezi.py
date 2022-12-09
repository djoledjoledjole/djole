############ opsezi #################
x = 10 #GLOBALNA PROMENJLJIVA

def poruka():
    print('hello')
    print(x)
    a = 15 #lokalna promenjljiva

def proba():
    global y
    y = 15

proba() #mora da se pozove funkcija da bi se pojavilo y
print(y)

#################################################################
