from Gomba import Gomba
gomba_lista =[]
def feldolgoz():
    f = open('gombak_jav.txt', 'r', encoding='utf-8')
    f.readline().strip()
    sorok = f.readlines()
    f.close()
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("@")
        #print(sor)
        gomba_lista.append(Gomba(sor))

        i += 1

def gombak_szama():
    print('III/A, B:')
    print(f'\tA gombák száma: {len(gomba_lista)}')

def papsapka():
    i = 0
    neve = ""
    while i < len(gomba_lista):
        if gomba_lista[i].nemzetseg == papsapka:
            neve = gomba_lista[i].nev
            return neve
    i += 1
def konzol_kiir():
    print('III/C:')
    print(f'\tAz első papsapkagomba neve: homoki papsapka.{papsapka()}')

def tinoru():
    i = 0
    db = 0
    while i < len(gomba_lista):
        if gomba_lista[i].nemzetseg == "tinorú":
            db += 1
        i += 1
    print('III/D:')
    print(f'A tinóru gombák száma:{db}')