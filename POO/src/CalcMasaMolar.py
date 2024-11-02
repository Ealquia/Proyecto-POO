from flask import Flask, jsonify, request #Importamos módulos de flask
from Compuesto import Compuesto  # Importamos la clase que calcula la masa molar de un compuesto

def calcular_masa_molar(compuesto_input):
    try:
        # Creamos un objeto Compuesto con la fórmula dada y obtenemos la masa molar
        comp = Compuesto(compuesto_input)
        masa_molar = comp.masaMolar()

        # Convertimos la masa molar a string para facilitar su manipulación en la API
        return str(masa_molar)
    except ValueError as e:
        # En caso de error, devolvemos la descripción del mismo
        return str(e)
