from flask import Flask, jsonify, request
from Compuesto import Compuesto

app = Flask(__name__)

# Endpoint para calcular la masa molar del compuesto
@app.route('/masa_molar', methods=['POST'])
def calcular_masa_molar():
    data = request.json  # Espera datos en formato JSON
    compuesto_input = data.get('formula')  # Obtiene la fórmula desde el JSON
    if not compuesto_input:
        return jsonify({'error': 'Fórmula del compuesto no proporcionada'}), 400

    try:
        # Crea el objeto Compuesto y calcula la masa molar
        compuesto = Compuesto(compuesto_input)
        masa_molar = compuesto.masaMolar()
        return jsonify({
            'formula': compuesto_input,
            'masa_molar': masa_molar
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

# Ruta de prueba para verificar que el servidor está en funcionamiento
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})

# Ejecuta el servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
