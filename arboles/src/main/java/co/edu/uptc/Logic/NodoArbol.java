package co.edu.uptc.Logic;

import co.edu.uptc.Entities.Estudiante;

public class NodoArbol{
    Estudiante estudiante;
    NodoArbol izquierdo, derecho;
    
    public NodoArbol(Estudiante estudiante){
        this.estudiante = estudiante;
        this.izquierdo = null;
        this.derecho = null;
    }
}