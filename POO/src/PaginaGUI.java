

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class PaginaGUI {//extends JFrame {

    protected JFrame frame;
    protected JTextArea instrucciones;
    protected JTextField datosIngresados;
    protected JButton botonRegistrar;
    protected JLabel respuesta;

    /**
     * Lanza la aplicación.
     */
  /*  public static void main(String[] args) {
        PaginaGUI window = new PaginaGUI();
        window.getFrame().setVisible(true);
    }

    /**
     * Crea la aplicación.
     */
    public PaginaGUI() {
        initialize();
        frame.setVisible(false);
    }

    /**
     * Inicializa el contenido del frame.
     */
    protected void initialize() {
        frame = new JFrame();
        frame.setBounds(100, 100, 450, 300);
        frame.setTitle("Pagina GUI");
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Maximizar la ventana al abrir
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);

        // Inicializar componentes
        instrucciones = new JTextArea("Instrucciones: Por favor, ingrese los datos.");
        instrucciones.setEditable(false); // Hacer que el JTextArea no sea editable
        datosIngresados = new JTextField();
        botonRegistrar = new JButton("Registrar");
        respuesta = new JLabel();

        // Usar GridLayout: 4 filas, 1 columna
        frame.setLayout(new GridLayout(4, 1));

        // Añadir componentes al frame
        frame.add(instrucciones);      // Primera fila
        frame.add(datosIngresados);    // Segunda fila
        frame.add(botonRegistrar);     // Tercera fila
        frame.add(respuesta);          // Cuarta fila

        // ActionListener para el botón
        botonRegistrar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    // Acción de ejemplo: Mostrar el texto ingresado como respuesta
                    String input = datosIngresados.getText();
                    if (input.isEmpty()) {
                        throw new IllegalArgumentException("El campo de datos no puede estar vacío.");
                    }
                    respuesta.setText("Datos registrados: " + input);
                } catch (IllegalArgumentException ex) {
                    // Mostrar diálogo de alerta
                    JOptionPane.showMessageDialog(frame, ex.getMessage(), "Se requiere otro tipo de datos", JOptionPane.ERROR_MESSAGE);
                }
            }
        });
    }

    public JFrame getFrame() {
        return frame;
    }

    public void setFrame(JFrame frame) {
        this.frame = frame;
    }

    // Método para actualizar las instrucciones
    public void setInstrucciones(String texto) {
        instrucciones.setText(texto);
    }

    // Método para obtener los datos ingresados
    public String getDatosIngresados() {
        return datosIngresados.getText();
    }

    // Método para actualizar la respuesta
    public void setRespuesta(String texto) {//Aqui debe ir el tipo de dato que se requiera
        respuesta.setText(texto);
    }
}

