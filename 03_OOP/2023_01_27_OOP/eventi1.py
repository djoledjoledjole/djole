import time

def rezervoar_lampica():
    print('na rezervi ste')
    print('zuta lampica')

def vozi(gorivo, indikator_goriva):
    rezerva_limit = 10
    while gorivo > 0:
        print('voznja')
        time.sleep(0.3)
        gorivo -= 5
        if gorivo <= rezerva_limit:
            indikator_goriva()
    print('prazan')

vozi(40, rezervoar_lampica)