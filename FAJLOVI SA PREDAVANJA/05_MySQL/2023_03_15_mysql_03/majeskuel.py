import mysql.connector as conn    # PREKO OVOGA KORISTIMO MYSQL

print(conn)

konekcija = conn.connect(host='Localhost',username='root',passwd='mysqlosam',database='telefoni1') #SADA JE KONEKTOVAN NA MYSQL SERVER

cur = konekcija.cursor() # OVO SIMBOLIZUJE JEDNU SESIJU NA BAZI PODATAKA
cur.execute("drop database telefoni2") # OVO SALJE KOMANDE
