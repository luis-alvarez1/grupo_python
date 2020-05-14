# Matrices

'''
Las matrices se pueden definir de dos formas:
    Un vector bidimensional que ya no posee un solo indice sino que ahora posee subindices

    Una estructura de control que almacena datos y accede a ellos mediante filas y coljumnas

En este tipo de estructuras de datos ya no tendremos solo una posicion del array, sino que tendremos una posicion
definida por otras 2. En Python, estas se definen como listas dentro de listas... Las listas externas son las filas de
la matriz y las listas internas son las columnas de la misma. Esto puede variar segun el criterio de cada persona.

Supongamos que tenemos una matriz A

Sintaxis:
    A= [[a, b, c],[1, 2, 3],[true, false, 24.9]]

    Aquí estamos definiendo que la matriz tendrá 3 fila y  3 columnas quedando así

    [a,     b,     c]
    [1,     2,     3]
    [True, False, 24.9]

    [a, 1, True],
    [b, 2, False],
    [c, 3, 24.9]

    [0,1]>[1,0]

    [3,2]>[2,3]


'''

'''
Elabore un programa que pida al usuario dos matrices y que las multiplique 
'''

import numpy

def imprimirMatriz(matriz):
    for i in matriz:
        for j in i:
            print(j, end=' ')
        print("")


def main():
    # filas de la primera matriz deben ser iguales a las columnas de la segunda matriz

    filas1 = int(input("Ingrese las filas de la primera matríz: "))
    columnas1 = int(input("Ingrese las columnas de la primera matríz: "))
    filas2 = int(input("Ingrese las filas de la segunda matríz: "))
    columnas2 = int(input("Ingrese las columnas de la segunda matríz: "))

    matriz1 = numpy.zeros((filas1, columnas1))
    matriz2 = numpy.zeros((filas2, columnas2))

    matrizResultante = numpy.zeros((filas1, columnas2))

    print("PRIMERA MATRIZ")
    for i in range(filas1):
        for j in range(columnas1):
            matriz1[i, j] = int(input(f"ingrese el valor {i}:{j}: "))
    print("SEGUNDA  MATRIZ")
    for i in range(filas2):
        for j in range(columnas2):
            matriz2[i, j] = int(input(f"ingrese el valor {i}:{j}: "))

    # multiplicacion

    if (filas1 != columnas2):
        print("NO SE PUEDEN MULTIPLICAR SUS MATRICES")
    else:
        for i in range(filas1):
            for j in range(columnas2):
                for k in range(filas2):
                    matrizResultante[i, j] += matriz1[i, k] * matriz2[k, j]

        imprimirMatriz(matrizResultante)


main()
