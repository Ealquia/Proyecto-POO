import java.util.*;

/**
 * 
 */
public class Compuesto {
    //ATRIBUTOS
    private String Compuesto;
    private int Coeficiente;

    /**
     * Constructor
     * @param Compuesto: string con la fórmula del compuesto
     */
    public Compuesto(String Compuesto) {
        this.Compuesto = Compuesto;
        this.Coeficiente = 1;
    }

    //MÉTODOS
    /**
     * @return
     */
    public List<Elemento> getElementos() {
        // TODO implement here
        return null;
    }

    /**
     * @return
     */
    public Double masaMolar() {
        // TODO implement here
        return null;
    }

    /**
     * @return
     */
    public boolean ElementoPuro() {
        // TODO implement here
        return false;
    }

    /**
     * @return
     */
    public Elemento Elemento() {
        // TODO implement here
        return null;
    }

    //SETTERS AND GETTERS
    /**
     * @return
     */
    public String getCompuesto() {
        return this.Compuesto;
    }

    /**
     * @param value
     */
    public void setCompuesto(String value) {
        this.Compuesto = value;
    }

    /**
     * @return
     */
    public int getCoeficiente() {
        return this.Coeficiente;
    }

    /**
     * @param value
     */
    public void setCoeficiente(int value) {
        this.Coeficiente = value;
    }

}