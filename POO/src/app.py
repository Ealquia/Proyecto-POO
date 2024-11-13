from flask import Flask, jsonify, request  # Importamos Flask y funciones auxiliares para gestionar el API
from CalcMasaMolar import calcular_masa_molar  # Importamos la función para calcular la masa molar
from Compuesto import Compuesto  # Opcional: si decides usar la clase Compuesto directamente
from Estequiometria.Conversiones import *
from Estequiometria.crearDato import *
from Estequiometria.problemaEsteq import *

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
@app.route('/mi_api/crear_dato', methods=['POST'])
def crear_dato():
    # datos de la solicitud en formato JSON
    dict = request.json
    
    if not dict:
        # Si no se proporciona la fórmula, retornamos un error 400 (solicitud incorrecta)
        return jsonify({'error': 'Fórmula del compuesto no proporcionada'}), 400

    try:
        #Creamos el dato
        dato = crearDato(dict).__str__()
        
        # Retornamos el resultado en formato JSON
        return jsonify(dato)
    
    except ValueError as e:
        # Capturamos excepciones y devolvemos el error en formato JSON
        return jsonify({'error': str(e)}), 400
    

# Ejecutamos la aplicación en modo de depuración para pruebas locales
if __name__ == '__main__':
    app.run(debug=True)
