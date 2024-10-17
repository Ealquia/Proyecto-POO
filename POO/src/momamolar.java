import java.awt.EventQueue;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JInternalFrame;
import javax.swing.BoxLayout;
import javax.swing.JTextPane;
import java.awt.BorderLayout;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.Font;
import java.awt.Color;
import org.python.util.PythonInterpreter;
import org.python.core.*;

public class Momamolar extends PaginaGUI {

    private static final long serialVersionUID = 1L;
    private JPanel PanelMoma;
    private JTextField Compingresado;
    private PythonInterpreter miPython;

    /**
     * Launch the application.
     */
    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable() {
            public void run() {
                try {
                    Momamolar frame = new Momamolar();
                    frame.setVisible(true);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }

    /**
     * Create the frame.
     */
    public Momamolar() {
        super();

        miPython = new PythonInterpreter();
        miPython.execfile("./src/CalcMasaMolar.py");

        // Llamar a la función definida en el archivo Python
        PyFunction funcionSaludo = (PyFunction) miPython.get("saludo", PyFunction.class);

        // Pasar un argumento a la función Python
        PyObject resultado = funcionSaludo.__call__(new PyString("H2O"));

        miPython.close();

        // Configuración del frame
        setTitle("MomaMolar");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(200, 200, 900, 600);
        PanelMoma = new JPanel();
        PanelMoma.setBorder(new EmptyBorder(5, 5, 5, 5));
        setContentPane(PanelMoma);
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
        Compingresado.setText("Ingrese su compuesto aquí:");
        Compingresado.setToolTipText("Ingrese el compuesto químico");
        Ingresodatos.add(Compingresado);
        Compingresado.setColumns(10);

        // Botón para calcular la masa molar
        JButton Registrar = new JButton("Calcular");
        Ingresodatos.add(Registrar);

        // Área de texto para mostrar el resultado
        JTextPane Resultado = new JTextPane();
        Resultado.setEditable(false);
        Resultado.setText("La masa molar de su compuesto es:\r\n");
        Ingresodatos.add(Resultado);
    }
}

