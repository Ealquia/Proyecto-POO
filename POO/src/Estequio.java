import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JSplitPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.border.Border;

public class Estequio extends JFrame {
    private JTextArea instrucciones;
    private JTextField datosIngresados;
    private JSplitPane splitPaneInfo;
    private JSplitPane splitPaneBotones;
    private JComboBox tipoDato;
    private JComboBox tipoIncognita;
    private JTextArea lblDatos;
    private JTextArea lblIncognitas;
    private JTextField textField;
    private JTextArea respuesta;
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
	    instrucciones = new JTextArea("Escribe la reacción química sin balancear separada por un signo =.  \r\n          Por ejemplo: H2 + O2 = H2O\r\n          Si no te dan una reacción (si no solo un compuesto) escribe su fórmula.\r\n          Por ejemplo: H2O\r\n      Presiona enter antes de continuar");
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
        datosIngresados.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Deshabilitar la edición del JTextField al presionar Enter
                datosIngresados.setEditable(false);
            }
        });
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
        lblDatos = new JTextArea("DATOS: \n");
        lblDatos.setFont(new Font("Sitka Subheading", Font.PLAIN, 15));
        lblDatos.setEditable(false);
        Border borde = BorderFactory.createLineBorder(Color.BLACK, 3);
        lblDatos.setBorder(borde);
        panel.add(lblDatos, BorderLayout.NORTH);
        
        //DropDown de tipo dato
        tipoDato = new JComboBox<>(new String[]{"¿Qué me dan en el problema?", "Masa", "Volumen de solución", "Volumen de líquido","Volumen de gas","Cantidad de materia"});
        panel.add(tipoDato, BorderLayout.CENTER);
        
        //Botón para agregarDato
        JButton btnNuevoDato = new JButton("Añadir dato");
        btnNuevoDato.setFont(new Font("Sitka Subheading", Font.BOLD, 15));
        panel.add(btnNuevoDato, BorderLayout.EAST);
        //Funcionalidad del botón
        btnNuevoDato.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                if (datosIngresados.getText().isEmpty())
                    JOptionPane.showMessageDialog(null, "Debe ingresar una reacción o un compuesto", "Error", JOptionPane.ERROR_MESSAGE);
                else {
                    if (tipoDato.getSelectedIndex()==0)
                        JOptionPane.showMessageDialog(null, "Elija un tipo de dato", "Error", JOptionPane.ERROR_MESSAGE);
                    else {
                        String tipo = tipoDato.getSelectedItem().toString();
                        Jefa.anadirDato(false, tipo, datosIngresados.getText(), lblDatos); }
                }
            }
        });
        
        //TextField para el porcentaje de error
        textField = new JTextField("Porcentaje de error (opcional)");
        textField.setFont(new Font("Sitka Subheading", Font.PLAIN, 18));
        panel.add(textField, BorderLayout.SOUTH);
        textField.setColumns(10);
        textField.addFocusListener(new FocusListener() {
            @Override
            public void focusGained(FocusEvent e) {
                // Borrar el texto cuando el campo recibe el foco
                textField.setText("");
            }
            @Override
            public void focusLost(FocusEvent e) {
            }
        });
        textField.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Deshabilitar la edición del JTextField al presionar Enter
                textField.setEditable(false);
            }
        });

        
        //Panel de las incógnitas
        JPanel panel_1 = new JPanel();
         splitPaneInfo.setRightComponent(panel_1);
         panel_1.setLayout(new BorderLayout(0, 0));
         
         //Label Incógnitas
         lblIncognitas = new JTextArea("INCÓGNITAS: \n");
         lblIncognitas.setEditable(false);
         lblIncognitas.setFont(new Font("Sitka Subheading", Font.PLAIN, 15));
         lblIncognitas.setBorder(borde);
         panel_1.add(lblIncognitas, BorderLayout.NORTH);

         //Combobox de tipoIncognita
         tipoIncognita = new JComboBox(new String[]{"¿Qué tengo que encontrar?", "Masa", "Volumen de solución", "Volumen de líquido","Volumen de gas","Molaridad","Presión de un gas",
             "Temperatura de un gas","Cantidad de materia", "Porcentaje de rendimiento"});
         panel_1.add(tipoIncognita, BorderLayout.CENTER);
         
         //Botón para añadir incógnita
         JButton btnNuevaIncognita = new JButton("Añadir incógnita");
         btnNuevaIncognita.setFont(new Font("Sitka Subheading", Font.BOLD, 15));
         btnNuevaIncognita.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                if (datosIngresados.getText().isEmpty())
                    JOptionPane.showMessageDialog(null, "Debe ingresar una reacción o un compuesp", "Error", JOptionPane.ERROR_MESSAGE);
                else {
                    String tipo = tipoIncognita.getSelectedItem().toString();
                    Jefa.anadirDato(true, tipo, datosIngresados.getText(), lblIncognitas); }
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
        respuesta = new JTextArea("");
        respuesta.setFont(new Font("Sitka Subheading", Font.BOLD, 18));
        respuesta.setEditable(false);
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