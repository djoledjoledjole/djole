
# recnik = {
#     'a':'a1', 
#     'b':'b1'
#     }

# # print(recnik)
# # print(recnik['a'])
# # print(recnik['b'])

# for k,v in recnik.items():
#     print(k, ":", v)
######################################
# poruke = {'en':'hello', 'sr':'zdravo', 'de':'hallo'}

# jezici = input('enter language: ')

# if jezici == 'en' or jezici == 'sr' or jezici == 'de':
#     print(poruke[jezici])
######################################
# poruke = {'en':'hello', 'sr':'zdravo', 'de':'hallo'}

# # print("ENGLESKI: ", poruke['en'])
# # print("SRPSKI: ", poruke['sr'])
# # print("NEMACKI: ", poruke['de'])

# for k,v in poruke.items():
#     if k == 'en':
#         print('ENGLESKI: ', v)
#     elif k == 'sr':
#         print('SRPSKI: ', v)
#     elif k == 'de':
#         print('NEMACKI: ', v)
######################################
# selekcija = {
#     'drzava' : 'srbija',
#     'brojPobeda' : 0,
#     'bojeDresova' : ['crvena', 'plava', 'bela'],
#     'brojeviIgraca' : [9, 5, 13, 20]
# }

# for k,v in selekcija.items():
#     print('kljuc: ', k)
#     print("vrednost", v)
#     if k == 'bojeDresova':
#         for boja in v:
#             print('boja: ', boja)
#     if k == 'brojeviIgraca':
#         for brojevi in v:
#             print('brojevi:', brojevi)
######################################
# automobili = {
#     'marka':'citroen',
#     'model':'c3',
#     'boje':['crvena','bela','crna'],
#     'aluFelne': False,
#     'godiste':2017
# }

# for v, k in automobili.items():
#     if v=='marka':
#         print('marka: ', k)
#     elif v=='model':
#         print('model: ', k)
#     elif v=='boje':
#         for boja in k:
#             print('boja: ', boja)
#     elif v=='aluFelne':
#         if k:
#             print('ima alufelne')
#         else:
#             print('nema alufelne :(')
#     elif v=='godiste':
#         print('godiste: ', k)
########################################
a=False
if a:
    print('a')
if a == False:
    print('not a')