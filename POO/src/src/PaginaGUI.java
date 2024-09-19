package src;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class PaginaGUI {

    private JFrame frame;
    private JTextArea instrucciones;
    private JTextField datosIngresados;
    private JButton botonRegistrar;
    private JLabel respuesta;

    /**
     * Launch the application.
     */
    public static void main(String[] args) {
        PaginaGUI window = new PaginaGUI();
        window.getFrame().setVisible(true);
    }

    /**
     * Create the application.
     */
    public PaginaGUI() {
        initialize();
    }

    /**
     * Initialize the contents of the frame.
     */
    private void initialize() {
        setFrame(new JFrame());
        getFrame().setBounds(100, 100, 450, 300);
        getFrame().setTitle("Pagina GUI");
        getFrame().setSize(400, 300);
        getFrame().setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Initialize components
        instrucciones = new JTextArea("Instrucciones: Por favor, ingrese los datos.");
        datosIngresados = new JTextField();
        botonRegistrar = new JButton("Registrar");
        respuesta = new JLabel();

        // Use GridLayout: 4 rows, 1 column
        getFrame().setLayout(new GridLayout(4, 1));

        // Add components to the frame
        getFrame().add(instrucciones);      // First row
        getFrame().add(datosIngresados);    // Second row
        getFrame().add(botonRegistrar);     // Third row
        getFrame().add(respuesta);          // Fourth row

        // ActionListener for the button
        botonRegistrar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Example action: Display entered text as response
                String input = datosIngresados.getText();
                respuesta.setText("Datos registrados: " + input);
            }
        });
    }

    public JFrame getFrame() {
        return frame;
    }

    public void setFrame(JFrame frame) {
        this.frame = frame;
    }
}
