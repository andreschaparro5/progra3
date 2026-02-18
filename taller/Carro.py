class Carro:
    def __init__(self, marca, precio, placa):
        self.marca = marca
        self.precio = precio
        self.placa = placa

    def to_json(self):
        return self.__dict__
        
