package Logic;

public class ArbolBinarioEstudiante {
    private NodoArbol raiz;
    
    public ArbolBinarioEstudiante(){
        this.raiz = null;
    }

    public void insertar(Estudiante estudiante){
        raiz = insertarRec(raiz, estudiante);
    }

    public NodoArbol insertarRec(NodoArbol raiz, Estudiante estudiante){
        if(raiz == null){
            return new NodoArbol(estudiante);
        }
        if(estudiante.getIdentificacion() < raiz.estudiante.getIdentificacion()){
            raiz.izquierdo = insertarRec(raiz.izquierdo, estudiante);
        }else if(estudiante.getIdentificacion() > raiz.estudiante.getIdentificacion()){
    raiz.derecho = insertarRec(raiz.derecho, estudiante);
        }
        return raiz;
    }

    public void inOrder(){
        inOrderRec(raiz);
    }

    public void inOrderRec(NodoArbol raiz){
        if(raiz != null){
            inOrderRec(raiz.izquierdo);
            System.out.println(raiz.estudiante.getNombre());
            inOrderRec(raiz.derecho);
        }
    }

    public void postOrder(){
        postOrederRec(raiz);
    }
    
    public void postOrderRec(NodoArbol raiz){
        if(raiz != null){
            inOrderRec(raiz.derecho);
            System.out.println(raiz.estudiante.getNombre());
            inOrderRec(raiz.izquierdo);
        }
    }
}