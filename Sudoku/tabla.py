""" 
[1,2,3,4,5,6,7,8,9]
[4,5,6,7,8,9,1,2,3] 
[7,8,9,1,2,3,4,5,6] 
[3,1,2,5,6,4,8,9,7] 
[5,6,4,8,9,7,3,1,2] 
[8,9,7,3,1,2,5,6,4]
[2,3,1,6,4,5,9,7,8]
[6,4,5,9,7,8,2,3,1]
[9,7,8,2,3,1,6,4,5] 

"""

lista_numeros = [1,2,3,4,5,6,7,8,9]

# hay 3 formas de comprobar si ganaste
# horizontal , vertical y bloque

def columna(tabla):
    contador = 0
    for x in range(9):
        lista = []
        for y in range(9):
            lista.append(tabla[y][x])
            lista.sort()
            if lista == lista_numeros:
                contador += 1
    if contador == 9:
        return 1
    else:
        return 0

def fila(tabla):
    contador = 0
    for x in range(len(tabla)):
        lista = []
        for y in range(9):
            lista.append(tabla[x][y])
            lista.sort()
            if lista == lista_numeros:
                contador += 1
    
    if contador == 9:
        return 1
    else:
        return 0


def bloque(tabla):
    block01_p,block02_p ,block03_p ,block04_p ,block05_p ,block06_p ,block07_p ,block08_p ,block09_p = [],[],[],[],[],[],[],[],[]

    tabla_1 = [block01_p,block02_p,block03_p,block04_p,block05_p,block06_p,block07_p,block08_p,block09_p]

    ###
    for x in range(3):
        for y in range(3):
            block01_p.append(tabla[x][y])
        for y in range(3,6):
            block02_p.append(tabla[x][y])
        for y in range(6,9):
            block03_p.append(tabla[x][y])

    ###
    for x in range(3,6):
        for y in range(3):
            block04_p.append(tabla[x][y])
        for y in range(3,6):
            block05_p.append(tabla[x][y])
        for y in range(6,9):
            block06_p.append(tabla[x][y])

    ###
    for x in range(6,9):
        for y in range(3):
            block07_p.append(tabla[x][y])
        for y in range(3,6):
            block08_p.append(tabla[x][y])
        for y in range(6,9):
            block09_p.append(tabla[x][y])

    for x in range(9):
        tabla_1[x].sort()

    contador = 0

    for x in range(9):
        if tabla_1[x] == lista_numeros:
            contador += 1

    if contador == 9:
        return 1
    else:
        return 0
    
