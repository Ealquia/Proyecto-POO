import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSplitPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.border.Border;

public class Estequio extends JFrame {
    private JTextArea instrucciones;
    private JTextField datosIngresados;
    private JSplitPane splitPaneInfo;
    private JSplitPane splitPaneBotones;
    private JButton nuevoDato;
    private JButton nuevaIncognita;
    private JComboBox tipoDato;
    private JComboBox tipoIncognita;
    private JLabel lblDatos;
    private JButton btnNuevoDato;
    private JLabel lblIncognitas;
    private JButton btnNuevaIncognita;
    private JTextField textField;
    private JLabel respuesta;
    private JButton btnResolver;
    private ControladoraEsteq Jefa;

    public Estequio() {
        initialize();
    }

    protected void initialize() {
        Jefa = new ControladoraEsteq();
        //Setups de la ventana 
        setBounds(100, 100, 450, 300);
        setTitle("Estequiometría");
        setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE); // Permitir cerrar la ventana
        setSize(500, 500);
        GridBagLayout gridBagLayout = new GridBagLayout();
        gridBagLayout.columnWidths = new int[]{561, 0};
        gridBagLayout.rowHeights = new int[]{115, 115, 115, 115, 0};
        gridBagLayout.columnWeights = new double[]{0.0, Double.MIN_VALUE};
        gridBagLayout.rowWeights = new double[]{0.0, 0.0, 0.0, 0.0, Double.MIN_VALUE};
        getContentPane().setLayout(gridBagLayout);
        
        //Instrucciones
	    instrucciones = new JTextArea("Escribe la reacción química sin balancear separada por un signo =.  \r\n          Por ejemplo: H2 + O2 = H2O\r\n          Si no te dan una reacción (si no solo un compuesto) escribe su fórmula.\r\n          Por ejemplo: H2O");
	    instrucciones.setFont(new Font("Sitka Display", Font.BOLD, 17));
	    instrucciones.setEditable(false);
	    GridBagConstraints gbc_instrucciones = new GridBagConstraints();
	    gbc_instrucciones.fill = GridBagConstraints.BOTH;
	    gbc_instrucciones.insets = new Insets(0, 0, 5, 0);
	    gbc_instrucciones.gridx = 0;
	    gbc_instrucciones.gridy = 0;
	    getContentPane().add(instrucciones, gbc_instrucciones);
	    
        //textfield para ingresar la reacción
        datosIngresados = new JTextField();
        GridBagConstraints gbc_datosIngresados = new GridBagConstraints();
        gbc_datosIngresados.fill = GridBagConstraints.BOTH;
        gbc_datosIngresados.insets = new Insets(0, 0, 5, 0);
        gbc_datosIngresados.gridx = 0;
        gbc_datosIngresados.gridy = 1;
        datosIngresados.setFont(new Font("Sitka Subheading", Font.PLAIN, 25));
        getContentPane().add(datosIngresados, gbc_datosIngresados);
        
        //Split plane con las labels de los datos
        splitPaneInfo = new JSplitPane();
        splitPaneInfo.setResizeWeight(0.5);
        GridBagConstraints gbc_splitPaneInfo = new GridBagConstraints();
        gbc_splitPaneInfo.fill = GridBagConstraints.BOTH;
        gbc_splitPaneInfo.insets = new Insets(0, 0, 5, 0);
        gbc_splitPaneInfo.gridx = 0;
        gbc_splitPaneInfo.gridy = 2;
        getContentPane().add(splitPaneInfo, gbc_splitPaneInfo);
        
        JPanel panel = new JPanel();
        splitPaneInfo.setLeftComponent(panel);
        panel.setLayout(new BorderLayout(0, 0));
        
        //Label de los datos
        lblDatos = new JLabel(Jefa.getDatos());
        lblDatos.setHorizontalAlignment(SwingConstants.CENTER);
        lblDatos.setFont(new Font("Sitka Subheading", Font.PLAIN, 18));
        Border borde = BorderFactory.createLineBorder(Color.BLACK, 5);
        lblDatos.setBorder(borde);
        panel.add(lblDatos, BorderLayout.NORTH);
        
        //DropDown de tipo dato
        tipoDato = new JComboBox<>(new String[]{"Masa", "Volumen de solución", "Volumen de líquido","Volumen de gas","Cantidad de materia"});
        panel.add(tipoDato, BorderLayout.CENTER);
        
        //Botón para agregarDato
        btnNuevoDato = new JButton("+");
        btnNuevoDato.setFont(new Font("Sitka Subheading", Font.BOLD, 30));
        panel.add(btnNuevoDato, BorderLayout.EAST);
        //Funcionalidad del botón
        btnNuevoDato.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                String tipo = tipoDato.getSelectedItem().toString();
                Jefa.anadirDato(false, tipo, datosIngresados.getText(), lblDatos);
            }
        });
        
        //TextField para el porcentaje de error
        textField = new JTextField("Porcentaje de error (opcional)");
        textField.setFont(new Font("Sitka Subheading", Font.PLAIN, 18));
        panel.add(textField, BorderLayout.SOUTH);
        textField.setColumns(10);
        
        //Panel de las incógnitas
        JPanel panel_1 = new JPanel();
         splitPaneInfo.setRightComponent(panel_1);
         panel_1.setLayout(new BorderLayout(0, 0));
         
         //Label Incógnitas
         lblIncognitas = new JLabel("New label");
         lblIncognitas.setHorizontalAlignment(SwingConstants.CENTER);
         lblIncognitas.setFont(new Font("Sitka Subheading", Font.PLAIN, 18));
         panel_1.add(lblIncognitas, BorderLayout.NORTH);

         //Combobox de tipoIncognita
         tipoIncognita = new JComboBox(new String[]{"Masa", "Volumen de solución", "Volumen de líquido","Volumen de gas","Molaridad","Presión de un gas",
             "Temperatura de un gas","Cantidad de materia", "Porcentaje de rendimiento"});
         panel_1.add(tipoIncognita, BorderLayout.CENTER);
         
         //Botón para añadir incógnita
         btnNuevaIncognita = new JButton("+");
         btnNuevaIncognita.setFont(new Font("Sitka Subheading", Font.BOLD, 30));
         btnNuevaIncognita.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                String tipo = tipoIncognita.getSelectedItem().toString();
                Jefa.anadirDato(true, tipo, datosIngresados.getText(), lblIncognitas);
            }
         });
         panel_1.add(btnNuevaIncognita, BorderLayout.EAST);
         
         //Botón para resolver
         btnResolver = new JButton("Resolver");
         btnResolver.setBackground(Color.BLUE);
         btnResolver.setForeground(Color.WHITE);
         btnResolver.setFont(new Font("Sitka Subheading", Font.BOLD, 18));
         btnResolver.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                String porcentaje = textField.getText().equals("Porcentaje de error (opcional)")? "100" : textField.getText();
                String Respuesta = Jefa.resolverProblema(datosIngresados.getText(), porcentaje);
                respuesta.setText(Respuesta);
            }
         });
         panel_1.add(btnResolver, BorderLayout.SOUTH);
    
         //Label de respuesta
        respuesta = new JLabel("");
        respuesta.setHorizontalAlignment(SwingConstants.CENTER);
        respuesta.setFont(new Font("Sitka Subheading", Font.BOLD, 18));
        GridBagConstraints gbc_respuesta = new GridBagConstraints();
        gbc_respuesta.fill = GridBagConstraints.BOTH;
        gbc_respuesta.gridx = 0;
        gbc_respuesta.gridy = 3;
        getContentPane().add(respuesta, gbc_respuesta);
        GridBagLayout gbl_panel = new GridBagLayout();
        gbl_panel.columnWidths = new int[]{0, 0};
        gbl_panel.rowHeights = new int[]{0, 0};
        gbl_panel.columnWeights = new double[]{1.0, Double.MIN_VALUE};
        gbl_panel.rowWeights = new double[]{0.0, Double.MIN_VALUE};

    }

    public void setInstrucciones(String texto) {
        instrucciones.setText(texto);
    }

    public String getDatosIngresados() {
        return datosIngresados.getText();
    }

}