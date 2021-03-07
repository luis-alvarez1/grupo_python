# Bucle while
'''

este bucle recibe una condicion booleana y
se deja de iterar hasta que la condicion se vuelva falsa

while <condicion bool>:
    #codigo a iterar
'''


def main():

    '''Escriba un programa que pida números decimales
    mientras el usuario escriba número mayores que el primero.'''

    num1 = float(input("ingrese el numero "))
    num2 = float(input(f"ingrese un numero mayor a {num1}"))

    while num2 > num1:
        num1 = num2
        num2 = float(input("ingrese un numero mayor a " + str(num2)))

    print(str(num1) + " no es mayor a " + str(num2))


main()
