class tablero:
    
    def __init__(self,*args):
        
        self.lista = []
        
        for x in args:
            self.lista.append(x)

    def Retornar_tabla(self):
        return print(self.lista)