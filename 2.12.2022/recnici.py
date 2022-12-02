# # #UMESTO INDEKSA IDE VREDNOST

# # osobaRecnik = {'ime' : 'Sofija', 'godine' : 25, 'plava' : True}
# # print(osobaRecnik)
# # print(osobaRecnik['ime'])
# # print(osobaRecnik['godine'])

# # for k in osobaRecnik:
# #     print(osobaRecnik[k])

# # for (kljuc, vrednost) in osobaRecnik.items():
# #     print('ovo je kljuc', kljuc)
# #     print('ovo je vrednost', vrednost)

# # osoba2 = {}

# # osoba2['ime'] = 'marija'
# # osoba2['ime'] = 'sofija'
# # print(osoba2)

# # del osoba2['ime']
# # print(osoba2)
# ######################################################
# # poruke = {'en':'hello', 'sr':'zdravo', 'de':'hallo'}
# # print(poruke['sr'])

# # jezik = input('unesi jezik: ')
# # if jezik == 'en' or jezik == 'sr' or jezik == 'de':
# #     print(poruke[jezik])
# # else:
# #     print('nemamo ovaj prevod')
# ######################################################
# # poruke = {'en':'hello', 'sr':'zdravo', 'de':'hallo'}

# # for (k, v) in poruke.items():
# #     if k == 'en':
# #         print(f'ENGLESKI: {v}')
# #     if k == 'sr':
# #         print(f'SRPSKI: {v}')
# #     if k == 'de':
# #         print(f'NEMACKI: {v}')
# ######################################################
# # selekcija = {
# #     'drzava':'Srbija', 
# #     'broj pobeda':0,
# #     'boje dresova':['bela','crvena'], 
# #     'brojevi igraca':[9,5,13,20]
# #     }

# # for k, v in selekcija.items():
# #     # print('kljuc: ', k)
# #     # print('vrednost: ', v)
# #     if k == 'boje dresova':
# #         for boja in v:
# #             print('boja: ', boja)
# #     elif k == 'brojevi igraca':
# #         for broj in v:
# #             print('igrac:', broj)
# #     else:
# #         print(f'{k}:{v}')
# #####################################################
# automobili = {
#     'marka' : 'citroen',
#     'model' : 'c3',
#     'boja' : ['crvena', 'bela', 'crna'],
#     'alu_felne' : False,
#     'godiste' : 2017,
#     'kubikaza' : 1.6
# }

# for k, v in automobili.items():

#     if k == 'marka':
#         print(f'marka je: {v}')

#     if k == 'model':
#         print(f'model je: {v}')

#     if k == 'boja':
#         for i in v:
#             print(f'boja je: {i}')
 
#     if k == 'alu_felne':
#         if v == False:
#             print('nema alu felne :(')
#         else:
#             print('ima felne :D')

#     if k == 'godiste':
#         print(f'godiste je: {v}')

#     if k == 'kubikaza':
#         print(F'kubikaza je: {v}')
# #######################################################

# automobili = {
#     "BG-123" : {
#         'marka' : 'citroen',
#         'model': 'c3',
#         'kubikaza' : 1.6,
#         'boje':['crvena', 'bela', 'crna']
#     },
#     "BG-451" : {
#         'marka' : 'opel',
#         'model': 'astra',
#         'kubikaza' : 2.0,
#         'boje':['plava', 'metalik']
#     },
#     "BG-789" : {
#         'marka' : 'audi',
#         'model': 'q2',
#         'kubikaza' : 2.0,
#         'boje':['srebrna', 'metalik']
#         }
# }

# for reg, detalji in automobili.items():
#     # print('REGISTRACIJA', reg)
#     # print('DETALJI', detalji)
#     for k,v in detalji.items():
#         print(f'{k}:{v}')
#     print('============================')
##########################################################

# kursevi = {
#     'ppf' : {
#         'naziv' : 'python fundamentals',
#         'semester' : 1
#     },
#     'oop' : {
#         'naziv' : 'poo',
#         'semestar' : 1
#     }
# }

# for id_kursa, detalji in kursevi.items():
#     for k, v in detalji.items():
#         print(id_kursa, k,v)
##########################################################
# RECNIK: {skup:vrednost}
# SKUPOVI:  ______ = {}
# boje = {'bela', 'plava', 'crvena'}
# print(boje)
# boje.add('zuta')
# print(boje)
# boje.remove("bela")
# print(boje)
##########################################################
