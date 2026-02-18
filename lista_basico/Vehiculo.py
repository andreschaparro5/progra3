class ObjetoVehiculo:
    def __init__(self, modelo, marca, color, placa):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.placa = placa

    def to_json(self):
        return self.__dict__
