from flask import Flask, jsonify, request  # Importamos Flask y funciones auxiliares para gestionar el API
from CalcMasaMolar import calcular_masa_molar  # Importamos la función para calcular la masa molar
from Compuesto import Compuesto  # Opcional: si decides usar la clase Compuesto directamente
from Reaccion import Reaccion  
import chempy as ch

app = Flask(__name__)  # Creamos una instancia de Flask para configurar la aplicación

# Definimos el endpoint de la API
@app.route('/mi_api/masa_molar', methods=['POST'])
def masa_molar():
    # Obtenemos los datos de la solicitud en formato JSON
    data = request.json
    compuesto_input = data.get('formula')  # Extraemos la fórmula química desde el JSON
    
    if not compuesto_input:
        # Si no se proporciona la fórmula, retornamos un error 400 (solicitud incorrecta)
        return jsonify({'error': 'Fórmula del compuesto no proporcionada'}), 400

    try:
        # Calculamos la masa molar usando la función `calcular_masa_molar`
        mmolar = calcular_masa_molar(compuesto_input)
        
        # Retornamos el resultado en formato JSON
        return {
            'formula': compuesto_input,
            'masa_molar': mmolar
        }
    except ValueError as e:
        # Capturamos excepciones y devolvemos el error en formato JSON
        return jsonify({'error': str(e)}), 400
    
# endpoint de la API para el balanceo de ecuaciones
@app.route('/mi_api/balancear_reaccion', methods=['POST'])
def balancear_reaccion():
    # datos de la solicitud en formato JSON
    data = request.json
    reaccion_str = data.get('reaccion')  # Obtiene la reacción como string

    if not reaccion_str:
        return jsonify({'error': 'Reacción no proporcionada'}), 400

    #instancia de Reaccion con el string de la reacción
    try:
        reaccion = Reaccion(reaccion_str)
    except Exception as e:
        return jsonify({'error': 'Error al crear la reacción: ' + str(e)}), 400

    # Llama al método Balancear para balancear la reacción
    try:
        resultado_balanceo = reaccion.Balancear()
    except Exception as e:
        # Manejo de errores en caso de que falle el balanceo
        return jsonify({'error': 'Error al balancear la reacción: ' + str(e)}), 500

    return jsonify({
        'reaccion_original': reaccion_str,
        'reaccion_balanceada': resultado_balanceo
    })

if __name__ == '__main__':
    app.run(debug=True)
