package co.edu.uptc.Entities;

public class Estudiante {
    private int identificacion;
    private String nombre;
    private double promedio;
    
    public Estudiante(int identificacion, String nombre, double promedio){
        this.identificacion = identificacion;
        this.nombre = nombre;
        this.promedio = promedio;
    }

    public int getIdentificacion(){
        return identificacion;
    }
    public void setIdentificacion(int identificacion){
        this.identificacion = identificacion;
    }
    public String getNombre(){
        return nombre;
    }
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    @Override
    public String toString(){
        return "nombre: "+nombre+"\n";
    }
}