import java.awt.BorderLayout;
import java.awt.Component;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
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
	private JLabel TextoQueSeMuestra;
	private int Nivel= 0;
	private int ID = 0;
	private String Problema= "";
	private String Respuesta = "";
	private String Solucion = "";
	private String Comprobante = "";
	private JButton ingresarButton;
	private JLabel ContadorAciertos;
	private int Aciertos = 0;
	private JLabel NumeroPreguntas;
	private int NoPreguntas = 0;
	private JLabel TextoRespuesta;

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

	public String getProblema(){
		return Problema;
	}

	public void setProblema(String problema){
		this.Problema = problema;
	}

	public int getAciertos() {
        return Aciertos;
    }

    public void setAciertos(int Aciertos) {
        this.Aciertos = Aciertos;
    }

	public void aumentarAciertos(){
		this.Aciertos += 1;
	}

    public int getNoPreguntas() {
        return NoPreguntas;
    }

    public void setNoPreguntas(int NoPreguntas) {
        this.NoPreguntas = NoPreguntas;
    }

	public void aumentarNoPreguntas(){
		this.NoPreguntas += 1;
	}

	public String getComprobante(){
		return this.Comprobante;
	}
	
	public void setComprobante(String comprobante){
		this.Comprobante = comprobante;
	}

	public String getSolucion(){
		return this.Solucion;
	}

	public void setSolucion(String solucion){
		this.Solucion = solucion;
	}

	public static long getSerialversionuid() {
		return serialVersionUID;
	}

	public JPanel getContentPanel() {
		return contentPanel;
	}

	public JTextField getTextoQueIngresa() {
		return TextoQueIngresa;
	}

	public void setTextoQueIngresa(JTextField textoQueIngresa) {
		TextoQueIngresa = textoQueIngresa;
	}

	public JLabel getTextoQueSeMuestra() {
		return TextoQueSeMuestra;
	}

	public void setTextoQueSeMuestra(JLabel textoQueSeMuestra) {
		TextoQueSeMuestra = textoQueSeMuestra;
	}

	public int getNivel() {
		return Nivel;
	}

	public void setNivel(int nivel) {
		Nivel = nivel;
	}

	public int getID() {
		return ID;
	}

	public void setID(int iD) {
		ID = iD;
	}

	public String getRespuesta() {
		return Respuesta;
	}

	public void setRespuesta(String respuesta) {
		Respuesta = respuesta;
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
	
		TextoQueSeMuestra = new JLabel("<html>Bienvenido, usa los menús de arriba para seleccionar el nivel que deseas practircar.<html>");
		contentPanel.add(TextoQueSeMuestra);
		
		JPopupMenu popupMenu = new JPopupMenu();
		addPopup(TextoQueSeMuestra, popupMenu);
		
		JMenu IonesQueRepasar = new JMenu("Iones a repasar");
		popupMenu.add(IonesQueRepasar);
	
		JMenuItem Nivel1IonesMenuPopUp = new JMenuItem("Nivel 1");
		IonesQueRepasar.add(Nivel1IonesMenuPopUp);
		
	
	
		JMenuItem Nivel2IonesMenuPopUp = new JMenuItem("Nivel 2");
		IonesQueRepasar.add(Nivel2IonesMenuPopUp);
	
	
		JMenuItem Nivel3IonesMenuPopUp = new JMenuItem("Nivel 3");
		IonesQueRepasar.add(Nivel3IonesMenuPopUp);
	
	
		JMenuItem Nivel4IonesMenuPopUp = new JMenuItem("Nivel 4");
		IonesQueRepasar.add(Nivel4IonesMenuPopUp);
	
	
		JMenuItem TodoslosNivelesMenuPopUp = new JMenuItem("Todos los niveles");
		IonesQueRepasar.add(TodoslosNivelesMenuPopUp);
					
				
				
		JMenuItem GraduarCantidadPreguntas = new JMenuItem("Graduar cantidad de preguntas a realizar");
		popupMenu.add(GraduarCantidadPreguntas);
				
			
		
		
		TextoQueIngresa = new JTextField();
		contentPanel.add(TextoQueIngresa);
		TextoQueIngresa.setColumns(10);
	
	
		TextoRespuesta = new JLabel("<html>Aquí se mostrará la solución en caso de que la respuesta sea incorrecta.<html>");
		contentPanel.add(TextoRespuesta);
	
	
		JPanel buttonPane = new JPanel();
		buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
		getContentPane().add(buttonPane, BorderLayout.SOUTH);
	
		ingresarButton = new JButton("Ingresar respuesta");
		ingresarButton.addActionListener(e -> comprobarRespuestaPorNivel(this.getNivel(), this.getID()));
		
		ContadorAciertos = new JLabel("Aciertos");
		buttonPane.add(ContadorAciertos);
	
	
		JLabel Slash = new JLabel("/");
		buttonPane.add(Slash);
	
	
		NumeroPreguntas = new JLabel("N.o. preguntas");
		buttonPane.add(NumeroPreguntas);
	
		ingresarButton.setActionCommand("OK");
		buttonPane.add(ingresarButton);
		getRootPane().setDefaultButton(ingresarButton);
	
	
		JButton saltarButton = new JButton("Saltar pregunta");
		saltarButton.addActionListener(e-> comprobarRespuestaPorNivel(this.getNivel(), this.getID()));
		buttonPane.add(saltarButton);
			
		
	
		JMenuBar menuBar = new JMenuBar();
		setJMenuBar(menuBar);
		
		JMenu SeleccionIonesMenu = new JMenu("Iones a Repasar");
		menuBar.add(SeleccionIonesMenu);
	
		JMenuItem Nivel1IonesMenuItem = new JMenuItem("Nivel 1");
		//Nivel1IonesMenuItem.putClientProperty("actionCommand", "nivel1");
		Nivel1IonesMenuItem.addActionListener(e -> cargarProblemPorNivel(1));
		SeleccionIonesMenu.add(Nivel1IonesMenuItem);
	
	
		JMenuItem Nivel2IonesMenuItem = new JMenuItem("Nivel 2");
		//Nivel2IonesMenuItem.putClientProperty("actionCommand", "nivel2");
		Nivel2IonesMenuItem.addActionListener(e -> cargarProblemPorNivel(2));
		SeleccionIonesMenu.add(Nivel2IonesMenuItem);
	
	
		JMenuItem Nivel3IonesMenuItem = new JMenuItem("Nivel 3");
//		Nivel3IonesMenuItem.putClientProperty("actionCommand", "nivel3");
		Nivel3IonesMenuItem.addActionListener(e -> cargarProblemPorNivel(3));
		SeleccionIonesMenu.add(Nivel3IonesMenuItem);
	
	
		JMenuItem Nivel4IonesMenuItem = new JMenuItem("Nivel 4");
		//Nivel4IonesMenuItem.putClientProperty("actionCommand", "nivel4");
		Nivel4IonesMenuItem.addActionListener(e -> cargarProblemPorNivel(4));
		SeleccionIonesMenu.add(Nivel4IonesMenuItem);
	
	
		JMenuItem TodosLosNivelesMenuItem = new JMenuItem("Todos los niveles");
		//TodosLosNivelesMenuItem.putClientProperty("actionCommand", "todos");
		TodosLosNivelesMenuItem.addActionListener(e -> cargarProblemPorNivel(5));
		SeleccionIonesMenu.add(TodosLosNivelesMenuItem);
	
	
		//JMenuItem mntmNewMenuItem = new JMenuItem("Graduar la cantidad de preguntas");
		//menuBar.add(mntmNewMenuItem);
				
			
		
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
	
	// Método para obtener el problema en formato de cadena JSON
    public String getProblemaPorNivel(int level) {
        String endpoint = "http://127.0.0.1:5000/api/ProblemaNivel" + Integer.toString(level);
        try {
            // Crear el URI y luego convertirlo a URL
            URI uri = URI.create(endpoint);
            URL url = uri.toURL();

            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");

            int responseCode = conn.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) {
                BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream(), "utf-8"));
                StringBuilder content = new StringBuilder();
                String inputLine;
                while ((inputLine = in.readLine()) != null) {
                    content.append(inputLine);
                }
                in.close();
                return content.toString(); // Devuelve la cadena JSON
            } else {
                TextoQueSeMuestra.setText("Error en la solicitud: Código de respuesta " + responseCode);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

	

	private void cargarProblemPorNivel(int level) {
		// Llamar al método que obtiene el problema de la API
		String jsonResponse = this.getProblemaPorNivel(level);

		if (jsonResponse != null) {
			// Expresiones regulares para extraer los campos "nivel", "id" y "problema"
			Pattern nivelPattern = Pattern.compile("\"nivel\":\\s*(\\d+)");
			Pattern idPattern = Pattern.compile("\"id\":\\s*(\\d+)");
			Pattern problemaPattern = Pattern.compile("\"problema\":\\s*\"([^\"]+)\"");

			Matcher nivelMatcher = nivelPattern.matcher(jsonResponse);
			Matcher idMatcher = idPattern.matcher(jsonResponse);
			Matcher problemaMatcher = problemaPattern.matcher(jsonResponse);

			int nivel = 0;
			int id = 0;
			String problema = "No se pudo obtener el problema";

			// Extraer cada valor si coincide con el patrón
			if (nivelMatcher.find()) {
				nivel = Integer.parseInt(nivelMatcher.group(1));
			}
			if (idMatcher.find()) {
				id = Integer.parseInt(idMatcher.group(1));
			}
			if (problemaMatcher.find()) {
				problema = problemaMatcher.group(1);
			}

			// Actualizar la interfaz gráfica (reemplaza TextoQueSeMuestra por el nombre de tu JLabel)
			TextoQueSeMuestra.setText("<html>" + problema + "<html>");
			this.setNivel(nivel);
			this.setID(id);
			this.setProblema(problema);
		} else {
			TextoQueSeMuestra.setText("No se pudo cargar el problema. Intenta nuevamente.");
		}
	}
	
	private void comprobarRespuestaPorNivel (int level, int id){
		String endpoint = "http://127.0.0.1:5000/api/SolucionProblema";
		try {
            // Crear el URI y luego convertirlo a URL
            URI uri = URI.create(endpoint);
            URL url = uri.toURL();

            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
			conn.setRequestProperty("Content-Type", "application/json; utf-8"); // Formato de datos de entrada
            conn.setRequestProperty("Accept", "application/json"); // Formato de datos de salida esperado
            conn.setDoOutput(true); // Permite enviar datos en el cuerpo de la solicitud

			if(TextoQueIngresa.getText().equalsIgnoreCase("")){
				String jsonInputString ="{\"nivel\": \""+level+ "\", "+ "\"problema\":\""+ this.getProblema()+ "\", "+"\"solución\": \"" + "solución no dada" + "\", " + "\"id\": \"" + id + "\"}";
				// Enviar los datos al servidor
				try (OutputStream os = conn.getOutputStream()) {
					byte[] input = jsonInputString.getBytes("utf-8");
					os.write(input, 0, input.length); // Escribe el JSON en el flujo de salida
				}
			}else{
				// JSON con la fórmula ingresada por el usuario
				String jsonInputString ="{\"nivel\": \""+level+ "\", "+ "\"problema\":\""+ this.getProblema()+ "\", "+"\"solución\": \"" + TextoQueIngresa.getText() + "\", " + "\"id\": \"" + id + "\"}";
				// Enviar los datos al servidor
				try (OutputStream os = conn.getOutputStream()) {
					byte[] input = jsonInputString.getBytes("utf-8");
					os.write(input, 0, input.length); // Escribe el JSON en el flujo de salida
				}
				

			}


			// Verifica si la respuesta es exitosa (200 OK)
			int responseCode = conn.getResponseCode();
			if (responseCode == HttpURLConnection.HTTP_OK) {
				// Lee la respuesta del servidor
				try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream(), "utf-8"))) {
					StringBuilder response = new StringBuilder();
					String responseLine;
					while ((responseLine = br.readLine()) != null) {
						response.append(responseLine.trim());
					}

					// Extrae el valor de "solución" de la respuesta JSON manualmente
					String jsonResponse = response.toString();

					String[] responsess = jsonResponse.replaceAll("[{]", "").replaceAll("[}]", "").split(",");
					
					

					String Comprobante = responsess[0];
					String solucion2 = responsess[1];

					
					// Actualiza el JTextPane con el resultado
					this.setSolucion(solucion2);
					this.setComprobante(Comprobante);

					if(this.getComprobante().equalsIgnoreCase("\"comprobante\": 1")){
						this.aumentarAciertos();
						TextoRespuesta.setText("<html> ¡Correcto! <html>");
					}


					if(TextoQueIngresa.getText().equalsIgnoreCase("")){
						if(this.getComprobante().equalsIgnoreCase("\"comprobante\": 0")){
							TextoRespuesta.setText("<html>"+ solucion2 +"<html>");
						}	
					}else{
						if(this.getComprobante().equalsIgnoreCase("\"comprobante\": 0")){
								TextoRespuesta.setText("<html> Incorrecto, "+ solucion2 +"<html>");
							}
					}


					if(this.getComprobante().equalsIgnoreCase("\"comprobante\": -1")){
						TextoRespuesta.setText("<html>"+ solucion2 +"<html>");
					}
					

					this.aumentarNoPreguntas();

					ContadorAciertos.setText(Integer.toString(this.getAciertos()));
					NumeroPreguntas.setText(Integer.toString(this.getNoPreguntas()));

					this.cargarProblemPorNivel(this.getNivel());
					TextoQueIngresa.setText("");

				}
			} else {
				this.setSolucion("Error en la conexión: " + responseCode); // Mensaje de error si la respuesta no es 200
			}
        } catch (Exception e) {
            e.printStackTrace();
        }

	}

	private void saltarRespuesta(int level, int id){
		

	}

    

	
	
	
	
	

}

