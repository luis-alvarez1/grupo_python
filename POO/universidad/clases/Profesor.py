class Profesor:
    edad = 0
    nombre = ''
    codProf = ''
    materia = ''

    def setEdad(self, edad):
        self.edad = edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setTeacherCode(self, cod):
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
        return self.nombre + '\n' + self.codProf + '\n' + self.edad + '\n' + self.materia
