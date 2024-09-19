package src;

import java.awt.EventQueue;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class PaginaGUI {
	
	private JFrame frame;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		PaginaGUI window = new PaginaGUI();
		window.getFrame().setVisible(true);
				
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
		setFrame(new JFrame());
		getFrame().setBounds(100, 100, 450, 300);
	    getFrame().setTitle("Pagina GUI");
	    getFrame().setSize(400, 300);
	    getFrame().setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	    //frame.setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE);

	        instrucciones = new JTextArea();
	        datosIngresados = new JTextField();
	        botonRegistrar = new JButton("Registrar");
	        respuesta = new JLabel();
	        getFrame().setLayout(new GridLayout(4, 1));
	        getFrame().add(instrucciones);
	        getFrame().add(datosIngresados);
	        getFrame().add(botonRegistrar);
	        getFrame().add(respuesta);
	}
	
	public JFrame getFrame() {
		return frame;
	}

	public void setFrame(JFrame frame) {
		this.frame = frame;
	}

	private class Oyente implements ActionListener{

		@Override
		public void actionPerformed(ActionEvent e) {
			// TODO Auto-generated method stub
			
		}
		
	}

}
