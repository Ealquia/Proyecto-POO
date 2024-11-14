import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
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
    private NomenclaturaGui nomenVentana;
    private Perfil perfii;
    private momamolar mamol;  // Nombre corregido
    private TablaP tablap;
    private Balanceo balanc;
    private informacion infos; // Nombre corregido
    private Estequio estequi;

    public static void main(String[] args) {
        try {
            ProcessBuilder processBuilder = new ProcessBuilder("python", "POO\\src\\app.py");
            processBuilder.redirectErrorStream(true);
            Process process = processBuilder.start();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        // Esto va en el main para lanzar la aplicación
        EventQueue.invokeLater(new Runnable() {
            public void run() {
                try {
                    Home window = new Home();
                    window.frame.setVisible(true);  // Mostrar ventana
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }

    public Home() {
        initialize();
    }

    private void initialize() {
        frame = new JFrame();
        frame.setTitle("Pagina de Inicio");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Inicializar todas las ventanas correctamente
        nomenVentana = new NomenclaturaGui();
        perfii = new Perfil();
        mamol = new momamolar(); // Inicialización corregida
        tablap = new TablaP();
        balanc = new Balanceo();
        infos = new informacion(); // Nombre corregido
        estequi = new Estequio();

        // Toda la pantalla
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        int screenWidth = toolkit.getScreenSize().width;
        int screenHeight = toolkit.getScreenSize().height;
        frame.setSize(screenWidth, screenHeight);
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);

        // Pantalla de fondo

        
        
        
        BackgroundPanel panel = new BackgroundPanel(new ImageIcon(Home.class.getResource("T1.png")).getImage());
        panel.setLayout(null); // Posición absoluta
        frame.getContentPane().add(panel);

        Oyente mp = new Oyente();

        // Añadir los botones
        nomenclatura = new JButton("Nom");
        nomenclatura.setBounds(1170, 127, 75, 74);
        nomenclatura.setBackground(Color.PINK);
        panel.add(nomenclatura);
        nomenclatura.addActionListener(mp);

        masamolar = new JButton("Mol");
        masamolar.setBounds(482, 345, 75, 75);
        masamolar.setBackground(Color.ORANGE);
        panel.add(masamolar);
        masamolar.addActionListener(mp);

        tabla = new JButton("Tabl");
        tabla.setBounds(407, 420, 75, 75);
        tabla.setBackground(Color.ORANGE);
        panel.add(tabla);
        tabla.addActionListener(mp);

        perfil = new JButton("Perf");
        perfil.setBounds(1170, 202, 75, 74);
        perfil.setBackground(Color.PINK);
        panel.add(perfil);
        perfil.addActionListener(mp);

        balanceo = new JButton("Balan");
        balanceo.setBounds(252, 420, 75, 75);
        balanceo.setBackground(Color.BLUE);
        panel.add(balanceo);
        balanceo.addActionListener(mp);

        informacion = new JButton("inf");
        informacion.setBounds(1325, 345, 75, 75);
        informacion.setBackground(Color.RED);
        panel.add(informacion);
        informacion.addActionListener(mp);

        estequiometria = new JButton("Est");
        estequiometria.setBounds(1133, 670, 75, 74);
        estequiometria.setBackground(Color.WHITE);
        panel.add(estequiometria);
        estequiometria.addActionListener(mp);

        // Añadir el panel con la imagen de fondo al frame
        frame.getContentPane().add(panel, BorderLayout.CENTER);
    }

    // Custom JPanel class para manejar la imagen de fondo
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

    // Clase oyente para manejar las acciones de los botones
    private class Oyente implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            if (e.getSource() == nomenclatura) {
                nomenVentana.setVisible(true);
            }
            if (e.getSource() == perfil) {
                perfii.setVisible(true);
            }
            if (e.getSource() == masamolar) {
                mamol.getFrame().setVisible(true);
            }
            if (e.getSource() == tabla) {
                tablap.setVisible(true);
            }
            if (e.getSource() == balanceo) {
                balanc.setVisible(true);
            }
            if (e.getSource() == informacion) {
                infos.setVisible(true);
            }
            if (e.getSource() == estequiometria) {
                estequi.setVisible(true);
            }
        }
    }
}
