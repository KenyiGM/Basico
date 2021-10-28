#Este programa intenta encontrar todos los numeros Amigos o Perfectos !!Cuidado es Automatico
def main():
    numero = 0
    while numero >= 0:
        numero += 1
        sumx = 0
        sumy = 0
        for x in range(1,numero):
            if numero % x == 0:
                sumx +=x
        for y in range(1,sumx):
            if sumx % y == 0:
                sumy += y
        if sumy == sumx:
            print(numero,"Es numero Perfecto")
        elif sumy == numero:
            print(numero,"Es numero Amigo")

if __name__ == "__main__":
    main()
