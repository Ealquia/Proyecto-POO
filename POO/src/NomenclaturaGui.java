import java.awt.BorderLayout;
import java.awt.Component;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.JPopupMenu;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;

public class NomenclaturaGui extends JDialog {

	private static final long serialVersionUID = 1L;
	private final JPanel contentPanel = new JPanel();
	private JTextField TextoQueIngresa;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		try {
			NomenclaturaGui dialog = new NomenclaturaGui();
			dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Create the dialog.
	 */
	public NomenclaturaGui() {
		setBounds(100, 100, 479, 323);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		contentPanel.setLayout(new GridLayout(0, 1, 0, 0));
		{
			JLabel TextoQueSeMuestra = new JLabel("<html>Bienvenido, usa los menús de arriba para seleccionar el nivel que deseas practircar.<html>");
			contentPanel.add(TextoQueSeMuestra);
			{
				JPopupMenu popupMenu = new JPopupMenu();
				addPopup(TextoQueSeMuestra, popupMenu);
				{
					JMenu IonesQueRepasar = new JMenu("Iones a repasar");
					popupMenu.add(IonesQueRepasar);
					{
						JMenuItem Nivel1IonesMenuPopUp = new JMenuItem("Nivel 1");
						IonesQueRepasar.add(Nivel1IonesMenuPopUp);
					}
					{
						JMenuItem Nivel2IonesMenuPopUp = new JMenuItem("Nivel 2");
						IonesQueRepasar.add(Nivel2IonesMenuPopUp);
					}
					{
						JMenuItem Nivel3IonesMenuPopUp = new JMenuItem("Nivel 3");
						IonesQueRepasar.add(Nivel3IonesMenuPopUp);
					}
					{
						JMenuItem Nivel4IonesMenuPopUp = new JMenuItem("Nivel 4");
						IonesQueRepasar.add(Nivel4IonesMenuPopUp);
					}
					{
						JMenuItem TodoslosNivelesMenuPopUp = new JMenuItem("Todos los niveles");
						IonesQueRepasar.add(TodoslosNivelesMenuPopUp);
					}
				}
				{
					JMenuItem GraduarCantidadPreguntas = new JMenuItem("Graduar cantidad de preguntas a realizar");
					popupMenu.add(GraduarCantidadPreguntas);
				}
			}
		}
		{
			TextoQueIngresa = new JTextField();
			contentPanel.add(TextoQueIngresa);
			TextoQueIngresa.setColumns(10);
		}
		{
			JLabel TextoRespuesta = new JLabel("<html>Aquí se mostrará la solución en caso de que la respuesta sea incorrecta.<html>");
			contentPanel.add(TextoRespuesta);
		}
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				JButton ingresarButton = new JButton("Ingresar respuesta");
				ingresarButton.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
					}
				});
				{
					JLabel ContadorAciertos = new JLabel("Aciertos");
					buttonPane.add(ContadorAciertos);
				}
				{
					JLabel Slash = new JLabel("/");
					buttonPane.add(Slash);
				}
				{
					JLabel NumeroPreguntas = new JLabel("N.o. preguntas");
					buttonPane.add(NumeroPreguntas);
				}
				ingresarButton.setActionCommand("OK");
				buttonPane.add(ingresarButton);
				getRootPane().setDefaultButton(ingresarButton);
			}
			{
				JButton saltarButton = new JButton("Saltar pregunta");
				saltarButton.setActionCommand("Cancel");
				buttonPane.add(saltarButton);
			}
		}
		{
			JMenuBar menuBar = new JMenuBar();
			setJMenuBar(menuBar);
			{
				JMenu SeleccionIonesMenu = new JMenu("Iones a Repasar");
				menuBar.add(SeleccionIonesMenu);
				{
					JMenuItem Nivel1IonesMenuItem = new JMenuItem("Nivel 1");
					SeleccionIonesMenu.add(Nivel1IonesMenuItem);
				}
				{
					JMenuItem Nivel2IonesMenuItem = new JMenuItem("Nivel 2");
					SeleccionIonesMenu.add(Nivel2IonesMenuItem);
				}
				{
					JMenuItem Nivel3IonesMenuItem = new JMenuItem("Nivel 3");
					SeleccionIonesMenu.add(Nivel3IonesMenuItem);
				}
				{
					JMenuItem Nivel4IonesMenuItem = new JMenuItem("Nivel 4");
					SeleccionIonesMenu.add(Nivel4IonesMenuItem);
				}
				{
					JMenuItem TodosLosNivelesMenuItem = new JMenuItem("Todos los niveles");
					SeleccionIonesMenu.add(TodosLosNivelesMenuItem);
				}
			}
			{
				JMenu CantidadPreguntasMenu = new JMenu("Cantidad de preguntas a realizar");
				menuBar.add(CantidadPreguntasMenu);
				{
					JMenuItem mntmNewMenuItem = new JMenuItem("Graduar la cantidad de preguntas");
					CantidadPreguntasMenu.add(mntmNewMenuItem);
				}
			}
		}
	}

	private static void addPopup(Component component, final JPopupMenu popup) {
		component.addMouseListener(new MouseAdapter() {
			public void mousePressed(MouseEvent e) {
				if (e.isPopupTrigger()) {
					showMenu(e);
				}
			}
			public void mouseReleased(MouseEvent e) {
				if (e.isPopupTrigger()) {
					showMenu(e);
				}
			}
			private void showMenu(MouseEvent e) {
				popup.show(e.getComponent(), e.getX(), e.getY());
			}
		});
	}

	public void actionPerformed (ActionEvent e) {
		JMenuItem source = (JMenuItem)  e.getSource();
		

	}


}

