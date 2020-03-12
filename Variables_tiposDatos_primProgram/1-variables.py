# una variable es un espacio en memoria donde se almacena un dato

# tipos de datos:
"""
numéricos :
    integer : enteros (no decimal)
    float : decimales

cadenas :
    char : un solo caracter = 'a', '6', '?'
    string : texto de más de un caracter

booleanos :
    True : verdadero
    False : falso


print(f"texto {variable}")
"""


# el resultado es: numero

def main():
    # definicion de variables
    num1 = 5
    num2 = 3

    # operacion de los numeros
    resultado = num1 + num2

    # define variable float
    var = 3.4

    # mostrar tipos de variables
    print(type(num1))
    print(type(num2))
    print(type(resultado))
    print(type(var))

    # print("el resultado es : " + str(resultado))

    # 5 + 3 = 8

    # imprime el resultado
    print(f"{num1} + {num2} = {resultado}")

    # falta definir variables


main()
