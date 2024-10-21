import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Paginas extends JFrame {
    private JTextArea instrucciones;
    private JTextField datosIngresados;
    private JButton botonRegistrar;
    private JLabel respuesta;

    public Paginas() {
        setTitle("Pagina GUI");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        instrucciones = new JTextArea();
        datosIngresados = new JTextField();
        botonRegistrar = new JButton("Registrar");
        respuesta = new JLabel();

        botonRegistrar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Aquí puedes agregar la lógica para procesar los datos ingresados
                respuesta.setText("Respuesta calculada");
            }
        });

        setLayout(new GridLayout(4, 1));
        add(instrucciones);
        add(datosIngresados);
        add(botonRegistrar);
        add(respuesta);
    }

    // Método para obtener datos ingresados
    public String getDatosIngresados() {
        return datosIngresados.getText();
    }

    // Método para establecer la respuesta
    public void setRespuesta(String textoRespuesta) {
        respuesta.setText(textoRespuesta);
    }

    public static void main(String[] args) {
        Paginas pagina = new Paginas();
        pagina.setVisible(true);
    }
}