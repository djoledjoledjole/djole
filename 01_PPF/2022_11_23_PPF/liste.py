# osoba = ['sofija', 25, 'plava', False]

# for i in range(len(osoba)):
#     print(osoba[i])

# for i in osoba:
#     print(i)


# voceIpovrce = ['jabuka', 'beli luk', 'crni luk', 'banana', 'mandarina', 'krastravac']

# for i in voceIpovrce:
#     print(i)

# for i in range(len(voceIpovrce)):
#     print('na indeksu', i, voceIpovrce[i]

# for i, v in enumerate(voceIpovrce):
#     print('indeks', i, 'stavka', v)

# automobil = ['opel', 'citroen', 'mercedes', 'bmw', 'kia']

# for pozicija, auto in enumerate(automobil):
#     print('pozicija', pozicija, 'auto', auto)

# automobil.append('jugo')
# print(automobil)

# automobil[2] = 'opel corsa'
# print(automobil)

# del automobil[3]
# print(automobil)




# automobil = ['opel', 'citroen', 'mercedes', 'bmw', 'kia', 'audi']

# automobiliNaAkciji = []

# for i in range(len(automobil)):
#     if i == 1 or i == 2 or i == 3:
#         automobiliNaAkciji.append(automobil[i])

# automobiliNaAkciji = automobil[1:4]

# print(automobiliNaAkciji)


a = [1, 34, 4, 5, 12, 8, 9]
parni = []
neparni = []
for i in a:
    if i % 2 == 0:
        parni.append(i)
    else:
        neparni.append(i)

print('parni', parni)
print('neparni', neparni)