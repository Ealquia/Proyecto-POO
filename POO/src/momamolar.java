import java.awt.BorderLayout; // Layout para organizar componentes dentro de contenedores
import java.awt.Color; // Para cambiar los colores de fondo y texto
import java.awt.Font; // Para configurar el estilo de fuente de los textos
import java.awt.event.ActionEvent; // Evento para manejar acciones (como clics de botones)
import java.awt.event.ActionListener; // Interfaz para capturar eventos de acción en componentes
import java.io.BufferedReader; // Para leer datos de la respuesta del servidor
import java.io.InputStreamReader; // Para leer la entrada del servidor como un flujo de caracteres
import java.io.OutputStream; // Para enviar datos al servidor
import java.net.HttpURLConnection; // Para establecer una conexión HTTP con el servidor
import java.net.URI; // Para manejar URIs de manera segura
import java.net.URL; // Para representar y manipular direcciones URL
import javax.swing.BoxLayout; // Layout que organiza componentes en una sola columna o fila
import javax.swing.JButton; // Botón interactivo para ejecutar una acción
import javax.swing.JFrame; // Marco principal de la interfaz gráfica
import javax.swing.JInternalFrame; // Frame interno para mostrar secciones dentro de un marco más grande
import javax.swing.JPanel; // Panel para agrupar y organizar componentes visuales
import javax.swing.JTextField; // Campo de texto para que el usuario ingrese datos
import javax.swing.JTextPane; // Panel de texto para mostrar contenido formateado
import javax.swing.border.EmptyBorder; // Borde vacío que sirve como margen alrededor de los paneles

public class momamolar extends PaginaGUI {

    private static final long serialVersionUID = 1L;
    private JPanel PanelMoma;
    private JTextField Compingresado;
    private JButton btnRegistrar;
    private JTextPane Resultado;

    public momamolar() {
        super();
        frame.setVisible(true);

        frame.setTitle("MomaMolar");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Cierra la aplicación al cerrar la ventana
        frame.setBounds(200, 200, 900, 600); // Tamaño y posición inicial de la ventana
        PanelMoma = new JPanel();
        PanelMoma.setBorder(new EmptyBorder(5, 5, 5, 5)); // Agrega margen alrededor del panel principal
        frame.setContentPane(PanelMoma);
        PanelMoma.setLayout(new BoxLayout(PanelMoma, BoxLayout.Y_AXIS)); // Organiza los componentes en una columna

        // Creación del frame interno para las instrucciones
        JInternalFrame Frameinterno = new JInternalFrame("Instrucciones:");
        Frameinterno.setVisible(true); // Hace visible el frame interno
        PanelMoma.add(Frameinterno);

        // Panel de instrucciones
        JTextPane Instrucciones = new JTextPane();
        Instrucciones.setBackground(new Color(128, 255, 255)); // Color de fondo para la sección de instrucciones
        Instrucciones.setForeground(new Color(64, 0, 64)); // Color del texto de las instrucciones
        Instrucciones.setFont(new Font("Verdana", Font.BOLD | Font.ITALIC, 14)); // Configuración de fuente
        Instrucciones.setText("¡Bienvenido a la calculadora de Masa molar!\r\n\r\n"
                + "Ingrese el compuesto del que desea calcular su Masa Molar.\r\n"
                + "Ejemplo Agua: H2O"); // Texto de bienvenida e instrucciones de uso
        Instrucciones.setEditable(false); // Hace que el texto no sea editable
        Frameinterno.getContentPane().add(Instrucciones, BorderLayout.NORTH); // Añade el panel de instrucciones al frame interno

        // Panel de ingreso de datos
        JPanel Ingresodatos = new JPanel();
        Frameinterno.getContentPane().add(Ingresodatos, BorderLayout.CENTER); // Coloca el panel de ingreso de datos al centro
        Ingresodatos.setLayout(new BoxLayout(Ingresodatos, BoxLayout.X_AXIS)); // Organiza componentes en una fila

        // Campo de texto para ingresar el compuesto
        Compingresado = new JTextField();
        Compingresado.setFont(new Font("Tahoma", Font.PLAIN, 16)); // Fuente del campo de texto
        Compingresado.setText("");
        Compingresado.setToolTipText("Ingrese el compuesto químico"); // Mensaje emergente para guiar al usuario
        Ingresodatos.add(Compingresado); // Añade el campo de texto al panel de ingreso
        Compingresado.setColumns(10); // Define el tamaño del campo de texto

        // Botón para calcular la masa molar
        btnRegistrar = new JButton("Calcular");
        btnRegistrar.setBackground(Color.ORANGE); // Color de fondo del botón
        btnRegistrar.setForeground(Color.BLACK); // Color de texto del botón
        btnRegistrar.setFont(new Font("Tahoma", Font.PLAIN, 10)); // Fuente del botón
        btnRegistrar.addActionListener(new MP()); // Agrega un ActionListener para manejar el clic
        Ingresodatos.add(btnRegistrar); // Añade el botón al panel de ingreso

        // Área de texto para mostrar el resultado
        Resultado = new JTextPane();
        Resultado.setFont(new Font("Times New Roman", Font.BOLD | Font.ITALIC, 15)); // Configuración de la fuente del resultado
        Resultado.setEditable(false); // El campo no es editable por el usuario
        Resultado.setText("La masa molar de su compuesto es:\r\n"); // Texto inicial en el campo de resultado
        Ingresodatos.add(Resultado); // Añade el área de resultado al panel de ingreso
    }

    // Clase interna que implementa ActionListener para el botón
    private class MP implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
            if (e.getSource() == btnRegistrar) {
                URI uri = URI.create("http://127.0.0.1:5000/mi_api/masa_molar"); // URI del endpoint de la API
                try {
                    URL url = uri.toURL();
                    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                    conn.setRequestMethod("POST"); // Configura el método HTTP como POST
                    conn.setRequestProperty("Content-Type", "application/json; utf-8"); // Formato de datos de entrada
                    conn.setRequestProperty("Accept", "application/json"); // Formato de datos de salida esperado
                    conn.setDoOutput(true); // Permite enviar datos en el cuerpo de la solicitud

                    // JSON con la fórmula ingresada por el usuario
                    String jsonInputString = "{\"formula\": \"" + Compingresado.getText() + "\"}";

                    // Enviar los datos al servidor
                    try (OutputStream os = conn.getOutputStream()) {
                        byte[] input = jsonInputString.getBytes("utf-8");
                        os.write(input, 0, input.length); // Escribe el JSON en el flujo de salida
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

                            // Extrae el valor de "masa_molar" de la respuesta JSON manualmente
                            String jsonResponse = response.toString();
                            String masaMolar = jsonResponse.split("\"masa_molar\":")[1].split(",")[0].replace("\"", "").trim();

                            // Actualiza el JTextPane con el resultado
                            Resultado.setText("La masa molar de su compuesto es:\n" + masaMolar);
                        }
                    } else {
                        Resultado.setText("Error en la conexión: " + responseCode); // Mensaje de error si la respuesta no es 200
                    }

                    conn.disconnect();
                } catch (Exception e1) {
                    e1.printStackTrace();
                    Resultado.setText("Error: " + e1.getMessage()); // Muestra el mensaje de error en la interfaz
                }
            }
        }
    }
}

