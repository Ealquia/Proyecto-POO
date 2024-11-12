from Estequiometria import Gas
from Estequiometria.Liquido import Liquido
from Estequiometria.Masa import Masa
from Estequiometria.Solucion import Solucion


tipos = ["Masa", "Volumen de solución", "Volumen de líquido","Volumen de gas","Molaridad","Presión de un gas",
             "Temperatura de un gas","Calor de la reacción", "Entalpía de la reacción", "Entalpía molar", 
             "Cantidad de materia", "Porcentaje de rendimiento"]
tiposDatos = ["Masa", "Volumen de solución", "Volumen de líquido","Volumen de gas","Cantidad de materia", "Calor de una reacción"]

def crearDato(info: dict):
    tipoDato = info["Tipo"]
    if not(tipoDato=="Calor de la reacción") and not(tipoDato=="Entalpía de la reacción"):
        compuesto =info["Compuesto"]
    dimensionales=info["Dimensionales"]
    magnitud=info["Magnitud"]
    if tipoDato=="Masa":
        dato = Masa(compuesto=compuesto,dimensional=dimensionales,magnitud=magnitud)
    if tipoDato=="Volumen de líquido":
        dato = Liquido(compuesto=compuesto,dimMagnitud=dimensionales,dimDensidad=info["DimDensidad"],magnitud=magnitud,densidad=info["Densidad"])
    if tipoDato=="Volumen de solución":
        dato = Solucion(compuesto=compuesto,dimensional=dimensionales,magnitud=magnitud,molaridad=info["Molaridad"])
    if tipoDato=="Volumen de gas":
        dato = Gas(compuesto=compuesto,magnitud=magnitud,dimVolumen=dimensionales,dimPresion=info["DimPresion"],
                   presion=info["Presion"],dimTemperatura=info["DimTemp"],temperatura=info["Temperatura"])
    return dato
