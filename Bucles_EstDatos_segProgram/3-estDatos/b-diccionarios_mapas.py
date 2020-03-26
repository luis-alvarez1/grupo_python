# Diccionarios o mapas
'''
Un diccionario es una colección de elementos que están
indexados, no están ordenados y se pueden
modificar. Son escritos entre llaves
y están formados por pares de elementos, clave valor.

diccionario = {
    calve1:valor1,
     clave2:valor2,
     ...
}

keys()    Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario.

items()    Devuelve una lista de tuplas, cada tupla se compone de dos elementos: el primero será la clave y el segundo,
    su valor.

values()     Retorna una lista de elementos, que serán los valores de nuestro diccionario.

clear()    Elimina todos los ítems del diccionario dejándolo vacío.

copy()    Retorna una copia del diccionario original.

get(<clave>)    Recibe como parámetro una clave, devuelve el valor de la clave. Si no lo encuentra, devuelve un
    objeto none.

pop(<clave>)   Recibe como parámetro una clave, elimina esta y devuelve su valor. Si no lo encuentra, devuelve error.


setdefault():    Funciona de dos formas.
        En la primera como get: dic.setdefault(<clave>)
        Y en la segunda forma, nos sirve para agregar un nuevo elemento a nuestro diccionario.:
            dic.setdefault(<clave>,<valor>)

'''


def main():
    pass  # code here


main()
