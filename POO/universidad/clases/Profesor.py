class Profesor:
    edad = 0
    nombre = ''
    codProf = ''
    materia = ''

    def setEdad(self, edad):
        if edad < 0 or edad > 100:
            print("EDAD NO VALIDA")
        else:
            self.edad = edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setTeacherCode(self, codProf):
        self.codProf = codProf

    def setMateria(self, materia):
        self.materia = materia

    def getEdad(self):
        return self.edad

    def getNombre(self):
        return self.nombre

    def getTeacherCode(self):
        return self.codProf

    def getMateria(self):
        return self.materia

    def toString(self):
        return self.nombre + '\n' + self.codProf + '\n' + str(self.edad) + '\n' + self.materia
