# Bucle for
'''
Se usa para iterar sobre una secuencia de elementos

for <var index> in range(<inicio iteracion>,<final iteracion-1>):
    #codigo a repetir

Se puede iterar sobre alguna lista o se puede usar la función range() para
generar un rango de valores los cuales, nuestra variable indexadora, tomará

Tambien se puede iterar sobre cadenas
'''


def main():
    ''' cadena = "palabra"

    for letra in cadena:
        print(letra)

    # ejercicio

    Escriba un programa que pida dos números enteros y escriba qué 
    números impares desde el primero hasta el segundo. (+5)

    num1 = int(input("ingrese el primero: "))
    num2 = int(input("ingrese el segundo: "))

    for i in range(num1, num2):
        if i % 2 != 0: 
            print(i)

    (contador) Escriba un programa que pregunte cuántos números se van a introducir,
    pida esos números y escriba cuántos negativos han introducido.
    '''

    numeros = int(input("¿cuanto numeros va a introducir? :"))

    negativos = 0
    for i in range(0, numeros):
        actual = int(input(f"ingrese el numero {(i + 1)}: "))
        if actual < 0:
            negativos += 1

    print(f"usted introdujo {negativos} numeros negativos")


main()
