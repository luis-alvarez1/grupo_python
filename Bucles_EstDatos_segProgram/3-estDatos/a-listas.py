'''
las listas son estructuras de datos que se usan para almacenar valores.
Se asemejan a los vectores

Append(<obj>)
    Este método nos permite agregar nuevos elementos a una lista.

Remove(<indice>)
    El método remove va a remover un elemento que se le pase como
    parámentro de la lista a donde se le esté aplicando.

Index(<dato>)
    Index devuelve el número de indice del elemento que le pasemos por parámetro.

Count(<dato>)
    Para saber cuántas veces un elemento de una lista
    se repite podemos utilizar el metodo count().

Reverse()
    También podemos invertir los elementos  de una lista.
'''


def main():

    '''Escriba un programa que pida dos números enteros y escriba qué
    números son pares y cuáles impares desde el primero hasta el segundo.

    num1 = int(input("ingrese el primero: "))
    num2 = int(input("ingrese el segundo: "))

    pares = []
    impares = []
    for i in range(num1, (num2+1)):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)

    print("\nPARES")
    for par in pares:
        print(par)

    print("\nIMPARES")
    for impar in impares:
        print(impar)'''

    nombres = ["luis", "pepe", "roberto", "maria", "roberto"]
    nombres.reverse()
    print(nombres)


main()