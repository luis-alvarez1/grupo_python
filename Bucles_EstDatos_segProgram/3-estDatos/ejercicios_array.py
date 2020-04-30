'''
Crea un array de 10 posiciones de números con valores pedidos por teclado.
 Muestra por consola el indice y el valor al que corresponde. Haz dos métodos,
  uno para rellenar valores y otro para mostrar.

'''

import random


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


main()
