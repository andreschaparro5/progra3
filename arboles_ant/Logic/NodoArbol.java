package Logic;

import Entities.Estudiante;

class NodoArbol{
    Estudiante estudiante;
    NodoArbol izquierdo, derecho;
    
    public NodoArbol(Estudiante estudiante){
        this.estudiante = estudiante;
        this.izquierdo = null;
        this.derecho = null;
    }
}