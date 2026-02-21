import Entities.Estudiante;

public class Main(){
    public static void main(String[] args){
        System.out.println("Arboles binarios");
        
        ArbolBinarioEstudiante arbol = new ArbolBinarioEstudiante();
        
        arbol.insertar(new Estudiante(103, "Carlos", 4.5));
        arbol.insertar(new Estudiante(101, "Ana", 3.8));
        arbol.insertar(new Estudiante(105, "Pedro", 4.2));
        arbol.insertar(new Estudiante(102, "Luisa", 3.9));
        
        System.out.println("Arbol en orden: ");
        arbol.inOrden();
        
        System.out.println("\nArbol despues de la eliminacion");
        arbol.inOrden();
    }
}