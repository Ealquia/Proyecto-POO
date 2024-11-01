import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JInternalFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.JTextPane;
import javax.swing.border.EmptyBorder;

public class momamolar extends PaginaGUI {

    private static final long serialVersionUID = 1L;
    private JPanel PanelMoma;
    private JTextField Compingresado;
    private JButton btnRegistrar;
    private JTextPane Resultado;
//    private PythonInterpreter miPython;

    /**
     * Launch the application.
     
    public static void main(String[] args) {
            momamolar frame = new momamolar();
            frame.setVisible(true);
    
    }*/

    /**
     * Create the frame.
     */
    public momamolar() {
        super();
        frame.setVisible(true);

    //    miPython = new PythonInterpreter();
      //  miPython.execfile("./src/CalcMasaMolar.py");

        // Llamar a la función definida en el archivo Python
   //     PyFunction funcionSaludo = (PyFunction) miPython.get("saludo", PyFunction.class);

        // Pasar un argumento a la función Python
     //   PyObject resultado = funcionSaludo.__call__(new PyString("H2O"));

       // miPython.close();

        // Configuración del frame
        frame.setTitle("MomaMolar");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setBounds(200, 200, 900, 600);
        PanelMoma = new JPanel();
        PanelMoma.setBorder(new EmptyBorder(5, 5, 5, 5));
        frame.setContentPane(PanelMoma);
        PanelMoma.setLayout(new BoxLayout(PanelMoma, BoxLayout.Y_AXIS));

        // Creación del frame interno para las instrucciones
        JInternalFrame Frameinterno = new JInternalFrame("Instrucciones:");
        Frameinterno.setVisible(true);
        PanelMoma.add(Frameinterno);

        // Panel de instrucciones
        JTextPane Instrucciones = new JTextPane();
        Instrucciones.setBackground(new Color(128, 255, 255));
        Instrucciones.setForeground(new Color(64, 0, 64));
        Instrucciones.setFont(new Font("Verdana", Font.BOLD | Font.ITALIC, 14));
        Instrucciones.setText("¡Bienvenido a la calculadora de Masa molar!\r\n\r\n"
                + "Ingrese el compuesto del que desea calcular su Masa Molar.\r\n"
                + "Ejemplo Agua: H2O");
        Instrucciones.setEditable(false);
        Frameinterno.getContentPane().add(Instrucciones, BorderLayout.NORTH);

        // Panel de ingreso de datos
        JPanel Ingresodatos = new JPanel();
        Frameinterno.getContentPane().add(Ingresodatos, BorderLayout.CENTER);
        Ingresodatos.setLayout(new BoxLayout(Ingresodatos, BoxLayout.X_AXIS));

        // Campo de texto para ingresar el compuesto
        Compingresado = new JTextField();
        Compingresado.setText("");
        Compingresado.setToolTipText("Ingrese el compuesto químico");
        Ingresodatos.add(Compingresado);
        Compingresado.setColumns(10);

        // Botón para calcular la masa molar
        btnRegistrar = new JButton("Calcular");
        btnRegistrar.addActionListener(new MP());
        Ingresodatos.add(btnRegistrar);
        

        // Área de texto para mostrar el resultado
   Resultado = new JTextPane();
        Resultado.setEditable(false);
    Resultado.setText("La masa molar de su compuesto es:\r\n");
    Ingresodatos.add(Resultado);
}
private class MP implements ActionListener {

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == btnRegistrar) {
            URI uri = URI.create("http://127.0.0.1:5000/mi_api/masa_molar");
            try {
                URL url = uri.toURL();
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("POST");  // Configura el método HTTP
                conn.setRequestProperty("Content-Type", "application/json; utf-8");
                conn.setRequestProperty("Accept", "application/json");
                conn.setDoOutput(true);

                // JSON de datos de entrada
                String jsonInputString = "{\"formula\": \"" + Compingresado.getText() + "\"}";

                // Enviar los datos
                try (OutputStream os = conn.getOutputStream()) {
                    byte[] input = jsonInputString.getBytes("utf-8");
                    os.write(input, 0, input.length);
                }

                // Verifica si la respuesta es exitosa (200 OK)
                int responseCode = conn.getResponseCode();
                if (responseCode == HttpURLConnection.HTTP_OK) {
                    // Lee la respuesta del servidor
                    try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream(), "utf-8"))) {
                        StringBuilder response = new StringBuilder();
                        String responseLine;
                        while ((responseLine = br.readLine()) != null) {
                            response.append(responseLine.trim());
                        }
                        
                        // Extrae el valor de "masa_molar" de la respuesta JSON
                        String jsonResponse = response.toString();
                        String masaMolar = jsonResponse.split("\"masa_molar\":\"")[1].split("\"")[0];

                        // Actualiza el JTextPane con el resultado
                        Resultado.setText("La masa molar de su compuesto es:\n" + masaMolar);
                    }
                } else {
                    Resultado.setText("Error en la conexión: " + responseCode);
                }

                conn.disconnect();
            } catch (Exception e1) {
                e1.printStackTrace();
                Resultado.setText("Error: " + e1.getMessage());
            }
        }
    }
}
}

