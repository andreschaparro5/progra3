from NodoLista import Nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_al_frente(self, informacion):
        nuevo_nodo = Nodo(informacion)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def agregar_al_final(self, informacion):
        nuevo_nodo = Nodo(informacion)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.informacion, end=" -> ")
            actual = actual.siguiente
        print("None")

    def imprimir_lista_objetos(self):
        listaEstudiantes = []
        actual = self.cabeza
        while actual is not None :
            print(actual.informacion.__dict__, end=" -> ")
            listaEstudiantes.append(actual.informacion.__dict__)
            actual = actual.siguiente

        print("None")
        print('Aca se esta imprimendo la lista enlazada')
        print(listaEstudiantes)
        return listaEstudiantes

    def buscarPorPosicion(self, posicion):
        actual = self.cabeza
        indice = 0
        while actual is not None:
            if indice == posicion:
                return actual.informacion
            actual = actual.siguiente
            indice += 1
        return None         
