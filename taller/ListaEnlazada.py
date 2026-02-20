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

    def buscarPorId(self, identifier):
        actual = self.cabeza
        indice = 0
        while actual is not None:
            if self.buscarPorPosicion(indice).identifier == identifier:
                return self.buscarPorPosicion(indice)
            actual = actual.siguiente
            indice += 1
        return None

    def actualizar(self, identifier, nueva_informacion):
        actual = self.cabeza

        while actual is not None:
            if actual.informacion.identifier == identifier:
                actual.informacion = nueva_informacion
                return True
            actual = actual.siguiente

        return False        
        
    def eliminarPorId(self, identifier):
        if self.esta_vacia():
            return False

        actual = self.cabeza
        anterior = None

        while actual is not None:
            if actual.informacion.identifier == identifier:
            
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                return True  

            anterior = actual
            actual = actual.siguiente

        return False  
    
    
    
        
        
        
        
    
        
        
        
        
        
            