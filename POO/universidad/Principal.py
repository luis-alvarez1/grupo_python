
from clases import Estudiante
from clases import Profesor


def main():
    jhon = Profesor()
    jhon.setEdad(45)
    jhon.setNombre("Jhon Niño")
    jhon.setMateria("Fundamento Prog")
    jhon.setTeacherCode("123")

    print(jhon.toString())


main()
