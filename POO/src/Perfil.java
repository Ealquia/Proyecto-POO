

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

    // Ruta a los avatares fijos
    
    private String ruta1 = "C:\\Users\\esteb\\OneDrive\\Escritorio\\UVG\\UVG 2024 EHVM\\Segundo Semestre\\PROGRAMACIÓN ORIENTADA A OBJETOS\\Proyecto Progra\\POO\\src\\Chang.png";
    private String ruta2 = "C:\\Users\\esteb\\OneDrive\\Escritorio\\UVG\\UVG 2024 EHVM\\Segundo Semestre\\PROGRAMACIÓN ORIENTADA A OBJETOS\\Proyecto Progra\\POO\\src\\Chiquin.png";

    // Ruta a los avatares iconicos xd
    private String icono1 = "C:\\Users\\esteb\\OneDrive\\Escritorio\\UVG\\UVG 2024 EHVM\\Segundo Semestre\\PROGRAMACIÓN ORIENTADA A OBJETOS\\Proyecto Progra\\POO\\src\\Chang Default (1).gif";
    private String icono2 = "C:\\Users\\esteb\\OneDrive\\Escritorio\\UVG\\UVG 2024 EHVM\\Segundo Semestre\\PROGRAMACIÓN ORIENTADA A OBJETOS\\Proyecto Progra\\POO\\src\\Chiquin Default (1).gif";

    private boolean usandoAvatar1 = true;  // que avatar se esta usando

    public Perfil() {
        // Set up the frame
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(100, 100, 707, 419);
        contentPane = new JPanel();
        contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
        setContentPane(contentPane);
        contentPane.setLayout(new BorderLayout(0, 0));

        JPanel infoPanel = new JPanel();
        infoPanel.setLayout(new GridLayout(1, 2));
        contentPane.add(infoPanel, BorderLayout.CENTER);

        // Informacion por excrito
        instruccion = new JTextPane();
        instruccion.setText("Nombre:\nCarnet:\nAño que cursa:\nQuímica 1 o 2:");
        infoPanel.add(instruccion);

        // Info del usuario
        infouser = new JLabel("Perfil del Usuario:");
        infoPanel.add(infouser);

        // crear el avatar
        cartelavatar = new JLabel();
        cartelavatar.setHorizontalAlignment(SwingConstants.CENTER);
        updateAvatarIcon(ruta1);  //avatar inicial
        infoPanel.add(cartelavatar);

        // boton inicial del avatar
        botonAvatar = new JButton("Cambiar Avatar");
        botonAvatar.setIcon(new ImageIcon(icono1));
        botonAvatar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // cambiar icono al clickear
                if (usandoAvatar1) {
                    updateAvatarIcon(ruta2);
                    botonAvatar.setIcon(new ImageIcon(icono2));  // Change button icon
                    usandoAvatar1 = false;
                } else {
                    updateAvatarIcon(ruta1);
                    botonAvatar.setIcon(new ImageIcon(icono1));  // Change button icon back
                    usandoAvatar1 = true;
                }
            }
        });
        infoPanel.add(botonAvatar);

        // Create a panel at the bottom for the buttons
        JPanel bottomPanel = new JPanel();
        bottomPanel.setLayout(new BorderLayout());
        contentPane.add(bottomPanel, BorderLayout.SOUTH);

        // Add a button to confirm the entered text
        JButton confirmButton = new JButton("Registrar perfil");
        bottomPanel.add(confirmButton, BorderLayout.CENTER);

        // Action listener to handle the confirm button click
        confirmButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Get the text from JTextPane and display it in displayInfoLabel
                String userInfo = instruccion.getText();
                infouser.setText("<html><p>Información del Usuario:</p><p>" + userInfo.replaceAll("\n", "<br>") + "</p></html>");
            }
        });
    }

    // Helper method to update the avatar icon
    private void updateAvatarIcon(String avatarPath) {
        ImageIcon avatarIcon = new ImageIcon(avatarPath);
        Image avatarImage = avatarIcon.getImage().getScaledInstance(100, 100, Image.SCALE_SMOOTH);
        cartelavatar.setIcon(new ImageIcon(avatarImage)); // Ensure avatarLabel is initialized
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

