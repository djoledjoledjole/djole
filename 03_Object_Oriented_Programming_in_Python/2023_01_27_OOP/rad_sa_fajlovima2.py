import csv

fajl = open('podaci2.csv')

reader = csv.reader(fajl)

broj_python_smer = 0

for red in reader:
    for i in red:
        if i == "python":
            broj_python_smer += 1
        

print(broj_python_smer)