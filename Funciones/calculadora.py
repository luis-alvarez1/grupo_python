'''realizar un programa que tenga las funciones basicas de una calculadora y que las devuelva y las imprima en consola'''


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multip(a, b):
    return a * b


def div(a, b):
    return a / b


def power(a, b):
    return a ** b


def main():
    opc = input("1-suma\n2-resta\n3-multiplicacion\n4-division\n5-exponente\nopcion: ")

    a = int(input("ingrese el primer numero: "))
    b = int(input("ingrese el segundo numero: "))

    if opc == '1':
        print(suma(a, b))
    elif opc == '2':
        print(resta(a, b))
    elif opc == '3':
        print(multip(a, b))
    elif opc == '4':
        print(div(a, b))
    elif opc == '5':
        print(power(a, b))
    else:
        print("no ingreso una opcion valida")


main()
