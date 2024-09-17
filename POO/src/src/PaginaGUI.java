package src;

import java.awt.EventQueue;
import java.awt.GridLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class PaginaGUI {
	  private JTextArea instrucciones;
	  private JTextField datosIngresados;
	  private JButton botonRegistrar;
	  private JLabel respuesta;


	private JFrame frame;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		PaginaGUI window = new PaginaGUI();
		window.frame.setVisible(true);
				
	}

	/**
	 * Create the application.
	 */
	public PaginaGUI() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	    frame.setTitle("Pagina GUI");
	    frame.setSize(400, 300);
	    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

	        instrucciones = new JTextArea();
	        datosIngresados = new JTextField();
	        botonRegistrar = new JButton("Registrar");
	        respuesta = new JLabel();
	        frame.setLayout(new GridLayout(4, 1));
	        frame.add(instrucciones);
	        frame.add(datosIngresados);
	        frame.add(botonRegistrar);
	        frame.add(respuesta);
	}

}
