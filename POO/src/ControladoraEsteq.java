import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.util.Map;
import javax.swing.JDialog;
import javax.swing.JLabel;

public class ControladoraEsteq {
    private String datos;
    private String incognitas;
    private String textoDatos;
    private String textoIncognitas;

    public ControladoraEsteq(){
        textoDatos = "DATOS: \r\n";
        textoIncognitas = "INCÓGNITAS: \r\n";
        datos = "[";
        incognitas = "[";
    }

    public void anadirDato(boolean Incognita, String Tipo, String reaccion, JLabel etiquetaDatos){
        //Crear la lista de compuestos
        String[] compuestos = this.listaCompuestos(reaccion);
        //Abrir el popUp
        try {
			PopNuevoDato dialog = new PopNuevoDato(Incognita,Tipo, compuestos, this, etiquetaDatos);
			dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
    }

    public String nuevoDato(Map<String,Object> DatoEntrante){
        String respuesta = infoDato(DatoEntrante);

        // Crear el JSON de manera manual y guardarlo en el atributo datosServidor
        {
        StringBuilder json = new StringBuilder();
        json.append("{");

        // Recorrer el mapa y construir el JSON
        boolean primero = true;
        for (Map.Entry<String, Object> entry : DatoEntrante.entrySet()) {
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

        json.append("},");

        // Convertir el StringBuilder en un String (JSON final) y actualizar los atributos
        if (!DatoEntrante.get("Incognita").equals("Si")) 
            datos = datos + json.toString();
        else incognitas = incognitas + json.toString();
        }

        //Devolver el texto para las labels actualizado
        if (DatoEntrante.get("Incognita").equals("Si")) {
            textoDatos = textoDatos + respuesta + "\n"; 
            return textoDatos;}
        else {
            textoIncognitas = textoIncognitas + respuesta + "\n";
            return textoIncognitas;}
    }

    public String infoDato(Map<String,Object> Dato){
        String dimensional = (String) Dato.get("Dimensionales");
        String magnitud =  Dato.get("Magnitud") != null ? (String) Dato.get("Magnitud") : "Incognita";
        String compuesto = (String) Dato.get("Compuesto");
        String info = magnitud + " " + dimensional + " de " + compuesto;

        if (Dato.get("Tipo").equals("Volumen de solución")) 
            info = info + " " + (String) Dato.get("Molaridad") + " Molar ";
        if (Dato.get("Tipo").equals("Molaridad")) 
            info = "Molaridad de una solución de " + info;
        if (Dato.get("Tipo").equals("Volumen de líquido")) 
            info = (Dato.get("Densidad") != null) ? info + ", Densidad: " + (String) Dato.get("Densidad") + " " + (String) Dato.get("DimDensidad") : info;
        if (Dato.get("Tipo").equals("Volumen de gas")||Dato.get("Tipo").equals("Presión de un gas")) {
            String temperatura = (Dato.get("Temperatura") != null)? (String) Dato.get("Temperatura") : "Incognita";
            String presion = (Dato.get("Presion") != null)? (String) Dato.get("Presion") : "Incognita";
            info = info + ", a " + temperatura + " " + Dato.get("DimTemp") + " y " + presion + Dato.get("DimPresion");
        }
        return info;
    }

    public String elMeroJson(String reaccion, String Porcentaje){
        StringBuilder json = new StringBuilder(datos);
        json.deleteCharAt(json.length() - 1); json.append("]");
        datos = json.toString();
        json = new StringBuilder(incognitas);
        json.deleteCharAt(json.length() - 1); json.append("]");
        incognitas = json.toString();
        String elMeroJson = String.format("{\"Reaccion\":\"%s\",\"Porcentaje\":\"%s\",\"Datos\":%s,\"Incognitas\":%s}",
                                  reaccion, Porcentaje, datos, incognitas);
        System.out.println(elMeroJson);
        return elMeroJson;
    }

    public String resolverProblema(String reaccion, String Porcentaje){
        String respuesta = "";
        String elMeroJson = elMeroJson(reaccion, Porcentaje);
        //Conectarse con el servidor
        URI uri = URI.create("http://127.0.0.1:5000/mi_api/resolver_Problema"); // URI del endpoint de la API
        try {
            URL url = uri.toURL();
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST"); // Configura el método HTTP como POST
            conn.setRequestProperty("Content-Type", "application/json; utf-8"); // Formato de datos de entrada
            conn.setRequestProperty("Accept", "application/json"); // Formato de datos de salida esperado
            conn.setDoOutput(true); // Permite enviar datos en el cuerpo de la solicitud

            // Enviar los datos al servidor
            try (OutputStream os = conn.getOutputStream()) {
                byte[] input = elMeroJson.getBytes("utf-8");
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
                    respuesta = response.toString();

                }
            } else {
                System.out.print("Error en la conexión: " + responseCode); // Mensaje de error si la respuesta no es 200
            }
            conn.disconnect();
        } catch (Exception e1) {
            e1.printStackTrace();
            System.out.print("Error: " + e1.getMessage()); // Muestra el mensaje de error en la interfaz
        }
        return respuesta;
    }

    public String[] listaCompuestos(String reaccion){
        String[] arrayCompuestos = new String[]{};
        //Conectarse con el servidor
        URI uri = URI.create("http://127.0.0.1:5000/mi_api/lista_Compuestos"); // URI del endpoint de la API
        try {
            URL url = uri.toURL();
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST"); // Configura el método HTTP como POST
            conn.setRequestProperty("Content-Type", "application/json; utf-8"); // Formato de datos de entrada
            conn.setRequestProperty("Accept", "application/json"); // Formato de datos de salida esperado
            conn.setDoOutput(true); // Permite enviar datos en el cuerpo de la solicitud

            String jsonInputString = "{\"Reaccion\": \"" + reaccion + "\"}";

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
                    String jsonResponse  = response.toString();
                    jsonResponse = jsonResponse.substring(2, jsonResponse.length() - 2);
                    arrayCompuestos = jsonResponse.split("\",\"");
                }
            } else {
                System.out.print("Error en la conexión: " + responseCode); // Mensaje de error si la respuesta no es 200
            }
            conn.disconnect();
        } catch (Exception e1) {
            e1.printStackTrace();
            System.out.print("Error: " + e1.getMessage()); // Muestra el mensaje de error en la interfaz
        }
        return arrayCompuestos;
    }

    public String getDatos() {
        return datos;
    }

    public void setDatos(String datos) {
        this.datos = datos;
    }

    public String getIncognitas() {
        return incognitas;
    }

    public void setIncognitas(String incognitas) {
        this.incognitas = incognitas;
    }

    public String getTextoDatos() {
        return textoDatos;
    }

    public void setTextoDatos(String textoDatos) {
        this.textoDatos = textoDatos;
    }

    public String getTextoIncognitas() {
        return textoIncognitas;
    }

    public void setTextoIncognitas(String textoIncognitas) {
        this.textoIncognitas = textoIncognitas;
    }
}


