package src;

import java.awt.EventQueue;

public class MasaMolar extends PaginaGUI {

    private static final long serialVersionUID = 1L;

    /**
     * Lanza la aplicación.
     */
    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable() {
            public void run() {
                try {
                    MasaMolar window = new MasaMolar();
                    window.getFrame().setVisible(true);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }

    /**
     * Crea el frame.
     */
@wbp.parser.entryPoint
    public MasaMolar() {
        super(); // Llama al constructor de la clase base
        initialize(); // Inicializa los componentes específicos de MasaMolar
    }

    /**
     * Inicializa el contenido específico del frame.
     */
    @Override
    protected void initialize() {
        super.initialize(); // Llama al método initialize de la clase base

        // Personaliza los componentes específicos de MasaMolar
        setInstrucciones("Instrucciones específicas para Masa Molar: Por favor, ingrese los datos necesarios.");
        botonRegistrar.setText("Calcular Masa Molar");

        // Puedes añadir más personalizaciones aquí si es necesario
    }
}

