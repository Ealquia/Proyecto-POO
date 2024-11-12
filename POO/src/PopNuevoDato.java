import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.io.BufferedReader; // Para leer datos de la respuesta del servidor
import java.io.InputStreamReader; // Para leer la entrada del servidor como un flujo de caracteres
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URI; // Para enviar datos al servidor
import java.net.URL; // Para establecer una conexión HTTP con el servidor
import java.util.ArrayList; // Para manejar URIs de manera segura
import java.util.Collections; // Para representar y manipular direcciones URL
import java.util.HashMap;
import java.util.Map;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JComboBox; // Para leer datos de la respuesta del servidor
import javax.swing.JDialog; // Para leer la entrada del servidor como un flujo de caracteres
import javax.swing.JLabel; // Para enviar datos al servidor
import javax.swing.JPanel; // Para establecer una conexión HTTP con el servidor
import javax.swing.JTextField; // Para manejar URIs de manera segura
import javax.swing.border.EmptyBorder;

public class PopNuevoDato extends JDialog implements ItemListener{

	private static final long serialVersionUID = 1L;
	private final JPanel contentPanel = new JPanel();
	private JLabel LabelTipoDato;
	private JLabel LabelCompuesto;
	private JComboBox DropCompuesto;
	private JTextField TxtMagnitud;
	private JComboBox DropDimMag;
	private JLabel LabelExtra1;
	private JTextField TxtExtra1;
	private JComboBox DropDimExtra1;
	private JTextField TxtExtra2;
	private JComboBox DropDimExtra2;
	private JCheckBox CheckExtra;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		try {
			PopNuevoDato dialog = new PopNuevoDato(false,"Cantidad de materia", new String[]{"H2O", "O2", "H2"});
			dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Create the dialog.
	 */
	@SuppressWarnings({ "rawtypes", "unchecked" })
	public PopNuevoDato(boolean Incognita, String Tipo, String[] compuestos) {
		if (Incognita)
			setTitle("Nueva Incógnita");
		else 
			setTitle("Nuevo Dato");
		//Config general del dialog
		setBounds(100, 100, 403, 333);
		BorderLayout borderLayout = new BorderLayout();
		borderLayout.setVgap(3);
		borderLayout.setHgap(3);
		getContentPane().setLayout(borderLayout);
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		GridBagLayout gbl_contentPanel = new GridBagLayout();
		gbl_contentPanel.columnWidths = new int[]{68, 0, 0, 0, 0};
		gbl_contentPanel.rowHeights = new int[]{17, 0, 0, 0, 0, 0, 0, 0, 0};
		gbl_contentPanel.columnWeights = new double[]{1.0, 1.0, 1.0, 1.0, Double.MIN_VALUE};
		gbl_contentPanel.rowWeights = new double[]{0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, Double.MIN_VALUE};
		contentPanel.setLayout(gbl_contentPanel);

		//Label con el Tipo  de dato o incógnita
		{
			LabelTipoDato = new JLabel(Tipo);
			LabelTipoDato.setFont(new Font("Tw Cen MT", Font.BOLD, 20));
			LabelTipoDato.setBackground(new Color(240, 240, 240));
		}
		GridBagConstraints gbc_labelTipoDato = new GridBagConstraints();
		gbc_labelTipoDato.gridwidth = 2;
		gbc_labelTipoDato.insets = new Insets(0, 0, 5, 5);
		gbc_labelTipoDato.fill = GridBagConstraints.BOTH;
		gbc_labelTipoDato.gridx = 1;
		gbc_labelTipoDato.gridy = 0;
		contentPanel.add(LabelTipoDato, gbc_labelTipoDato);
		//Label del compuesto
		{
			this.LabelCompuesto = new JLabel("Compuesto:");
			LabelCompuesto.setFont(new Font("Tw Cen MT", Font.BOLD, 20));
			GridBagConstraints gbc_LabelCompuesto = new GridBagConstraints();
			gbc_LabelCompuesto.anchor = GridBagConstraints.WEST;
			gbc_LabelCompuesto.insets = new Insets(0, 0, 5, 5);
			gbc_LabelCompuesto.gridx = 0;
			gbc_LabelCompuesto.gridy = 1;
			contentPanel.add(LabelCompuesto, gbc_LabelCompuesto);
			//Si el dato o incógnita es de tipo calor, hacer invisible
			if (Tipo.equals("Calor de la reacción") || Tipo.equals("Entalpía de la reacción")){
				this.LabelCompuesto.setVisible(false);
			}
		}
		//Dropbox de compuesto
		{
			this.DropCompuesto = new JComboBox(compuestos);
			this.DropCompuesto.setSelectedIndex(-1);
			DropCompuesto.setFont(new Font("Tw Cen MT", Font.PLAIN, 18));
			GridBagConstraints gbc_DropCompuesto = new GridBagConstraints();
			gbc_DropCompuesto.gridwidth = 2;
			gbc_DropCompuesto.insets = new Insets(0, 0, 5, 5);
			gbc_DropCompuesto.fill = GridBagConstraints.HORIZONTAL;
			gbc_DropCompuesto.gridx = 1;
			gbc_DropCompuesto.gridy = 1;
			contentPanel.add(DropCompuesto, gbc_DropCompuesto);
			//Si el dato o incógnita es de tipo calor o entalpía reacción, hacer invisible
			if (Tipo.equals("Calor de la reacción") || Tipo.equals("Entalpía de la reacción")){
				this.DropCompuesto.setVisible(false);
			}
		}
		//Label de Magnitud
		{
			String Magnitud = null;
			if (Tipo.equals("Masa")) Magnitud = "Masa: ";
			if (Tipo.equals("Cantidad de materia")) Magnitud = "Magnitud: ";
			ArrayList<String> Volumen = new ArrayList<>();
			Collections.addAll(Volumen,  "Volumen de solución", "Molaridad", "Volumen de líquido", "Densidad", "Volumen de gas", "Presión de un gas", "Temperatura de un gas");
			if (Volumen.contains(Tipo)) Magnitud = "Volumen:";
			if (Tipo.equals("Calor de la reacción")||Tipo.equals("Entalpía de la reacción")||Tipo.equals("Entalpía molar"))  Magnitud = "Calor: "; 

			JLabel LabelMagnitud = new JLabel(Magnitud);
			LabelMagnitud.setFont(new Font("Tw Cen MT", Font.BOLD, 20));
			GridBagConstraints gbc_LabelMagnitud = new GridBagConstraints();
			gbc_LabelMagnitud.anchor = GridBagConstraints.WEST;
			gbc_LabelMagnitud.insets = new Insets(0, 0, 5, 5);
			gbc_LabelMagnitud.gridx = 0;
			gbc_LabelMagnitud.gridy = 2;
			contentPanel.add(LabelMagnitud, gbc_LabelMagnitud);
		}
		//TextField de Magnitud
		{
			TxtMagnitud = new JTextField();
			TxtMagnitud.setFont(new Font("Tw Cen MT", Font.PLAIN, 18));
			GridBagConstraints gbc_txtMagnitud = new GridBagConstraints();
			gbc_txtMagnitud.insets = new Insets(0, 0, 5, 5);
			gbc_txtMagnitud.fill = GridBagConstraints.HORIZONTAL;
			gbc_txtMagnitud.gridx = 1;
			gbc_txtMagnitud.gridy = 2;
			contentPanel.add(TxtMagnitud, gbc_txtMagnitud);
			TxtMagnitud.setColumns(10);
			//Si la magnitud es la incógnita, desactivar el text field
			ArrayList<String> IncognitasMagnitud = new ArrayList<>();
			Collections.addAll(IncognitasMagnitud, "Masa", "Volumen de solución", "Volumen de líquido","Volumen de gas", "Calor de la reacción", "Cantidad de materia");
			if (Incognita && IncognitasMagnitud.contains(Tipo)){
				TxtMagnitud.setText("INCÓGNITA");
				TxtMagnitud.setEditable(false);
			}
			
		}
		//ComboBox de dimensional Magnitud
		{
			String[] dimensionales = null;
			ArrayList<String> Volumen = new ArrayList<>();
			Collections.addAll(Volumen,  "Volumen de solución", "Volumen de líquido","Volumen de gas", "Molaridad","Presión de un gas",
             "Temperatura de un gas");
			if (Volumen.contains(Tipo)) dimensionales = new String[]{"L","mL","microL","m3","cm3", "pulg3","gal","ft3"};
			if (Tipo.equals("Masa")) dimensionales = new String[]{"g","kg","mg","microg","ton","lb", "oz"};
			if (Tipo.equals("Calor de la reacción")||Tipo.equals("Entalpia de la reacción")||Tipo.equals("Entalpia molar"))  dimensionales = new String[]{"J", "kJ", "cal", "kcal"};
			if (Tipo.equals("Cantidad de materia")) dimensionales = new String[]{"mol","umol","mmol","particulas"};
			DropDimMag = new JComboBox(dimensionales);
			DropDimMag.setFont(new Font("Tw Cen MT", Font.PLAIN, 18));
			GridBagConstraints gbc_DropDimMag = new GridBagConstraints();
			gbc_DropDimMag.insets = new Insets(0, 0, 5, 5);
			gbc_DropDimMag.fill = GridBagConstraints.HORIZONTAL;
			gbc_DropDimMag.gridx = 2;
			gbc_DropDimMag.gridy = 2;
			contentPanel.add(DropDimMag, gbc_DropDimMag);
		}
		//Label Extra 1
		{
		//Encontrar lo que debe decir el label
			String SubDato1 = null;
			//Si el tipo es volumen de solución o molaridad, molaridad
			if (Tipo.equals("Volumen de solución")||Tipo.equals("Molaridad")) SubDato1 = "Molaridad: "; 
			//Si el tipo es volumen de líquido o densidad, densidad
			if (Tipo.equals("Volumen de líquido")||Tipo.equals("Densidad")) SubDato1 = "Densidad: ";
			//Si el tipo es volumen, presión o temperatura de gas, presión 
			if (Tipo.equals("Volumen de gas")||Tipo.equals("Presión de un gas")||Tipo.equals("Temperatura de un gas")) SubDato1 = "Presión:  "; 
			//Si el tipo es calor, entalpía
			if (Tipo.equals("Calor de la reacción")||Tipo.equals("Entalpía de la reacción")||Tipo.equals("Entalpía molar"))  SubDato1 = "Entalpía: "; 
		//Crear el label siempre que el tipo no sea masa o cantidad de materia
		if (!Tipo.equals("Masa")||!Tipo.equals("Cantidad de materia")) {
			LabelExtra1 = new JLabel(SubDato1);
			LabelExtra1.setFont(new Font("Tw Cen MT", Font.BOLD, 20));
			GridBagConstraints gbc_LabelExtra1 = new GridBagConstraints();
			gbc_LabelExtra1.anchor = GridBagConstraints.WEST;
			gbc_LabelExtra1.insets = new Insets(0, 0, 5, 5);
			gbc_LabelExtra1.gridx = 0;
			gbc_LabelExtra1.gridy = 3;
			contentPanel.add(LabelExtra1, gbc_LabelExtra1); }
		}
		//Text Field Extra 1
		{
			//Crear el textfield si el tipo no es de masa o cantidad de materia
			if (!Tipo.equals("Masa")&&!Tipo.equals("Cantidad de materia")) {
				TxtExtra1 = new JTextField();
				TxtExtra1.setFont(new Font("Tw Cen MT", Font.PLAIN, 18));
				TxtExtra1.setColumns(10);
				GridBagConstraints gbc_txtExtra1 = new GridBagConstraints();
				gbc_txtExtra1.insets = new Insets(0, 0, 5, 5);
				gbc_txtExtra1.fill = GridBagConstraints.HORIZONTAL;
				gbc_txtExtra1.gridx = 1;
				gbc_txtExtra1.gridy = 3;
				contentPanel.add(TxtExtra1, gbc_txtExtra1);

				//Desactivarlo para las incógnitas
				ArrayList<String> Incognitas1 = new ArrayList<>();
				Collections.addAll(Incognitas1,"Molaridad", "Densidad", "Presión de un gas","Entalpía de la reacción", "Entalpía molar");
				if (Incognita && Incognitas1.contains(Tipo)){
					TxtExtra1.setText("INCÓGNITA");
					TxtExtra1.setEditable(false);
			} }
		}
		//ComboBox dimensionales 1
		{
			//Crear el combobox si el tipo no es de masa ni cantidad de materia 
			if (!Tipo.equals("Masa")&&!Tipo.equals("Cantidad de materia")) {
				String[] dimensionales = null;
				if (Tipo.equals("Volumen de solución")||Tipo.equals("Molaridad")) dimensionales = new String[]{"M"}; 
				if (Tipo.equals("Volumen de líquido")||Tipo.equals("Densidad")) dimensionales = new String[]{"g/mL","kg/gal","kg/m3","kg/L","g/L"};
				//Si el tipo es volumen, presión o temperatura de gas, presión 
				if (Tipo.equals("Volumen de gas")||Tipo.equals("Presión de un gas")||Tipo.equals("Temperatura de un gas")) dimensionales = new String[]{"Pa","kPa","mmHg","atm"}; 
				DropDimExtra1 = new JComboBox(dimensionales);
				DropDimExtra1.setFont(new Font("Tw Cen MT", Font.PLAIN, 18));
				GridBagConstraints gbc_DropDimExtra1 = new GridBagConstraints();
				gbc_DropDimExtra1.insets = new Insets(0, 0, 5, 5);
				gbc_DropDimExtra1.fill = GridBagConstraints.HORIZONTAL;
				gbc_DropDimExtra1.gridx = 2;
				gbc_DropDimExtra1.gridy = 3;
				contentPanel.add(DropDimExtra1, gbc_DropDimExtra1); }
		}
		//Label  Extra 2
		{
			//Si el tipo es relacionado a un gas, crear el label
			if (Tipo.equals("Volumen de gas")||Tipo.equals("Presión de un gas")||Tipo.equals("Temperatura de un gas")){ 
				JLabel LabelExtra2 =  new JLabel("Temperatura: ");
				LabelExtra2.setFont(new Font("Tw Cen MT", Font.BOLD, 20));
				GridBagConstraints gbc_LabelExtra2 = new GridBagConstraints();
				gbc_LabelExtra2.anchor = GridBagConstraints.WEST;
				gbc_LabelExtra2.insets = new Insets(0, 0, 5, 5);
				gbc_LabelExtra2.gridx = 0;
				gbc_LabelExtra2.gridy = 4;
				contentPanel.add(LabelExtra2, gbc_LabelExtra2); }
		}
		//TextFIeld extra 2
		{
			// Si el tipo es de un gas, crear el textfield
			if (Tipo.equals("Volumen de gas")||Tipo.equals("Presión de un gas")||Tipo.equals("Temperatura de un gas")){ 
				TxtExtra2 = new JTextField();
				TxtExtra2.setFont(new Font("Tw Cen MT", Font.PLAIN, 18));
				TxtExtra2.setColumns(10);
				GridBagConstraints gbc_txtExtra2 = new GridBagConstraints();
				gbc_txtExtra2.insets = new Insets(0, 0, 5, 5);
				gbc_txtExtra2.fill = GridBagConstraints.HORIZONTAL;
				gbc_txtExtra2.gridx = 1;
				gbc_txtExtra2.gridy = 4;
				contentPanel.add(TxtExtra2, gbc_txtExtra2); }
			//Si la incógnita  es temperatura, deshabilitar el campo
			if  (Tipo.equals("Temperatura de un gas")){
				TxtExtra2.setText("INCÓGNITA");
				TxtExtra2.setEditable(false);
			}
		}
		//DropBox dimensionales 2
		{
			if (Tipo.equals("Volumen de gas")||Tipo.equals("Presión de un gas")||Tipo.equals("Temperatura de un gas")){ 
				DropDimExtra2 = new JComboBox(new String[]{"K","C","F"});
				DropDimExtra2.setFont(new Font("Tw Cen MT", Font.PLAIN, 18));
				GridBagConstraints gbc_DropDimExtra2 = new GridBagConstraints();
				gbc_DropDimExtra2.insets = new Insets(0, 0, 5, 5);
				gbc_DropDimExtra2.fill = GridBagConstraints.HORIZONTAL;
				gbc_DropDimExtra2.gridx = 2;
				gbc_DropDimExtra2.gridy = 4;
				contentPanel.add(DropDimExtra2, gbc_DropDimExtra2); }
		}
		//Check Box extra
		{
			String Texto = null;
			if (Tipo.equals("Calor de la reacción"))
				Texto = "Entalpía Molar";
			if (Tipo.equals("Volumen de líquido"))
				Texto = "No me dan la densidad";
			if (Texto != null) {
				this.CheckExtra = new JCheckBox(Texto);
				CheckExtra.setEnabled(false);
				CheckExtra.setFont(new Font("Tw Cen MT", Font.PLAIN, 20));
				GridBagConstraints gbc_CheckExtra = new GridBagConstraints();
				gbc_CheckExtra.gridwidth = 2;
				gbc_CheckExtra.insets = new Insets(0, 0, 5, 5);
				gbc_CheckExtra.gridx = 1;
				gbc_CheckExtra.gridy = 5;
				contentPanel.add(CheckExtra, gbc_CheckExtra); 
				CheckExtra.setEnabled(true);
				CheckExtra.addItemListener(this);			
			}
		}
		//Check Box para dato real
		{
			if(!Incognita){
				JCheckBox CheckDatoReal = new JCheckBox("Dato real");
				CheckDatoReal.setFont(new Font("Tw Cen MT", Font.PLAIN, 20));
				GridBagConstraints gbc_CheckDatoReal = new GridBagConstraints();
				gbc_CheckDatoReal.insets = new Insets(0, 0, 0, 5);
				gbc_CheckDatoReal.gridx = 1;
				gbc_CheckDatoReal.gridy = 7;
				contentPanel.add(CheckDatoReal, gbc_CheckDatoReal);}
		}
		//Botoncito de ayuda
		{
			JButton btnNewButton = new JButton("?");
			btnNewButton.setFont(new Font("Tahoma", Font.BOLD, 15));
			GridBagConstraints gbc_btnNewButton = new GridBagConstraints();
			gbc_btnNewButton.insets = new Insets(0, 0, 0, 5);
			gbc_btnNewButton.gridx = 2;
			gbc_btnNewButton.gridy = 7;
			contentPanel.add(btnNewButton, gbc_btnNewButton); 
		}
		//Panel 
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				String TextoAceptar = (Incognita)? "Agregar Incógnita": "Agregar Dato";
				JButton AcceptButton = new JButton(TextoAceptar);
				AcceptButton.addActionListener(new ActionListener() {
					@Override
					public void actionPerformed(ActionEvent e) {
						URI uri = URI.create("http://127.0.0.1:5000/mi_api/crear_dato"); // URI del endpoint de la API
						try {
							URL url = uri.toURL();
							HttpURLConnection conn = (HttpURLConnection) url.openConnection();
							conn.setRequestMethod("POST"); // Configura el método HTTP como POST
							conn.setRequestProperty("Content-Type", "application/json; utf-8"); // Formato de datos de entrada
							conn.setRequestProperty("Accept", "application/json"); // Formato de datos de salida esperado
							conn.setDoOutput(true); // Permite enviar datos en el cuerpo de la solicitud

							// Crear un mapa para almacenar los datos
							Map<String, Object> datos = new HashMap<>();
							datos.put("Tipo", Tipo); datos.put("Compuesto", DropCompuesto.getSelectedItem());
							datos.put("Dimensionales", DropDimMag.getSelectedItem()); datos.put("Magnitud", TxtMagnitud.getText()); 
							if (Tipo.equals("Volumen de líquido")){datos.put("DimDensidad", DropDimExtra1.getSelectedItem()); datos.put("Densidad", TxtExtra1.getText());}
							if (Tipo.equals("Volumen de solución")){datos.put("Molaridad", TxtExtra1.getText());}
							if (Tipo.equals("Volumen de gas")){
								datos.put("DimPresion", DropDimExtra1.getSelectedItem()); 
								datos.put("Presion", TxtExtra1.getText());
								datos.put("DimTemp", DropDimExtra2.getSelectedItem()); 
								datos.put("Temperatura", TxtExtra2.getText());
							}

							// Crear el JSON de manera manual
							StringBuilder json = new StringBuilder();
							json.append("{");

							// Recorrer el mapa y construir el JSON
							boolean primero = true;
							for (Map.Entry<String, Object> entry : datos.entrySet()) {
								if (!primero) {
									json.append(", ");
								}
								json.append("\"").append(entry.getKey()).append("\": ");
								if (entry.getValue() instanceof String) {
									json.append("\"").append(entry.getValue()).append("\"");
								} else {
									json.append(entry.getValue());
								}
								primero = false;
							}

							json.append("}");

							// Convertir el StringBuilder en un String (JSON final)
							String jsonInputString = json.toString();
		
							// Enviar los datos al servidor
							try (OutputStream os = conn.getOutputStream()) {
								byte[] input = jsonInputString.getBytes("utf-8");
								os.write(input, 0, input.length); // Escribe el JSON en el flujo de salida
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
		
									// Extrae el valor de "masa_molar" de la respuesta JSON manualmente
									String jsonResponse = response.toString();
									System.out.println(jsonResponse);
								}
							} else {
								System.out.print("Error en la conexión: " + responseCode); // Mensaje de error si la respuesta no es 200
							}
							conn.disconnect();
						} catch (Exception e1) {
							e1.printStackTrace();
							System.out.print("Error: " + e1.getMessage()); // Muestra el mensaje de error en la interfaz
						}
						dispose();
					}
				});
				AcceptButton.setFont(new Font("Tw Cen MT", Font.PLAIN, 15));
				buttonPane.add(AcceptButton);
				getRootPane().setDefaultButton(AcceptButton);

			}
			{
				JButton cancelButton = new JButton("Cancelar");
				cancelButton.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						dispose();
					}
				});
				cancelButton.setFont(new Font("Tw Cen MT", Font.PLAIN, 15));
				cancelButton.setActionCommand("Cancel");
				buttonPane.add(cancelButton);
			}
		}
	}

	@Override
	public void itemStateChanged(ItemEvent e) {
		if (CheckExtra.isSelected() && CheckExtra.getText().equals("Entalpía Molar")) {
			this.LabelCompuesto.setVisible(true);
			this.DropCompuesto.setVisible(true); }
		if (!CheckExtra.isSelected() && CheckExtra.getText().equals("Entalpía Molar")){
			this.LabelCompuesto.setVisible(false);
			this.DropCompuesto.setVisible(false); }
		if (CheckExtra.isSelected() && CheckExtra.getText().equals("No me dan la densidad")) {
			this.LabelExtra1.setVisible(false);
			this.TxtExtra1.setVisible(false); 
			this.DropDimExtra1.setVisible(false); }
		if (!CheckExtra.isSelected() && CheckExtra.getText().equals("No me dan la densidad")){
			this.LabelExtra1.setVisible(true);
			this.TxtExtra1.setVisible(true); 
			this.DropDimExtra1.setVisible(true);}
		}
			
} 