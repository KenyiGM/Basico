from random import sample


def generador_sudoku():
    
    # lo puse asi para referenciar mejor los bloques
    block01 , block02 ,block03 ,block04 ,block05 ,block06 ,block07 ,block08 ,block09 = [],[],[],[],[],[],[],[],[]

    tabla = [block01,block02,block03,block04,block05,block06,block07,block08,block09]

    #tener una lista ordenada me ayuda a que todos los numeros esten en sucesión para sortear
    lista_numeros = [1,2,3,4,5,6,7,8,9]

    lista_sorteo = lista_numeros

    lista_sorteo = sample(lista_sorteo,9)

    a = lista_sorteo[0:3]
    b = lista_sorteo[3:6]
    c = lista_sorteo[6:9]

    block01 += lista_sorteo

    lista_n = [b,c,a]

    for x in range(3):
        for y in range(3):
            block02.append(lista_n[x][y])

    lista_n = [c,a,b]

    for x in range(3):
        for y in range(3):
            block03.append(lista_n[x][y])

    #cambiar la posicion de las variables de la lista para que no coincidan con los valores anteriores
    a = [a[-2],a[-1],a[0]]
    b = [b[-2],b[-1],b[0]]
    c = [c[-2],c[-1],c[0]]

    #cambiar la posicion de las listas a, b y c para que no coincidan entre ellas en fila
    lista_n = [a,b,c] 
    for x in range(3):
        for y in range(3):
            block04.append(lista_n[x][y])

    lista_n = [b,c,a]
    for x in range(3):
        for y in range(3):
            block05.append(lista_n[x][y])

    lista_n = [c,a,b]
    for x in range(3):
        for y in range(3):
            block06.append(lista_n[x][y])

    a = [a[-2],a[-1],a[0]]
    b = [b[-2],b[-1],b[0]]
    c = [c[-2],c[-1],c[0]]

    lista_n = [a,b,c]
    for x in range(3):
        for y in range(3):
            block07.append(lista_n[x][y])

    lista_n = [b,c,a]
    for x in range(3):
        for y in range(3):
            block08.append(lista_n[x][y])

    lista_n = [c,a,b]
    for x in range(3):
        for y in range(3):
            block09.append(lista_n[x][y])
    
    return tabla