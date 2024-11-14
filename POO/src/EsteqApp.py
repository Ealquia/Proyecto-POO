from flask import Flask, jsonify, request  # Importamos Flask y funciones auxiliares para gestionar el API
from Estequiometria.Conversiones import *
from Estequiometria.crearDato import *
from Estequiometria.problemaEsteq import *

app = Flask(__name__)

# endpoint de la API para el balanceo de ecuaciones
@app.route('/mi_api/resolver_Problema', methods=['POST'])
def resolver_Problema():
    respuesta = ""
    losDatos = []
    # datos de la solicitud en formato JSON
    todo = request.get_json(force=True)
    
    if not todo:
        # Si no se proporcionan datos, retornamos un error 400 (solicitud incorrecta)
        return jsonify({'error': 'No se proporcionaron datos'}), 400

    try:
        #Creamos los datos
        for d in todo["Datos"]:
            losDatos.append(crearDato(d)),
        
        #Creamos los problemas por cada incógnita
        for i in todo["Incognitas"]:
            #Creamos la incógnita
            incognita = crearDato(i)
            #Creamos el problema
            tipo = i["Tipo"]
            porcentaje = float(todo["Porcentaje"])
            problema = problemaEsteq(Datos=losDatos,Incognita=incognita,reaccion=todo["Reaccion"],tipo=tipo,Rendimiento=porcentaje)
            respuesta = respuesta + problema.Respuesta() + "|"
        
        # Retornamos el resultado en formato JSON
        return jsonify(respuesta)
    
    except ValueError as e:
        # Capturamos excepciones y devolvemos el error en formato JSON
        return jsonify({'error': str(e)}), 400
    
@app.route('/mi_api/lista_Compuestos', methods=['POST'])
def lista_Compuestos():
    # datos de la solicitud en formato JSON
    reaccion = request.get_json(force=True).get("Reaccion")
    
    if not reaccion:
        # Si no se proporcionan datos, retornamos un error 400 (solicitud incorrecta)
        return jsonify({'error': 'No se proporcionó una reacción o un compuesto'}), 400

    try:
        R = Reaccion(reaccion) if "=" in reaccion else reaccion
        lista_Compuestos = R.ObtenerReactivosString() + R.ObtenerProductosString() if "=" in reaccion else [reaccion]
        
        # Retornamos el resultado en formato JSON
        return jsonify(lista_Compuestos)
    
    except ValueError as e:
        # Capturamos excepciones y devolvemos el error en formato JSON
        return jsonify({'error': str(e)}), 400
    
    
# Ejecutamos la aplicación en modo de depuración para pruebas locales
if __name__ == '__main__':
    app.run(debug=True)