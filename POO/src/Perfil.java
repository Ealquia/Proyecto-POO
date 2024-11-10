import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.GridLayout;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;
import javax.swing.border.EmptyBorder;

public class Perfil extends JFrame {

    private static final long serialVersionUID = 1L;
    private JPanel contentPane;
    private JTextPane instruccion;
    private JLabel cartelavatar;
    private JLabel infouser;
    private JButton botonAvatar;

    // Rutas a los avatares
    private String[] rutasAvatares = {
        "C:\\Users\\esteb\\OneDrive\\Escritorio\\UVG\\UVG 2024 EHVM\\Segundo Semestre\\PROGRAMACIÓN ORIENTADA A OBJETOS\\Proyecto Progra\\POO\\src\\Chang.png",
        "C:\\Users\\esteb\\OneDrive\\Escritorio\\UVG\\UVG 2024 EHVM\\Segundo Semestre\\PROGRAMACIÓN ORIENTADA A OBJETOS\\Proyecto Progra\\POO\\src\\Chiquin.png",
        "C:\\Users\\esteb\\OneDrive\\Escritorio\\UVG\\UVG 2024 EHVM\\Segundo Semestre\\PROGRAMACIÓN ORIENTADA A OBJETOS\\Proyecto Progra\\POO\\src\\Carla.png",
        "C:\\Users\\esteb\\OneDrive\\Escritorio\\UVG\\UVG 2024 EHVM\\Segundo Semestre\\PROGRAMACIÓN ORIENTADA A OBJETOS\\Proyecto Progra\\POO\\src\\Majito.png"
    };

    // Rutas a los iconos
    private String[] iconos = {
        "C:\\Users\\esteb\\OneDrive\\Escritorio\\UVG\\UVG 2024 EHVM\\Segundo Semestre\\PROGRAMACIÓN ORIENTADA A OBJETOS\\Proyecto Progra\\POO\\src\\Chang Default (1).gif",
        "C:\\Users\\esteb\\OneDrive\\Escritorio\\UVG\\UVG 2024 EHVM\\Segundo Semestre\\PROGRAMACIÓN ORIENTADA A OBJETOS\\Proyecto Progra\\POO\\src\\Chiquin Default (1).gif",
        "C:\\Users\\esteb\\OneDrive\\Escritorio\\UVG\\UVG 2024 EHVM\\Segundo Semestre\\PROGRAMACIÓN ORIENTADA A OBJETOS\\Proyecto Progra\\POO\\src\\Carla.gif",
        "C:\\Users\\esteb\\OneDrive\\Escritorio\\UVG\\UVG 2024 EHVM\\Segundo Semestre\\PROGRAMACIÓN ORIENTADA A OBJETOS\\Proyecto Progra\\POO\\src\\Majito.gif"
    };

    private int avatarIndex = 0; // Índice para llevar el seguimiento del avatar actual

    public Perfil() {
        // Configurar el marco
        setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);
        setBounds(100, 100, 707, 419);
        contentPane = new JPanel();
        contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
        setContentPane(contentPane);
        contentPane.setLayout(new BorderLayout(0, 0));

        JPanel infoPanel = new JPanel();
        infoPanel.setLayout(new GridLayout(1, 2));
        contentPane.add(infoPanel, BorderLayout.CENTER);

        // Información por escrito
        instruccion = new JTextPane();
        instruccion.setText("Nombre:\nCarnet:\nAño que cursa:\nQuímica 1 o 2:");
        infoPanel.add(instruccion);

        // Info del usuario
        infouser = new JLabel("Perfil del Usuario:");
        infoPanel.add(infouser);

        // Crear el avatar
        cartelavatar = new JLabel();
        cartelavatar.setHorizontalAlignment(SwingConstants.CENTER);
        updateAvatarIcon(rutasAvatares[avatarIndex]); // avatar inicial
        infoPanel.add(cartelavatar);

        // Botón inicial del avatar
        botonAvatar = new JButton("Cambiar Avatar");
        botonAvatar.setIcon(new ImageIcon(iconos[avatarIndex]));
        botonAvatar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Cambiar avatar al hacer clic
                avatarIndex = (avatarIndex + 1) % rutasAvatares.length; // Cambia al siguiente avatar
                updateAvatarIcon(rutasAvatares[avatarIndex]); // Actualiza el avatar
                botonAvatar.setIcon(new ImageIcon(iconos[avatarIndex])); // Cambia el icono del botón
            }
        });
        infoPanel.add(botonAvatar);

        // Crear un panel en la parte inferior para los botones
        JPanel bottomPanel = new JPanel();
        bottomPanel.setLayout(new BorderLayout());
        contentPane.add(bottomPanel, BorderLayout.SOUTH);

        // Agregar un botón para confirmar la entrada de texto
        JButton confirmButton = new JButton("Registrar perfil");
        bottomPanel.add(confirmButton, BorderLayout.CENTER);

        // Action listener para manejar el clic en el botón de confirmar
        confirmButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Obtener el texto de JTextPane y mostrarlo en infouser
                String userInfo = instruccion.getText();
                infouser.setText("<html><p>Información del Usuario:</p><p>" + userInfo.replaceAll("\n", "<br>") + "</p></html>");
            }
        });
    }

    // Método auxiliar para actualizar el icono del avatar
    private void updateAvatarIcon(String avatarPath) {
        ImageIcon avatarIcon = new ImageIcon(avatarPath);
        Image avatarImage = avatarIcon.getImage().getScaledInstance(100, 100, Image.SCALE_SMOOTH);
        cartelavatar.setIcon(new ImageIcon(avatarImage)); // Asegúrate de que cartelavatar esté inicializado
    }

    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            try {
                Perfil frame = new Perfil();
                frame.setVisible(true);
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
    }
}

