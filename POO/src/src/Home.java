package src;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;

public class Home {

    private JFrame frame;
    private JButton nomenclatura;
    private JButton masamolar;
    private JButton tabla;
    private JButton perfil;
    private JButton balanceo;
    private JButton informacion;
    private JButton estequiometria;
    private Nomenclatura nomenVentana;
    private Perfil perfii;
    private MasaMolar mamol;
    private TablaP tablap;
    private Balanceo balanc;
    private informacion infos;
    private Estequio estequi;
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
        frame.setTitle("Pagina de Inicio");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        nomenVentana = new Nomenclatura();
        perfii = new Perfil();
        mamol = new MasaMolar();
        tablap = new TablaP();
        balanc = new Balanceo();
        infos = new informacion();
        estequi = new Estequio();
        // Toda la pantalla
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        int screenWidth = toolkit.getScreenSize().width;
        int screenHeight = toolkit.getScreenSize().height;
        frame.setSize(screenWidth, screenHeight);
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);

        // Pantalla de fondo
        BackgroundPanel panel = new BackgroundPanel(new ImageIcon("C:\\Users\\esteb\\OneDrive\\Escritorio\\UVG\\UVG 2024 EHVM\\Segundo Semestre\\PROGRAMACIÓN ORIENTADA A OBJETOS\\Proyecto Progra\\POO\\src\\src\\T1.png").getImage());
        panel.setLayout(null); // Position absoluta
        frame.getContentPane().add(panel);
        Oyente mp = new Oyente();
        // Añadir los botones realizados previamente
        nomenclatura = new JButton("Nom");
        nomenclatura.setBounds(1170, 127, 75, 74);
        nomenclatura.setBackground(Color.PINK);  // Nomenclatura es rosa
        panel.add(nomenclatura);
        nomenclatura.addActionListener(mp);

        masamolar = new JButton("Mol");
        masamolar.setBounds(482, 345, 75, 75);
        masamolar.setBackground(Color.ORANGE); // Masa molar es naranja
        panel.add(masamolar);
        masamolar.addActionListener(mp);
        
        tabla = new JButton("Tabl");
        tabla.setBounds(407, 420, 75, 75);
        tabla.setBackground(Color.ORANGE); // Tabla periodica es naranja
        panel.add(tabla);
        tabla.addActionListener(mp);
        
        perfil = new JButton("Perf");
        perfil.setBounds(1170, 202, 75, 74);
        perfil.setBackground(Color.PINK);  // Perfil es rosado
        panel.add(perfil);
        perfil.addActionListener(mp);
        
        balanceo = new JButton("Balan");
        balanceo.setBounds(252, 420, 75, 75);
        balanceo.setBackground(Color.BLUE); // Balanceo es azúl
        panel.add(balanceo);
        balanceo.addActionListener(mp);
        
        informacion = new JButton("inf");
        informacion.setBounds(1325, 345, 75, 75);
        informacion.setBackground(Color.RED); // informacion es rojo
        panel.add(informacion);
        informacion.addActionListener(mp);
        
        estequiometria = new JButton("Est");
        estequiometria.setBounds(1133, 670, 75, 74);
        estequiometria.setBackground(Color.WHITE);  //estequiometria es blanco
        panel.add(estequiometria);
        estequiometria.addActionListener(mp);

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
    private class Oyente implements ActionListener{
    	public void actionPerformed(ActionEvent e) {
    		if (e.getSource() == nomenclatura) {
    			nomenVentana.setVisible(true);}
    		if (e.getSource() == perfil)
    			perfii.setVisible(true);
    		if (e.getSource() == masamolar)
    			mamol.setVisible(true);
    		if (e.getSource() == tabla)
    			tablap.setVisible(true);
    		if (e.getSource() == balanceo)
    			balanc.setVisible(true);
    		if (e.getSource() == informacion)
    			infos.setVisible(true);
    		if (e.getSource() == estequiometria)
    			estequi.setVisible(true);
    	}
    }
}
