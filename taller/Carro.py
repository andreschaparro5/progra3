class Carro:
    def __init__(self, identifier, marca, precio, placa):
        self.identifier = identifier
        self.marca = marca
        self.precio = precio
        self.placa = placa

    def to_json(self):
        return self.__dict__
        
