package src;

import java.awt.*;
import javax.swing.*;

public class Home {

    private JFrame frame;

    /**
     * Launch the application.
     */
    public static void main(String[] args) {
        Home window = new Home();
        window.frame.setVisible(true);
    }

    /**
     * Create the application.
     */
    public Home() {
        initialize();
    }

    /**
     * Initialize the contents of the frame.
     */
    private void initialize() {
        frame = new JFrame();
        frame.setTitle("Pagina GUI");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Set the frame size to full screen
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        int screenWidth = toolkit.getScreenSize().width;
        int screenHeight = toolkit.getScreenSize().height;
        frame.setSize(screenWidth, screenHeight);
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);

        // Create a custom panel with a background image
        BackgroundPanel panel = new BackgroundPanel(new ImageIcon("C:\\Users\\esteb\\OneDrive\\Escritorio\\UVG\\UVG 2024 EHVM\\Segundo Semestre\\PROGRAMACIÓN ORIENTADA A OBJETOS\\Proyecto Progra\\POO\\src\\src\\T1.png").getImage());
        panel.setLayout(null); // Use absolute positioning for components

        // Add buttons to the BackgroundPanel, not the frame
        JButton nomenclatura = new JButton("Nom");
        nomenclatura.setBounds(1170, 127, 75, 74);
        nomenclatura.setBackground(Color.PINK);  // Set "Bal" button color to green
        panel.add(nomenclatura);

        JButton masamolar = new JButton("Mol");
        masamolar.setBounds(482, 345, 75, 75);
        masamolar.setBackground(Color.ORANGE); // Set "Mol" button color to yellow
        panel.add(masamolar);
        
        JButton tabla = new JButton("Tabl");
        tabla.setBounds(407, 420, 75, 75);
        tabla.setBackground(Color.ORANGE); // Set "Tabl" button color to yellow
        panel.add(tabla);
        
        JButton perfil = new JButton("Perf");
        perfil.setBounds(1170, 202, 75, 74);
        perfil.setBackground(Color.PINK);  // Set "Bal" button color to green
        panel.add(perfil);
        
        JButton balanceo = new JButton("Balan");
        balanceo.setBounds(252, 420, 75, 75);
        balanceo.setBackground(Color.BLUE); // Set "Tabl" button color to yellow
        panel.add(balanceo);
        
        JButton informacion = new JButton("inf");
        informacion.setBounds(1325, 345, 75, 75);
        informacion.setBackground(Color.RED); // Set "Mol" button color to yellow
        panel.add(informacion);
        
        JButton estequiometria = new JButton("Est");
        estequiometria.setBounds(1133, 670, 75, 74);
        estequiometria.setBackground(Color.WHITE);  // Set "Bal" button color to green
        panel.add(estequiometria);

        // Add the panel with the background image to the frame's content pane
        frame.getContentPane().add(panel, BorderLayout.CENTER);
    }

    // Custom JPanel class to handle background image
    class BackgroundPanel extends JPanel {
        private Image backgroundImage;

        public BackgroundPanel(Image image) {
            this.backgroundImage = image;
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            g.drawImage(backgroundImage, 0, 0, this.getWidth(), this.getHeight(), this);
        }
    }
}
