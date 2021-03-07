"""
La programación orientada a objeto (POO/OOP) viene a solucionar el problema que tenían lenguajes anteriores
de tener un código demasiado extenso e inentendible y esto hacía que, si fallaba un trozo del código,
caía el resto del código de ese punto en adelante.

La POO tiene como objetivo trasladar la naturaleza de los objetos de la vida real
a código de programación.

La programación Orientada a objetos (POO) es una forma especial de programar,
más cercana a como expresaríamos las cosas en la vida real que otros tipos de programación.

¿Naturaleza del objeto?:
    Esto se refiere a las propiedades básicas de los objetos: estado, comportamientos (acciones)
    y propiedades o atributos.

EJ: El típico ejemplo del coche :D

    Estados: Encendido, apagado, andando, aparacado, etc.

    Propiedades/Atributos: Color, peso, tamaño, número de placa, longitud, modelo, etc.

    Comportamientos/Acciones: Avanzar, retroceder, frenar, acelerar, girar a la izquierda/derecha

VENTAJAS:
    - Programas divididos en trozos o partes (clases) que no dependen de los demás trozos. (Modularización)
    - Mucho más reutilizable.
    - Se pueden manejar errores con mejor control del código.
    - "El objeto Coche no tiene por qué saber cómo está conformado el objeto Persona" (Encapsulamiento)


La POO se basa en Clases (tipos) que contienen los atributos, estados y acciones de los objetos.

¿Clase?: 
    Es una plantilla para la creación de objetos según un modelo predefinido.
    Las clases se utilizan para representar entidades o conceptos.

Pero... ¿Cómo accedo a los atributos/comportamientos de una cierta clase?
    Mediante métodos/funciones de acceso o accesores y mutadores (getter, setter).


self: se refiere al objeto al que apunta en ese momento.


Sintaxis de la clase:
    class <nombre clase>:
        # atributos
        # constructor
        # metodos/acciones
        # getter/setter

¿Cómo creo un objeto de la clase?
    <nombre objeto> = <nombre clase>(<parametros constructor>)

EJ:
    class Persona:
        edad = 0
        nombre = ""
        numId = ""

        def caminar(self):
            pass  # hace algo

        def comer(self):
            pass

        def setEdad(self, edad):
            self.edad = edad

        def getEdad(self):
            return self.edad

        def setNombre(self, nombre):
            self.nombre = nombre

        def getNombre(self):
            return self.nombre

        def setNumId(self, numId):
            self.numId = numId

        def getNumId(self):
            return self.numId

    carlos = Persona()

"""


class Persona:
    edad = 0
    nombre = ""
    numId = ""
    altura = 160

    def caminar(self):
        pass  # hace algo

    def comer(self):
        pass

    def setEdad(self, edad):
        self.edad = edad

    def setAltura(self, altura):
        self.altura = altura

    def getEdad(self):
        return self.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def getAltura(self):
        return self.altura

    def setNumId(self, numId):
        self.numId = numId

    def getNumId(self):
        return self.numId

    def toString(self):
        return str(self.edad) + "\n" + self.nombre + "\n" + self.numId + '\n' + str(self.altura)


def main():

    carlos = Persona()
    carlos.setEdad(20)
    carlos.setNombre("Carlos")
    carlos.setNumId("456")
    carlos.setAltura(185)

    haiber = Persona()
    haiber.setNombre("Haiber")
    haiber.setEdad(17)
    haiber.setNumId("123")

    print(haiber.toString())

    print()

    print(carlos.toString())


main()
