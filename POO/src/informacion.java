import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;

public class informacion extends JFrame {
    private JButton BotonA;

    public informacion() {
        setTitle("Información de Química");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);
        setLocationRelativeTo(null);

        BotonA = new JButton("Descargar tabla Periodica");
        BotonA.addActionListener(new DownloadAction());

        getContentPane().setLayout(new BorderLayout());
        getContentPane().add(BotonA, BorderLayout.CENTER);
    }

    private class DownloadAction implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            try {
                String userHome = System.getProperty("user.home");
                File desktop = new File(userHome, "Desktop");
                File pdfFile = new File(desktop, "downloaded.pdf");

                // Ruta local del archivo PDF
                File localPdf = new File("C:\\Users\\esteb\\OneDrive\\Escritorio\\UVG\\UVG 2024 EHVM\\Segundo Semestre\\PROGRAMACIÓN ORIENTADA A OBJETOS\\Proyecto Progra\\POO\\src\\TABLA_LA.pdf");
                
                // Copiar el archivo local al escritorio
                Files.copy(localPdf.toPath(), pdfFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
                JOptionPane.showMessageDialog(null, "Descarga correcta");
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(null, "No se descargo el PDF debido a: " + ex.getMessage());
            }
        }
    }

    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            informacion downloader = new informacion();
            downloader.setVisible(true);
        });
    }
}