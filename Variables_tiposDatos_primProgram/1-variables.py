# una variable es un espacio en memoria donde se almacena un dato

# tipos de datos:
"""
numéricos :
    integer : enteros (no decimal)
    float : decimales

cadenas :
    char : un solo caracter = 'a', '6', '?'
    string : texto de más de un caracter ""

booleanos :
    True : verdadero
    False : falso


print(f"texto {variable}")
"""


# el resultado es: numero

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
    print(type(num2))
    print(type(resultado))
    print(type(nombre))
    print(type(letra))
    print(type(estaActivo))

    # casting
    print("el resultado es : " + str(resultado))

    print("NOMBRE + LETRA = " + nombre + letra)
    # 5 + 3.6 = 8.6

    # imprime el resultado
    print(str(num1) + " + " + str(num2) + " = " + str(resultado))

    print(f"{num1} + {num2} = {resultado}")

    # falta definir variables


main()
