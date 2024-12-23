import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class Balanceo extends JFrame {

    private JTextField reaccionIngresada; // Campo para la reacción completa
    private JTextArea reaccionBalanceada; // Campo para mostrar el resultado
    private JButton botonBalancear;       // Botón para enviar la solicitud

    public Balanceo() {
        super();
        setTitle("Balanceador de Reacciones Químicas");

        // Inicializa los componentes de la interfaz
        reaccionIngresada = new JTextField();
        reaccionBalanceada = new JTextArea();
        reaccionBalanceada.setFont(new Font("Malgun Gothic", Font.BOLD, 18));
        reaccionBalanceada.setEditable(false);
        botonBalancear = new JButton("Balancear Reacción");
        botonBalancear.setBackground(SystemColor.activeCaption);

        // ActionListener para el botón de balancear
        botonBalancear.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Lógica para enviar la solicitud a la API
                if (reaccionIngresada.getText().isEmpty()) {
                    reaccionBalanceada.setText("Por favor, ingrese la reacción química.");
                } else {
                    // Envia la solicitud a la API y obtien el resultado
                    String resultadoBalanceo = enviarSolicitudBalanceo(reaccionIngresada.getText());
                    // Muestra solo la reacción balanceada en el área de texto
                    reaccionBalanceada.setText(resultadoBalanceo);
                }
            }
        });

        // Configuración de la interfaz
        getContentPane().setLayout(new GridLayout(4, 1));
        JLabel label = new JLabel("Ingrese la reacción química (ej: Al + O2 = Al2O3) :");
        label.setBackground(Color.ORANGE);
        label.setForeground(Color.BLACK);
        label.setFont(new Font("Yu Gothic UI", Font.BOLD | Font.ITALIC, 16));
        getContentPane().add(label);
        getContentPane().add(reaccionIngresada);
        getContentPane().add(botonBalancear);
        getContentPane().add(new JScrollPane(reaccionBalanceada));  // JScrollPane para scroll
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);
    }

    // Método para enviar solicitud a la API de Flask
    private String enviarSolicitudBalanceo(String reaccion) {
        try {
            // URL de la API
            URL url = new URL("http://127.0.0.1:5000/mi_api/balancear_reaccion");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json; utf-8");
            conn.setRequestProperty("Accept", "application/json");
            conn.setDoOutput(true);

            // JSON de la solicitud
            String jsonInputString = String.format("{\"reaccion\": \"%s\"}", reaccion.trim());

            // Envia la solicitud
            try (OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            // Verifica la respuesta
            int responseCode = conn.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) {
                //la respuesta del servidor
                StringBuilder response = new StringBuilder();
                try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream(), "utf-8"))) {
                    String responseLine;
                    while ((responseLine = br.readLine()) != null) {
                        response.append(responseLine.trim());
                    }
                }
                // respuesta de la reacción balanceada
                return response.toString(); // Retorna la respuesta como string
            } else {
                return "Error en la conexión: " + responseCode; // Mensaje de error 
            }

        } catch (Exception e) {
            e.printStackTrace();
            return "Error: " + e.getMessage(); // Muestra el mensaje de error en la interfaz
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Balanceo paginaReaccion = new Balanceo();
            paginaReaccion.setVisible(true);
        });
    }
}

