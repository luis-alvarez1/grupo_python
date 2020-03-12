# principales funciones y características de las cadenas de texto

"""
python trata a las cadenas como "listas/arrays" de caracteres
ej:
    nombre = "luis alvarez"

    esto equivale a: l , u , i , s ,   , a , l , v , a , r , e , z
    posiciones:      0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11

se puede acceder a cualquier posicion de la candena tal que...
    nombre[<posicion deseada>] (cabe resaltar que la posicion debe estar
                                contemplada en la cadena)

también es valido acceder a una porción de la cadena tal que...
    nombre[<pos inico>:<pos final>]


concatenación = "cadena1" + "cadena2"

(no se puede modificar mediante la consulta)
    nombre[i] = "m"

    metodo len(<cadena/variable>) devuelve el tamaño de la cadena
    metodo upper()/lower() convierte la cadena en
    mayusculas/minusculas
    metodo split(<argumento>) separa la cadena dependiendo del argumento y la almacena en un array
    donde cada pos es una parte de la cadena

"""


def main():
    ''' nombre = "luis"
    apellido = "alvarez"

    # print(nombre[11])

    # print(nombre[0:4])

    nombreCompleto = nombre + " " + apellido

    print(nombreCompleto)

    # nombre[2] = "m"

    # devuelve el tamaño de la cadena
    # print(len("hola mundo"))

    print(nombre.lower())
    print(nombre)

    # nombre =nombre.upper()
    print(nombre)

    print(nombreCompleto.capitalize())

    # nombre = nombreCompleto.split()


    crear variable que contenga un texto y mostrar el tipo de la variable,
    crear otra variable que almacene la longitud de la variable anterior,
    crear otra variable que almacene la primera variable pero en mayusculas.
    crear otra variable que concatene la variable mayusculas y la variable de longitud 
    '''


main()
