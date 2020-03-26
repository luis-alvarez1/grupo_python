'''
Escriba un programa que pida la cantidad de números que se tienen que escribir
 y a continuación pida números hasta que la cantidad de elementos especificada. Mostrar la cantidad de numeros
positivos y negativos
'''


def main():

    cant_numeros = int(input("¿cuantos elementos va ingresar?: "))
    numeros = []
    for i in range(cant_numeros):
        num = int(input(f"ingrese el valor {i+1}: "))
        numeros.append(num)

    positivos = []
    negativos = []
    for numero in numeros:
        if numero < 0:
            negativos.append(numero)
        else:
            positivos.append(numero)

    print("positivos: " + str(positivos))
    print("negativos: " + str(negativos))


main()