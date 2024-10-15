

import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class BackgroundGridLayoutFrame extends JFrame {

    private Image backgroundImage;

    public BackgroundGridLayoutFrame() {
        // Load the image (Escape backslashes or use forward slashes)
        try {
            backgroundImage = ImageIO.read(new File("C:/Users/esteb/OneDrive/Escritorio/UVG/UVG 2024 EHVM/Segundo Semestre/PROGRAMACIÓN ORIENTADA A OBJETOS/Proyecto Progra/POO/src/src/Tabla periodica.png"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Set frame properties
        setTitle("Background with GridLayout Example");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Create a custom JPanel with a background image
        BackgroundPanel backgroundPanel = new BackgroundPanel();
        backgroundPanel.setLayout(new GridLayout(3, 2, 10, 10)); // 3 rows, 2 columns, 10px gap

        // Add components to the grid layout
        backgroundPanel.add(new JButton("Button 1"));
        backgroundPanel.add(new JButton("Button 2"));
        backgroundPanel.add(new JButton("Button 3"));
        backgroundPanel.add(new JButton("Button 4"));
        backgroundPanel.add(new JButton("Button 5"));
        backgroundPanel.add(new JButton("Button 6"));

        // Set content pane
        setContentPane(backgroundPanel);
    }

    // Custom JPanel class to handle the background image
    class BackgroundPanel extends JPanel {
        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            // Draw the background image
            g.drawImage(backgroundImage, 0, 0, getWidth(), getHeight(), this);
        }
    }
}
