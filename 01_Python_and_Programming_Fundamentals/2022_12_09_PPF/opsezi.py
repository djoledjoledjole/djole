#---------OPSEZI< globalni i lokalni----------------------
x = 10 #GLOBALNA PROMENJLJIVA

def poruka():
    print('hello')
    print(x)
    global a # MORA DA SE "GLOBAL _" DA BI BILA GLOBALNA
             # plus mora da se pozove pre koriscenja  
    a = 12 #LOKALNA PROMRNJLJIVA

poruka()
print(a)