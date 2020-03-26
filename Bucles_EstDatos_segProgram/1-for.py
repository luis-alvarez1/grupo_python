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

    Escriba un programa que pida un número entero
    mayor que cero y que escriba sus divisores.


    num = int(input("Ingrese un numero positivo: "))
    if num < 0:
        print("el numero debe ser positivio")
    else:
        # num % i = 0

        # range() por defecto empieza en 0 si no se especifica el inicio
        # i < fin

        for i in range(1, (num + 1)):
            if num % i == 0:  # es un divisor
                print(i)

    Escriba un programa que pida dos números enteros y escriba qué 
    números son pares y cuáles impares desde el primero hasta el segundo.

    num1 = int(input("ingrese el primero: "))
    num2 = int(input("ingrese el segundo: "))

    for i in range(num1, num2):
        #num % 2 == 0
        if i % 2 != 0: #i % 2 == 0
            print(i)'''

    '''
    (contador) Escriba un programa que pregunte cuántos números se van a introducir,
    pida esos números y escriba cuántos negativos ha introducido.
    '''

    numeros = int(input("¿cuanto numeros va a introducir? :"))

    negativos = 0;
    for i in range(0, numeros):
        actual = int(input(f"ingrese el numero {(i + 1)}: "))
        if actual < 0:
            negativos += 1

    print(f"usted introdujo {negativos} numeros negativos")


main()
