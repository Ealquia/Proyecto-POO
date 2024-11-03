

import javax.swing.JPanel;
import javax.swing.JTextField;

public class momamolar2 extends PaginaGUI{

	private static final long serialVersionUID = 1L;
	private JPanel PanelMoma;
	private JTextField Compingresado;

	/**
	 * Launch the application.
	 */
/*	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					momamolar frame = new momamolar();
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
	public momamolar2() {
		super();
		/*
		miPython = new PythonInterpreter();
		miPython.execfile("./src/CalcMasaMolar.py");
		// Llamar a la función definida en el archivo Python
        PyFunction funcionSaludo = (PyFunction) miPython.get("saludo", PyFunction.class);

        // Pasar un argumento a la función Python
        PyObject resultado = funcionSaludo.__call__(new PyString("H2O"));

		 
        miPython.close();*/
		frame.setTitle("MomaMolar");
		frame.setVisible(true);
		/*setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(200, 200, 900, 600);
		PanelMoma = new JPanel();
		PanelMoma.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(PanelMoma);
		PanelMoma.setLayout(new BoxLayout(PanelMoma, BoxLayout.X_AXIS));
		
		JInternalFrame Frameinterno = new JInternalFrame("Instrucciones:");
		PanelMoma.add(Frameinterno);
		
		JTextPane Instrucciones = new JTextPane();
		Instrucciones.setBackground(new Color(128, 255, 255));
		Instrucciones.setForeground(new Color(64, 0, 64));
		Instrucciones.setFont(new Font("Verdana", Font.BOLD | Font.ITALIC, 14));
		Instrucciones.setText("¡Bienvenido a la calculadora de Masa molar!\r\n\r\nIngrese el elemento del que desea calcular su Masa Molar. \r\nLa forma de ingresar un elemento es de este estilo:\r\nEjemplo Agua: H2O");
		Instrucciones.setEditable(false);
		*/
		instrucciones.setText("¡Bienvenido a la calculadora de Masa molar!\r\n\r\nIngrese el elemento del que desea calcular su Masa Molar. \r\nLa forma de ingresar un elemento es de este estilo:\r\nEjemplo Agua: H2O");
		//Frameinterno.getContentPane().add(Instrucciones, BorderLayout.NORTH);
		
		/*JPanel Ingresodatos = new JPanel();
		
		Frameinterno.getContentPane().add(Ingresodatos, BorderLayout.CENTER);
		Ingresodatos.setLayout(new BoxLayout(Ingresodatos, BoxLayout.X_AXIS));
		
		Compingresado = new JTextField();
		Compingresado.setText("Ingrese su elemento aqui:");
		Compingresado.setToolTipText("");
		Ingresodatos.add(Compingresado);
		Compingresado.setColumns(10);
		
		JButton Registrar = new JButton("Calcular");
		Ingresodatos.add(Registrar);
		
		JTextPane Resultado = new JTextPane();
		Resultado.setEditable(false);
		Resultado.setText("La masa molar de su elemento es:\r\n");
		Ingresodatos.add(Resultado);
		Frameinterno.setVisible(true);*/
	}

}
