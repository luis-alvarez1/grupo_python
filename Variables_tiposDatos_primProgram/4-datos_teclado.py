# perdir datos al usuario mediante teclado

"""
funcion input():

    funcion utilizada para pedir datos al usuario por teclado
        (similar a un read en pseudocodigo)

    -se le puede pasar un mensaje al usuario
    -para mayor explicitud de datos, se puede encerrar en un casteo (str, int, float)
    -se pueden pasar variables en sus parametros
    -devuelve el dato que pasó el usuario por teclado así que este debe
        ser inyectado en una variable

"""


def main():

    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

    resultado = num1 + num2

    print(resultado)


main()
