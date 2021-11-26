class Piezas:
    #La pieza de Ajedrez recibe como parametro el nombre, color y posicion
    def __init__(self,nombre,color,posicion):
        self.nombre = nombre
        self.color = color
        self.posicion = posicion

class Peon(Piezas):

    def Mover(self, donde_mover, tablero):
        
        if tablero[donde_mover[0]][donde_mover[1]] == "":
            
            if self.color == "Negro":
                if tablero[self.posicion[0]+1][self.posicion[1]] == tablero[donde_mover[0]][donde_mover[1]] and [self.posicion[0]+1,self.posicion[1]] == donde_mover:
                    self.antigua_posi = self.posicion
                    self.posicion = donde_mover
                    return True
                else:
                    return False

            if self.color == "Blanco":
                if tablero[self.posicion[0]-1][self.posicion[1]] == tablero[donde_mover[0]][donde_mover[1]] and [self.posicion[0]-1,self.posicion[1]] == donde_mover:
                    self.antigua_posi = self.posicion
                    self.posicion = donde_mover
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def Comer(self,rival,tablero):
        
        if rival.color != self.color:

            if self.color == "Blanco":
                if tablero[self.posicion[0]+1][self.posicion[1]-1] == tablero[rival.posicion[0]][rival.posicion[1]] :
                    self.antigua_posi = self.posicion
                    self.posicion = rival.posicion
                    return True
                elif tablero[self.posicion[0]+1][self.posicion[1]+1] == tablero[rival.posicion[0]][rival.posicion[1]] :
                    self.antigua_posi = self.posicion
                    self.posicion = rival.posicion
                    return True
                else:
                    return False
            if self.color == "Negro":
                if tablero[self.posicion[0]-1][self.posicion[1]-1] == tablero[rival.posicion[0]][rival.posicion[1]]:
                    self.antigua_posi = self.posicion
                    self.posicion = rival.posicion
                    return True
                elif tablero[self.posicion[0]-1][self.posicion[1]+1] == tablero[rival.posicion[0]][rival.posicion[1]]:
                    self.antigua_posi = self.posicion
                    self.posicion = rival.posicion
                    return True
                else:
                    return False        
        else:
            return False


class Caballo(Piezas):
    def Mover(self,donde_mover, tablero):    
        if tablero[donde_mover[0]][donde_mover[1]] == "":
            #parte de atras
            if tablero[self.posicion[0]+2][self.posicion[1]+1] == tablero[donde_mover[0]][donde_mover[1]] and [self.posicion[0]+2,self.posicion[1]+1] == donde_mover:
                self.antigua_posi = self.posicion
                self.posicion = donde_mover
                return True
            
            elif tablero[self.posicion[0]+2][self.posicion[1]-1] == tablero[donde_mover[0]][donde_mover[1]] and [self.posicion[0]+2,self.posicion[1]-1] == donde_mover:
                self.antigua_posi = self.posicion
                self.posicion = donde_mover
                return True

            elif tablero[self.posicion[0]+1][self.posicion[1]+2] == tablero[donde_mover[0]][donde_mover[1]] and [self.posicion[0]+1,self.posicion[1]+2] == donde_mover:
                self.antigua_posi = self.posicion
                self.posicion = donde_mover
                return True

            elif tablero[self.posicion[0]+1][self.posicion[1]-2] == tablero[donde_mover[0]][donde_mover[1]] and [self.posicion[0]+1,self.posicion[1]-2] == donde_mover:
                self.antigua_posi = self.posicion
                self.posicion = donde_mover
                return True    

            #parte de adelante

            elif tablero[self.posicion[0]-2][self.posicion[1]+1] == tablero[donde_mover[0]][donde_mover[1]] and [self.posicion[0]-2,self.posicion[1]+1] == donde_mover:
                self.antigua_posi = self.posicion
                self.posicion = donde_mover
                return True
        
            elif tablero[self.posicion[0]-2][self.posicion[1]-1] == tablero[donde_mover[0]][donde_mover[1]] and [self.posicion[0]-2,self.posicion[1]-1] == donde_mover:
                self.antigua_posi = self.posicion
                self.posicion = donde_mover
                return True

            elif tablero[self.posicion[0]-1][self.posicion[1]+2] == tablero[donde_mover[0]][donde_mover[1]] and [self.posicion[0]-1,self.posicion[1]+2] == donde_mover:
                self.antigua_posi = self.posicion
                self.posicion = donde_mover
                return True

            elif tablero[self.posicion[0]-1][self.posicion[1]-2] == tablero[donde_mover[0]][donde_mover[1]]  and [self.posicion[0]-1,self.posicion[1]-2] == donde_mover:
                self.antigua_posi = self.posicion
                self.posicion = donde_mover
                return True    

            else:
                return False
        else:
            return False
    
    def Comer(self,rival,tablero):

        if rival.color != self.color:
            
            if tablero[self.posicion[0]+2][self.posicion[1]+1] == tablero[rival.posicion[0]][rival.posicion[1]]:
                self.antigua_posi = self.posicion
                self.posicion = rival.posicion
                tablero[rival.posicion[0]][rival.posicion[1]] = ""
                return True
            
            elif tablero[self.posicion[0]+2][self.posicion[1]-1] == tablero[rival.posicion[0]][rival.posicion[1]]:
                self.antigua_posi = self.posicion
                self.posicion = rival.posicion
                tablero[rival.posicion[0]][rival.posicion[1]] = ""
                return True

            elif tablero[self.posicion[0]+1][self.posicion[1]+2] == tablero[rival.posicion[0]][rival.posicion[1]]:
                self.antigua_posi = self.posicion
                self.posicion = rival.posicion
                tablero[rival.posicion[0]][rival.posicion[1]] = ""
                return True

            elif tablero[self.posicion[0]+1][self.posicion[1]-2] == tablero[rival.posicion[0]][rival.posicion[1]]:
                self.antigua_posi = self.posicion
                self.posicion = rival.posicion
                tablero[rival.posicion[0]][rival.posicion[1]] = ""
                return True    

            #parte de adelante

            elif tablero[self.posicion[0]-2][self.posicion[1]+1] == tablero[rival.posicion[0]][rival.posicion[1]]:
                self.antigua_posi = self.posicion
                self.posicion = rival.posicion
                tablero[rival.posicion[0]][rival.posicion[1]] = ""
                return True
        
            elif tablero[self.posicion[0]-2][self.posicion[1]-1] == tablero[rival.posicion[0]][rival.posicion[1]]:
                self.antigua_posi = self.posicion
                self.posicion = rival.posicion
                tablero[rival.posicion[0]][rival.posicion[1]] = ""
                return True

            elif tablero[self.posicion[0]-1][self.posicion[1]+2] == tablero[rival.posicion[0]][rival.posicion[1]]:
                self.antigua_posi = self.posicion
                self.posicion = rival.posicion
                tablero[rival.posicion[0]][rival.posicion[1]] = ""
                return True

            elif tablero[self.posicion[0]-1][self.posicion[1]-2] == tablero[rival.posicion[0]][rival.posicion[1]]:
                self.antigua_posi = self.posicion
                self.posicion = rival.posicion
                tablero[rival.posicion[0]][rival.posicion[1]] = ""
                return True    
            else:
                return False
                

class Alfil(Piezas):
    def i():
        return
class Torre(Piezas):
    def i():
        return
class Reina(Piezas):
    def i():
        return
class Rey(Piezas):
    def i():
        return