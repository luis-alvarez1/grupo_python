'''
Crea un array de 10 posiciones de números con valores pedidos por teclado.
 Muestra por consola el indice y el valor al que corresponde. Haz dos métodos,
  uno para rellenar valores y otro para mostrar.

'''

'''Crea un array de números de un tamaño pasado por teclado, 
el array contendrá números aleatorios impares entre los números deseados, 
por último nos indica cual es el mayor de todos.'''

'''
Crea un array de números de 100 posiciones, que contendrá los números del 
1 al 100. Obtén la suma de todos ellos y el promedio. 

    promedio = suma(elemntos)/elementos
'''

'''Realizar un programa que muestre por pantalla la traspuesta de una matriz'''

'''
def rellenarVector(vector):
    for i in range(10):
        vector.append(random.randint(0, 30))

    return vector


def mostrarVector(vector):
    # indice: 0 = ?
    # indice : 1 = ?
    # indice : 2 = 8
    # indice : 3 = 23

    for i in range(0, len(vector)):
        print(f"indice: {i} = {vector[i]}")


def main():
    array = []

    rellenarVector(array)

    mostrarVector(array)
'''

import numpy


def imprimirMatriz(matriz):
    for i in matriz:
        for j in i:
            print(j, end=' ')
        print()


def transponer(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    transpuesta = numpy.zeros((filas, columnas))

    for i in range(filas):
        for j in range(columnas):
            transpuesta[j, i] = matriz[i, j]

    return transpuesta


def main():
    '''size = int(input("Defina el tamaño del vector: "))  # 5

    impares = []

    while len(impares) < size:

        for i in range(size):
            num = random.randint(0, 100)

            if len(impares) >= size:
                break
            elif num % 2 != 0:
                impares.append(num)

    # calculo mayor

    mayor = 0
    for i in range(0, size):
        if impares[i] > mayor:
            mayor = impares[i]

    print(impares)
    print("El mayor es " + str(mayor))'''

    # ---------------------------------------

    '''filas = int(input("Ingrese las filas de la matriz: "))
    columnas = int(input("Ingrese las columnas de la matriz: "))

    matriz = numpy.zeros((filas, columnas))

    for i in range(filas):
        for j in range(columnas):
            matriz[i, j] = int(input(f"Ingrese el valor {i}:{j}= "))

    imprimirMatriz(matriz)
    transpuesta = transponer(matriz)
    print("\n")
    imprimirMatriz(transpuesta)'''


main()
