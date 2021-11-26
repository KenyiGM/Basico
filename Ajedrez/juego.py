
class Alfil():

    def __init__(self,nombre,color,posicion):
        self.nombre = nombre
        self.color = color
        self.posicion = posicion

    def Mover(self, donde_mover, tablero):
        if tablero[donde_mover[0]][donde_mover[1]] == "":
            for x in range(1,len(tablero)):
                if tablero[self.posicion[0]+x][self.posicion[1]+x] == tablero[donde_mover[0]][donde_mover[1]] and [self.posicion[0]+x,self.posicion[1]+x] == donde_mover:
                    self.antigua_posi = self.posicion
                    self.posicion = donde_mover
                    return True
                elif tablero[self.posicion[0]-x][self.posicion[1]-x] == tablero[donde_mover[0]][donde_mover[1]] and [self.posicion[0]-x,self.posicion[1]-x] == donde_mover:
                    self.antigua_posi = self.posicion
                    self.posicion = donde_mover
                    return True    
                if tablero[self.posicion[0]+x][self.posicion[1]+x] != "":
                    break                
            return True
        else:
            return False

    def Comer(self,rival,tablero):
        if rival.color != self.color:
            if self.color == "Blanco":
                return True
            if self.color == "Negro":
                return True


ab1 = Alfil("Alfil","Blanco",[0,0])
an1 = Alfil("Alfil","Negro",[2,2])

lista1=[ab1,"","","","","","",""]
lista2=["","","","","","","",""]
lista3=["","",an1,"","","","",""]

tablero=[lista1,lista2,lista3]

if ab1.Mover([1,1],tablero) == True:
    tablero[ab1.antigua_posi[0]][ab1.antigua_posi[1]] = ""
    tablero[ab1.posicion[0]][ab1.posicion[1]] = ab1
else:
    print("Algo salio mal")

for x in range(len(tablero)):
    print(tablero[x])


def tablero():
    lista1=["","","","","","","",""]
    lista2=["","","","","","","",""]
    lista3=["","","","","","","",""]
    lista4=["","","","","","","",""]
    lista5=["","","","","","","",""]
    lista6=["","","","","","","",""]
    lista7=["","","","","","","",""]
    lista8=["","","","","","","",""]

    tablero=[lista1,lista2,lista3,lista4,lista5,lista6,lista7,lista8]

def juego():
    print()

