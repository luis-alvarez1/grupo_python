'''
las funciones que retornan, en otros lenguajes, se caracterizan por tener un tipo especificado en la definición.

Esto no pasa en python. Aquí las funciones pueden retornar o no un valor, dependiendo de la situación y del contexto de
la función.

Las funciones que retornan están definidas por la clausula "return" en el cuerpo de la misma. Si se especifica al menos
return dentro de la función, sí o sí, esta debe retornar algún valor.

Estas funciones devuelven un valor y, si no se almacena en una variable o estructura de datos, se perderá el valor. Por
lo tanto, debemos asegurarnos de que el valor sea inyectado en otra variable.
'''


def calculo_multiple(a, b):
    suma = a + b
    # resta = a - b
    multip = a * b

    return suma, a - b, multip, a / b, a ** b


def main():
    a = int(input(("ingrese el primer valor: ")))
    b = int(input(("ingrese el segundo valor: ")))

    suma, resta, multiplicacion, div, exp = calculo_multiple(a, b)

    print(f"{suma}\n{resta}\n{multiplicacion}\n{div}\n{exp}")


main()
