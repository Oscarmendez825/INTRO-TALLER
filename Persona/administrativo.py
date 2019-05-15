from Persona import persona
class Administrativo(persona):
    def __init__(self, nombre, cedula, edad, departamento, puesto):
        super().__init__(nombre, cedula, edad)
        self.__departamento = departamento
        self.__puesto = puesto
    @property
    def departamento(self):
        return self.__departamento
    @departamento.setter
    def departamento(self,departamento):
        self.__departamento = departamento
    @property
    def puesto(self):
        return self.__puesto
    @puesto.setter
    def puesto(self, puesto):
        return self.__puesto = puesto
    def setpuesto(self, puesto):
        self.__puesto = puesto
