# una variable es un espacio en memoria donde se almacena un dato

"""
# tipos de datos:
numéricos :
    integer : enteros (no decimal)
    float : decimales

cadenas :
    char : un solo caracter = 'a', '6', '?'
    string : texto de más de un caracter = "esto es un texto de más de un caracter"

booleanos :
    True : verdadero
    False : falso


print(f"texto {variable}")
"""


def main():
    # definicion de variables
    # <nombre de varibale> = <valor de la variable>
    num1 = 5
    num2 = 3.6
    nombre = "Luis"
    letra = 'f'
    estaActivo = False

    # operacion de los numeros
    resultado = num1 + num2

    # define variable float
    var = 3.4

    # mostrar tipos de variables

    print(type(num1))

    # casting
    print("el resultado es : " + str(resultado))

    print("NOMBRE + LETRA = " + nombre + letra)

    # imprime el resultado
    print(str(num1) + " + " + str(num2) + " = " + str(resultado))

    print(f"{num1} + {num2} = {resultado}")

    # falta definir variables

    '''Crear una variable de cada tipo, imprimir por consola cada una con su respectivo tipo (+2)'''


main()
