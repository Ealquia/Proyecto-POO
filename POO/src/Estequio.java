import java.awt.GridLayout;
import java.awt.Toolkit;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.JSplitPane;
import javax.swing.border.CompoundBorder;
import javax.swing.border.EtchedBorder;
import java.awt.Color;
import javax.swing.AbstractListModel;
import javax.swing.ListSelectionModel;
import java.awt.Font;
import javax.swing.JRadioButton;
import javax.swing.SwingConstants;

public class Estequio extends JFrame {
    private JTextArea instrucciones;
    private JTextField datosIngresados;
    private JLabel respuesta;
    private JSplitPane splitPane;
    private JList Datos;
    private JList Incognitas;

    public Estequio() {
        initialize();
    }

    protected void initialize() {
        setBounds(100, 100, 450, 300);
        setTitle("Estequiometría");
        setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE); // Permitir cerrar la ventana
        setSize(500, 500);

        instrucciones = new JTextArea("Escribe la reacción química sin balancear separada por un signo =.  \r\n          Por ejemplo: H2 + O2 = H2O\r\n          Si no te dan una reacción (si no solo un compuesto) escribe su fórmula.\r\n          Por ejemplo: H2O");
        instrucciones.setFont(new Font("Sitka Display", Font.BOLD, 17));
        instrucciones.setEditable(false);
        datosIngresados = new JTextField();
        respuesta = new JLabel();

        getContentPane().setLayout(new GridLayout(4, 1));
        getContentPane().add(instrucciones);
        getContentPane().add(datosIngresados);
        
        splitPane = new JSplitPane();
        splitPane.setResizeWeight(0.5);
        getContentPane().add(splitPane);
        
        Datos = new JList();
        Datos.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        Datos.setLayoutOrientation(JList.VERTICAL_WRAP);
        Datos.setModel(new AbstractListModel() {
        	String[] values = new String[] {"\"Masa\"", "\"Volumen Líquido\"", "\"Volumen Solución\"", "\"Volumen de Gas\""};
        	public int getSize() {
        		return values.length;
        	}
        	public Object getElementAt(int index) {
        		return values[index];
        	}
        });
        Datos.setBorder(new CompoundBorder(new EtchedBorder(EtchedBorder.LOWERED, new Color(255, 0, 0), null), new EtchedBorder(EtchedBorder.LOWERED, new Color(255, 200, 0), null)));
        splitPane.setLeftComponent(Datos);
        
        Incognitas = new JList();
        Incognitas.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        Incognitas.setLayoutOrientation(JList.VERTICAL_WRAP);
        Incognitas.setBorder(new CompoundBorder(new EtchedBorder(EtchedBorder.LOWERED, new Color(255, 0, 0), new Color(255, 255, 255)), new EtchedBorder(EtchedBorder.LOWERED, new Color(255, 200, 0), null)));
        Incognitas.setModel(new AbstractListModel() {
        	String[] values = new String[] {"\"Masa\" ", "\"Volumen de solución\"", "\"Volumen de líquido\"", "\"Volumen de gas\"", "\"Molaridad\"", "\"Presión de un gas\"", "\"Temperatura de un gas\"", "\"Cantidad de materia\""};
        	public int getSize() {
        		return values.length;
        	}
        	public Object getElementAt(int index) {
        		return values[index];
        	}
        });
        splitPane.setRightComponent(Incognitas);
        getContentPane().add(respuesta);
    }

    public void setInstrucciones(String texto) {
        instrucciones.setText(texto);
    }

    public String getDatosIngresados() {
        return datosIngresados.getText();
    }

    public void setRespuesta(String texto) {
        respuesta.setText(texto);
    }
}