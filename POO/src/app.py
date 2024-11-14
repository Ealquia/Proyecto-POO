from flask import Flask, jsonify, request  # Importamos Flask y funciones auxiliares para gestionar el API
from CalcMasaMolar import calcular_masa_molar  # Importamos la función para calcular la masa molar
from Compuesto import Compuesto  # Opcional: si decides usar la clase Compuesto directamente
from Reaccion import Reaccion  
import chempy as ch
from FuncionesNomenclatur import *
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

@app.route("/api/ProblemaNivel1",  methods=["GET"])
def ProblemaNivel1():
    problema, id = Problema(1)
    return jsonify({"nivel":1,"id": id, "problema": problema})


@app.route("/api/ProblemaNivel2", methods=["GET"])
def ProblemaNivel2():
    problema, id = Problema(2)
    return jsonify({"nivel":2,"id": id, "problema": problema})

@app.route("/api/ProblemaNivel3",  methods=["GET"])
def ProblemaNivel3():
    problema, id = Problema(3)
    return jsonify({"nivel":3,"id": id, "problema": problema})

@app.route("/api/ProblemaNivel4",  methods=["GET"])
def ProblemaNivel4():
    problema, id = Problema(4)
    return jsonify({"nivel":4,"id": id, "problema": problema})

@app.route("/api/ProblemaNivel5",   methods=["GET"])
def ProblemaTodos():
    problema, id =  Problema(5)
    return jsonify({"nivel":5,"id": id, "problema": problema})

@app.route("/api/SolucionProblema", methods=["POST"])
def IonesSolucionProblema():
    data = request.json
    nivel = data.get("nivel")
    problema = data.get("problema")
    solución = data.get("solución")
    id = data.get("id")

    if not solución:
        return jsonify({"error": "Solución no proporcionada"})

    if not  problema:
        return jsonify({"error": "Problema no proporcionado"})

    if not  id:
        return jsonify({"error": "Id no proporcionado"})

    if (solución != "solución no dada"):
        try:
            solucion, comprobante = ComprobarRespuesta(int(nivel), solución, problema, id)
            return jsonify({"solucion": "Incorrecto; "+str(solucion), "comprobante": int(comprobante)})

        except  ValueError as e:
            return jsonify({"error": str(e)})
    else:
        try:
            solucion, comprobante = ComprobarRespuesta(int(nivel), solución, problema, id)
            return jsonify({"solucion": str(solucion), "comprobante": int(comprobante)})

        except  ValueError as e:
            return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
