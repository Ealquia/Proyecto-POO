# -*- coding: utf-8 -*-
from Compuesto import Compuesto
from Elemento import Elemento
def calcMasaMolar(comp_input):
    compuesto = Compuesto(compuesto_input)
	# Calcular la masa molar del compuesto
    masa_molar = compuesto.masaMolar()
    return masa_molar
