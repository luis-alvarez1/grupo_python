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
    elif(<otra condicion>): # else if
        #si la condicion anterior falló y se desea evaluar otra
    else:
        #si todo lo anterior falló

"""


def main():

	num1 = int(input("ingrese el primer numero: "))
	num2 = int(input("ingrese el segundo numero: "))

	if num1 > num2:
		print(f"{num1} es mayor que {num2}")
	elif num1 < num2:
		print(f"{num1} es menor que {num2}")
	else:
		print("son iguales")
			
main()