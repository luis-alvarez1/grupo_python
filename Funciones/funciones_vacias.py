# Funciones
'''
Una función es un conjunto de líneas de código que realizan una tarea específica y puede retornar un valor.

Las funciones pueden tomar parámetros que modifiquen su funcionamiento.

Las funciones son utilizadas para descomponer grandes problemas en tareas simples y para implementar operaciones que
son comúnmente utilizadas durante un programa y de esta manera reducir la cantidad de código.

sintaxis:

def <nombre de la funcion> (<parametros>):
    #cuerpo de la funcion

clausula return: Las funciones pueden comunicarse con el exterior de las mismas, al proceso principal del programa
usando la sentencia return. El proceso de comunicación con el exterior se hace devolviendo valores.

tipos de argumentos
- por defecto*
- posicionales*
- nombrados*
- indefinidos*
'''


def numeros(a, b, c):
    print(
        f"primer parametro: {a}\nsegundo parametro {b}\ntercer parametro {c}")


def main():
    numeros(3, c=3, b=2)


main()
