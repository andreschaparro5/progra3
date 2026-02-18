class Estudiante:
    def __init__(self, nombre, edad, identificacion):
        self.nombre = nombre
        self.edad = edad
        self.identificacion = identificacion

    def to_json(self):
        return self.__dict__
