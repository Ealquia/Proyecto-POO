from flask import Flask, jsonify, request
from Compuesto import Compuesto

def calcular_masa_molar(compuesto_input):
    try:
        # Crea el objeto Compuesto y calcula la masa molar
        comp = Compuesto(compuesto_input)
        masa_molar = comp.masaMolar()

        return str(masa_molar)
    except ValueError as e:
        return str(e)
