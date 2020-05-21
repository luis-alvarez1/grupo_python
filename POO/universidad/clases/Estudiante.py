class Estudiante:
    nombre = ''
    edad = 0
    carrera = ''
    cod = ''

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    def setEdad(self, edad):
        if edad < 0 or edad > 100:
            print("EDAD NO VALIDA")
        else:
            self.edad = edad

    def setCarrera(self, carrera):
        self.carrera = carrera

    def setStudentCode(self, cod):
        self.cod = cod

    def getNombre(self, nombre):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getCarrera(self):
        return self.carrera

    def getStudentCode(self):
        return self.cod

    def toString(self):
        return self.nombre + '\n' + self.carrera + '\n' + str(self.edad) + '\n' + self.cod
