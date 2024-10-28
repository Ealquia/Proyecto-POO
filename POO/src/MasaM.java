

import java.awt.EventQueue;

import javax.swing.JFrame;

public class MasaM {

	private static final long serialVersionUID = 1L;
	private JFrame frame;


	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MasaM ventana = new MasaM();
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}


	public MasaM() {
		frame.setVisible(true);
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

	}

}
