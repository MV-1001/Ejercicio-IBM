import numpy
import numpy as np

#Definimos la función  matriz

def matriz(n):
 # mat es la matriz vacia que se rellenará con números aleatorios
 mat =[]
 # crear un  bucle con for para rellenar filas aleatoriamente 
 for i in range(n):
   mat.append([])
   #crear un bucle con for para rellenar columnas aleatoriamente
   for j in range(n):
      mat[i].append(np.random.randint(0,9))
 return mat

"""
Luego se pide al usuario que introduzca un número y se llama a la función matriz() con ese número como argumento
La matriz resultante se almacena en la variable varmatriz y se imprime en pantalla.
"""

variable = int(input("Introduzca el número : "))
varmatriz = matriz(variable)
print("La matriz resultante es : ", varmatriz)


"""
se llama a estas funciones con la variable varmatriz como argumento y se almacenan los resultados en las variables 
sumafilas_matriz y sumarcolumns_matriz . Finalmente, se imprimen en pantalla las sumas de las filas y las columnas

"""
# funcion suma de filas
def sumafilas(matriz):
    return [sum(fila) for fila in varmatriz]
# funcion suma de columnas
def sumarcolumns(matriz):
    return [sum(columna) for columna in zip(*varmatriz)]
matriz = [varmatriz]

# Suma de filas
sumafilas_matriz = sumafilas(varmatriz)

# Suma de columnas
sumarcolumns_matriz = sumarcolumns(varmatriz)

print("Sumas de las filas:", sumafilas_matriz)
print("Sumas de las columnas:", sumarcolumns_matriz)















