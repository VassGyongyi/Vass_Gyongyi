kor_lista =[]
def kor():

    i = 0
    print('Add meg öt ember korát 0-120 év között: ')
    while i< 5:

       kor = int(input(''))
       if kor < 0 or kor > 120:
           input('Helytelen érték! Add meg újra!')


       kor_lista.append(kor)
       i +=1
    j = 0
    kimenet = ""
    while j < len(kor_lista):
        if j == len(kor_lista)-1:
            kimenet += str(kor_lista[j])
        else:
            kimenet += str(kor_lista[j]) + ":"
        j += 1
    print(kimenet)

def elso_idos(kor_lista):
    i = 0
    index = -1
    while i < len(kor_lista):
        if int(kor_lista[i]) > 70:
            index = i
            return index
        i += 1
def konzolra_ir():
    print('II/D, E:')
    print(f'\tElső idős ember korának helye a listában: {elso_idos(kor_lista)}')

def fajl_ir():
    f = open('oreg.txt','w',encoding='utf-8')
    f.write(f'II/F:\n\tElső idős ember korának helye a listában: {elso_idos(kor_lista)}')
    f.close()
