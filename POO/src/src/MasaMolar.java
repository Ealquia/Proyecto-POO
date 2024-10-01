package src;

import java.awt.EventQueue;
import javax.swing.*;

public class MasaMolar extends PaginaGUI{

    private static final long serialVersionUID = 1L;

    public MasaMolar() {
       super(); // Llama al constructor de la clase base
        initialize(); // Inicializa los componentes específicos de MasaMolar
    }


    protected void initialize() {
       super.initialize(); // Llama al método initialize de la clase base

        // Personaliza los componentes específicos de MasaMolar
       setInstrucciones("Instrucciones específicas para Masa Molar: Por favor, ingrese los datos necesarios.");
       botonRegistrar.setText("Calcular Masa Molar");

        // Puedes añadir más personalizaciones aquí si es necesario
    }
}

