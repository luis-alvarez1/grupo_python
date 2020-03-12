#Estructuras condicionales

"""

Python posee tres estructuras condicionales:

1-
    if(<condicion>):
        #cuerpo de la condicion

2-
    if(<condicion>):
        #cuerpo de la condicion
    else:
        #si la condicion no se cumple

3-
    if(<condicion>):
        #cuerpo de la condicion
    elif(<otra condicion>):
        #si la condicion anterior falló y se desea evaluar otra
    else:
        #si todo lo anterior falló

"""


def main():

    
    print("1-primero\n2-segundo\n3-tercero")
    opcion = int(input("ingrese la opcion: "))

    if opcion == 1:
        print("primero") 
    elif opcion == 2:
        print("segundo")
    elif opcion == 3:
        print("tercero")
    else:
        print("incorrecto")
main()