from Estequiometria.Gas import Gas
from Estequiometria.Liquido import Liquido
from Estequiometria.Masa import Masa
from Estequiometria.Solucion import Solucion
from Estequiometria.Moles import Moles


tipos = ["Masa", "Volumen de solución", "Volumen de líquido","Volumen de gas","Molaridad","Presión de un gas",
             "Temperatura de un gas","Calor de la reacción", "Entalpía de la reacción", "Entalpía molar", 
             "Cantidad de materia", "Porcentaje de rendimiento"]
tiposDatos = ["Masa", "Volumen de solución", "Volumen de líquido","Volumen de gas","Cantidad de materia", "Calor de una reacción"]

def crearDato(info: dict):
    tipoDato = info["Tipo"]
    incognita = info["Incognita"]=="Si"
    if not(incognita): 
        teorico = info["Teorico"]=="Si" 
    magnitud=info.get("Magnitud")
    if not(tipoDato=="Calor de la reacción") and not(tipoDato=="Entalpía de la reacción"):
        compuesto =info["Compuesto"]
    dimensionales=info["Dimensionales"]
    #Crear las incógnitas
    if (incognita):
        if tipoDato=="Masa":
            dato = Masa(compuesto=compuesto,dimensional=dimensionales)
        if tipoDato=="Volumen de líquido":
            dato = Liquido(compuesto=compuesto,dimMagnitud=dimensionales,dimDensidad=info["DimDensidad"],
                        densidad=info["Densidad"])
        if tipoDato =="Molaridad":
            dato = Solucion(compuesto=compuesto,magnitud=magnitud,dimMagnitud=dimensionales)
        if tipoDato=="Volumen de solución":
            dato = Solucion(compuesto=compuesto,dimensional=dimensionales,molaridad=info["Molaridad"])
        if tipoDato=="Volumen de gas":
            dato = Gas(compuesto=compuesto,dimVolumen=dimensionales,dimPresion=info["DimPresion"],
                    presion=info["Presion"],dimTemperatura=info["DimTemp"],temperatura=info["Temperatura"])
        if tipoDato=="Presion de un gas":
            dato = Gas(compuesto=compuesto,magnitud=magnitud,dimVolumen=dimensionales,dimPresion=info["DimPresion"],
                       dimTemperatura=info["DimTemp"], temperatura=info["Temperatura"])
        if tipoDato=="Temperatura de un gas":
            dato = Gas(compuesto=compuesto,magnitud=magnitud,dimVolumen=dimensionales,presion=info["Presion"],dimPresion=info["DimPresion"],
                       dimTemperatura=info["DimTemp"])
        if tipoDato=="Cantidad de materia":
            dato = Moles(compuesto=compuesto,dimensional=dimensionales)
    #Crear datos
    else:
        if tipoDato=="Masa":
            dato = Masa(compuesto=compuesto,dimensional=dimensionales,magnitud=magnitud,teorico=teorico)
        if tipoDato=="Volumen de líquido":
            dato = Liquido(compuesto=compuesto,dimMagnitud=dimensionales,dimDensidad=info.get("DimDensidad"),
                        densidad=info.get("Densidad"),magnitud=magnitud,teorico=teorico)
        if tipoDato=="Volumen de solución":
            dato = Solucion(compuesto=compuesto,dimensional=dimensionales,molaridad=info["Molaridad"],
                        magnitud=magnitud,teorico=teorico)
        if tipoDato=="Volumen de gas":
            dato = Gas(compuesto=compuesto,dimVolumen=dimensionales, 
                    presion=info["Presion"],dimTemperatura=info["DimTemp"],temperatura=info["Temperatura"],
                    dimPresion=info["DimPresion"],magnitud=magnitud,teorico=teorico)
        if tipoDato=="Cantidad de materia":
            dato = Moles(compuesto=compuesto,dimensional=dimensionales,magnitud=magnitud,teorico=teorico)
    return dato
