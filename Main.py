def menu(opciones, texto_Menu):
    #opcion = variable que devuelve la función
    #opciones = lista de opciones
    #texto_Menu = texto del input
    opcion = 0
    i = 0
    for x in opciones:
        i = i + 1
        print(i,".",x)
    while opcion<1 or opcion>len(opciones):
        try: 
            opcion = int(input(texto_Menu))
            if opcion<1 or opcion>len(opciones):
                print("Por favor ingrese una opción válida")
        except:
            print("Por favor ingrese un número entero")
    return opcion

def menuString(opciones, texto_Menu):
    #opcion = variable que devuelve la función
    #opciones = lista de opciones
    #texto_Menu = texto del input
    opcion = 0
    i = 0
    for x in opciones:
        i = i + 1
        print(i,".",x)
    while opcion<1 or opcion>len(opciones):
        try: 
            opcion = int(input(texto_Menu))
            if opcion<1 or opcion>len(opciones):
                print("Por favor ingrese una opción válida")
        except:
            print("Por favor ingrese un número entero")
    return opciones[opcion-1]

from Estequiometria.Masa import Masa
from Estequiometria.Solucion import  Solucion
from Estequiometria.Liquido import Liquido
from Estequiometria.Gas import Gas
from Estequiometria.problemaEsteq import problemaEsteq


def datoEstequiometria(reaccion):
    print("¿Qué te dan en el problema? ")
    tipoDato = menu(["Masa","Volumen Líquido","Volumen Solución","Volumen de Gas"],"Ingrese el número correspondiente: ")
    print("¿De qué compuesto?")
    compuesto = menuString(reaccion.ObtenerReactivosString()+reaccion.ObtenerProductosString(),"Ingrese el número del compuesto: ")
    C = Conversiones()
    if tipoDato==1:
        dimensionales = menuString(C.listaDimensionales("Masa"),"Ingrese  el número de la unidad correspondiente: ")
        magnitud = float(input("Ingrese la magnitud de la masa: "))
        dato = Masa(compuesto=compuesto,dimensional=dimensionales,magnitud=magnitud)
    if tipoDato==2:
        print("Dimensionales del volumen:")
        dimensionales = menuString(C.listaDimensionales("Volumen"),"Ingrese  el número de la unidad correspondiente: ")
        magnitud = float(input("Ingrese la magnitud del volumen del líquido: "))
        print("Dimensionales de la densidad:")
        dimDensidad = menuString(C.listaDimensionales("Densidad"),"Ingrese  el número de la unidad correspondiente: ")
        densidad = float(input("Ingresela densidad del compuesto (si no la conoce,  ingrese 0): "))
        if densidad==0: densidad = None
        dato = Liquido(compuesto=compuesto,dimMagnitud=dimensionales,dimDensidad=dimDensidad,magnitud=magnitud,densidad=densidad)
    if tipoDato==3:
        print("Dimensionales del volumen:")
        dimensionales = menuString(C.listaDimensionales("Volumen"),"Ingrese  el número de la unidad correspondiente: ")
        magnitud = float(input("Ingrese la magnitud del volumen de la solución: "))
        molaridad = float(input("Ingrese la molaridad de la solución (M): "))
        dato = Solucion(compuesto=compuesto,dimensional=dimensionales,magnitud=magnitud,molaridad=molaridad)
    if tipoDato==4:
        print("Dimensionales del volumen:")
        dimensionales = menuString(C.listaDimensionales("Volumen"),"Ingrese  el número de la unidad correspondiente: ")
        magnitud = float(input("Ingrese la magnitud del volumen del gas: "))
        print("Dimensionales de la presión:")
        dimPresion =  menuString(C.listaDimensionales("Presion"),"Ingrese  el número de la unidad correspondiente: ")
        presion = float(input("Ingrese la magnitud de la presión: "))
        print("Dimensionales de la temperatura")
        dimTemp =  menuString(C.listaDimensionales("Temperatura"),"Ingrese  el número de la unidad correspondiente: ")
        temp = float(input("Ingrese la magnitud de la temperatura: "))
        dato = Gas(compuesto=compuesto,magnitud=magnitud,dimVolumen=dimensionales,dimPresion=dimPresion,
                   presion=presion,dimTemperatura=dimTemp,temperatura=temp)
    return dato

import pandas as pd
def incognitaEstequiometria(reaccion):
    tipoDato = menu(["Masa","Volumen Líquido","Volumen Solución","Volumen de Gas","Densidad de un líquido","Molaridad de una solución", "Presión de un gas", "Temperatura de un gas"],
                    "¿Qué desea encontrar? Ingrese el número correspondiente: ")
    print("¿De qué compuesto?")
    compuesto = menuString(reaccion.ObtenerReactivosString()+reaccion.ObtenerProductosString(),"Ingrese el número del compuesto: ")
    C = Conversiones()
    if tipoDato==1:
        dimensionales = menuString(C.listaDimensionales("Masa"),"Ingrese  el número de la unidad correspondiente: ")
        incognita = Masa(dimensional=dimensionales, compuesto=compuesto)
    if tipoDato==2 or  tipoDato==5:
        magnitud, densidad = None, None
        print("Dimensionales del volumen:")
        dimensionales = menuString(C.listaDimensionales("Volumen"),"Ingrese  el número de la unidad correspondiente: ")
        if  tipoDato!=2:
            magnitud = float(input("Ingrese la magnitud del volumen del líquido: "))
        print("Dimensionales de la densidad:")
        dimDensidad = menuString(C.listaDimensionales("Densidad"),"Ingrese  el número de la unidad correspondiente: ")
        if  tipoDato!=3:
            densidad = float(input("Ingresela densidad del compuesto (si no la conoce,  ingrese 0): "))
            if densidad==0: densidad = None
        incognita = Liquido(compuesto=compuesto,dimMagnitud=dimensionales,dimDensidad=dimDensidad,magnitud=magnitud,densidad=densidad)
    if tipoDato==3 or tipoDato==6:
        magnitud, molaridad = None, None
        print("Dimensionales del volumen:")
        dimensionales = menuString(C.listaDimensionales("Volumen"),"Ingrese  el número de la unidad correspondiente: ")
        if tipoDato!=3:
            magnitud = float(input("Ingrese la magnitud del volumen de la solución: "))
        if tipoDato != 6:
            molaridad = float(input("Ingrese la molaridad de la solución (M): "))
        incognita = Solucion(compuesto=compuesto,dimensional=dimensionales,magnitud=magnitud,molaridad=molaridad)
    if tipoDato==4 or tipoDato==7 or tipoDato==8:
        magnitud, presion, temp = None, None, None
        print("Dimensionales del volumen:")
        dimensionales = menuString(C.listaDimensionales("Volumen"),"Ingrese  el número de la unidad correspondiente: ")
        if  tipoDato!=4:
            magnitud = float(input("Ingrese la magnitud del volumen del gas: "))
        print("Dimensionales de la presión:")
        dimPresion =  menuString(C.listaDimensionales("Presion"),"Ingrese  el número de la unidad correspondiente: ")
        if tipoDato != 7:
            presion = float(input("Ingrese la magnitud de la presión: "))
        print("Dimensionales de la temperatura")
        dimTemp =  menuString(C.listaDimensionales("Temperatura"),"Ingrese  el número de la unidad correspondiente: ")
        if  tipoDato != 8:
            temp = float(input("Ingrese la magnitud de la temperatura: "))
        incognita = Gas(compuesto=compuesto,magnitud=magnitud,dimVolumen=dimensionales,dimPresion=dimPresion,
                   presion=presion,dimTemperatura=dimTemp,temperatura=temp)
    return incognita, tipoDato

from Compuesto import Compuesto
from Reaccion import Reaccion
from Estequiometria.Conversiones import Conversiones
from Nomenclatura.Nomenclatura import Nomenclatura

#Main
print("Gracias por ser un beta tester de nuestra app de química! ¿Qué función deseas usar?")
continuar = True
while(continuar):
    opcion = menu(["Masa Molar", "Balanceo", "Estequiometría", "Nomenclatura", "Salir"],"Ingrese el número de la opción correspondiente: ")
    if opcion==1: #Calculadora de masa molar
        print("Calculadora de masa molar")
        print("Ingrese la fórmula del compuesto. ")
        formula = input()  #input de la fórmula
        compuesto  = Compuesto(formula) #Creación del objeto
        print("La masa molar del compuesto es: " + str(compuesto.masaMolar()) +  " g/mol")

    if opcion==2:  #Balanceo de ecuaciones
        print("Balanceo de ecuaciones")
        print("Ingresa la ecuación separada por un signo = ")
        strReaccion = input()  #input de la fórmula
        reaccion  = Reaccion(strReaccion) #Creación del objeto
        print("La reacción balanceada es: " + reaccion.Balancear())

    if opcion==3:  #Estequiometría
        print("Qué tipo de problema desea resolver?")
        problema = menu(["Estequiometría simple", "Reactivo limitanete"],"Ingresa el número de la opción correspondiente: ")
        if problema == 1:
            print("Escribe la reacción química sin balancear separada por un signo = ")
            strReaccion = input()  #input de la fórmula
            reaccion  = Reaccion(strReaccion) #Creación del objeto
            print("Escribe la reacción química sin balancear separada por un signo = ")
        strReaccion = input()  #input de la fórmula
        reaccion  = Reaccion(strReaccion) #Creación del objeto
        if problema==1:
            print("Ingrese el dato de partida: ")
            dato = datoEstequiometria(reaccion)
            print(dato)
            print("Ingrese la incógnita: ")
            incognita, tipoIncognita = incognitaEstequiometria(reaccion)
            problema = problemaEsteq(Datos=[dato],Incognita=incognita,reaccion=reaccion)
            respuestaNum, respuestaDato = problema.deCosaACosa()
            if  tipoIncognita<=4:
                print("La respuesta es ", respuestaDato)
            else:
                print("La respuesta es ", respuestaNum)
            

    if opcion == 4: #  Nomenclatura
        nomenclatura = Nomenclatura()
        print("¿Qué nivel desea prácticar?")
        menu1 = ["Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4", "Todos los niveles"]
        opcion1 = menu(menu1,"Ingrese el número de la opción correspondiente: ")
        iones = nomenclatura.Nivel(opcion1) #csv de iones que se usará
        print(iones.head())
        cantidadAciertos = 0
        try:
            cantidad = int(input("Ingrese la cantidad de iones que quiere repasar: "))
            for  i in range(cantidad):
                pregunta, id= nomenclatura.Problema(iones) #pregunta que se le planteará al usuario
                print(pregunta)
                respuesta = input() #respuesta del usuario
                if pregunta == "¿Cuál es la fórmula de este ión "+ str(iones.iloc[id,1])+ " ?": # caso en el que muestra el nombre del ión y pregunta la formula
                    if respuesta == iones.iloc[id,2]:
                        print("Correcto")
                        cantidadAciertos = cantidadAciertos+ 1
                    else:
                        print("Incorrecto, la respuesta correcta es "+ iones.iloc[id,2])
                elif pregunta == "¿Cuál es el nombre del ión "+ str(iones.iloc[id,2])+ " ?": # caso en el que muestra la fórmula del ión y pregunta el nombre
                    if respuesta == iones.iloc[id,1]:
                        print("Correcto")
                        cantidadAciertos = cantidadAciertos+ 1
                    else:
                        print("Incorrecto, la respuesta correcta es "+ iones.iloc[id,1])
                elif  pregunta == "¿Cuál es la carga del ión "+ str(iones.iloc[id,1]) + " ?" or pregunta == "¿Cuál es la carga del ión "+ str(iones.iloc[id,2]) +" ?": # caso en el que se pregunte la  carga del ión
                    if respuesta == iones.iloc[id,3]:
                        print("Correcto")
                        cantidadAciertos = cantidadAciertos+ 1
                    else:
                        print("Incorrecto, la respuesta correcta es "+ iones.iloc[id,3])
                else:
                    print("Error en la generación del número aleatorio a, consultar Nomenclatura.py")
            print("¡Felicidades ! Acertaste " + str(cantidadAciertos) + " de " + str(cantidad))
        except TypeError:
            print("Error, no se pudo leer la cantidad de iones que quieres repasar")
    else:
        print("¡Gracias por participar!")
        continuar = False

