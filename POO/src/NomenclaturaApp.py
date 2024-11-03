from flask import Flask, jsonify, request
from Nomenclatura import Nivel, Problema, ComprobarRespuesta


NomenclaturaApp = Flask(__name__) 

@NomenclaturaApp.route("/api/ProblemaNivel1",  methods=["GET"])
def ProblemaNivel1():
    problema, id = Problema(Nivel(1))
    return jsonify({"nivel":1,"id": id, "problema": problema})


@NomenclaturaApp.route("/api/ProblemaNivel2", methods=["GET"])
def ProblemaNivel2():
    problema, id = Problema(Nivel(2))
    return jsonify({"nivel":2,"id": id, "problema": problema})

@NomenclaturaApp.route("/api/ProblemaNivel3",  methods=["GET"])
def ProblemaNivel3():
    problema, id = Problema(Nivel(3))
    return jsonify({"nivel":3,"id": id, "problema": problema})

@NomenclaturaApp.route("/api/ProblemaNivel4",  methods=["GET"])
def ProblemaNivel4():
    problema, id = Problema(Nivel(4))
    return jsonify({"nivel":4,"id": id, "problema": problema})

@NomenclaturaApp.route("/api/ProblemaTodos",   methods=["GET"])
def ProblemaTodos():
    problema, id =  Problema(Nivel(5))
    return jsonify({"nivel":5,"id": id, "problema": problema})






@NomenclaturaApp.route("/api/SolucionProblema", methods=[POST])
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

    try:
        solucion, comprobante = Nomenclatura.ComprobarRespuesta(solución, problema, id)
        return {"solución": solución,  "comprobante": comprobante}

    except  ValueError as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    NomenclaturaApp.run(debug=True)