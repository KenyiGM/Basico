import tabla as comprobar
import generador
from msvcrt import getch

def juego():

    tabla = generador.generador_sudoku()

    valor_b = comprobar.bloque(tabla)
    valor_c = comprobar.columna(tabla)
    valor_f = comprobar.fila(tabla)

    suma = valor_b + valor_c + valor_f

    if suma == 3:
        
        print("Es funcional la tabla")
        for x in range(9):
            print(tabla[x])
        print("\nPresione cualquier tecla para salir...")
        getch()
    else:
        print("No es funcional la tabla")



if __name__ == "__main__":
    juego()
