'''
Constructores en POO:
    Un constructor se define como aquel que  inicializa los valores de los atributos que nosotros le especifiquemos.
    Por lo general se inicializan todos los atributos pero en proyectos más robustos no siempre se inicializan todos,
    todo esto depende de nuestras necesidades.

    sintaxis:

    def __init__():
        # lista de atributos con la clausula self. antes

Abstarcción en POO:
     La abstracción forma parte de los elementos fundamentales en el modelo de objetos. Una
    abstracción se enfoca en la visión externa de un objeto,  separa el comportamiento  específico de un objeto,
    a esta división que realiza se le conoce como la barrera de abstracción, la cuál se consigue aplicando el principio
    de mínimo compromiso. Básciamente consiste en identificar qué campos/atributos deben ser propios de la clase y no
    deben ser visibles desde otros lados del programa. La recomendación es que pongamos TODOS los atributos en privado
    para así posteriormente acceder a ellos mediante los métodos getter y setter.

    OJO: debemos identificar qué atributos necesitan un método setter ya que, si todos los atributos los poseen,
    nuestro código se enfrentaría a problemas de la tan preciada lógica que buscamos en este tipo de programas.

    EJ: ¿Es lógico que podamos modificar el número de ruedas a un Coche?

    sintaxis:
    __var = "valor"

    Con la anterior linea, le estamos diciendo a Python que esa linea va a ser privada, o sea, solo será accesible desde
    la clase donde se está definiendo.

Tomando el anterior ejemplo, aplicaremos todos los nuevos terminos que aprendimos:

    class Persona:

        def __init__():
           self.__edad = 0
           self.__nombre = ""
           self.__numId = ""

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

    juan = Persona()
'''


def main():
    pass  # code here


main()
