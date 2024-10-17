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


def datoEstequiometria(reaccion):
    print("Compuesto: ")
    compuesto = menuString(reaccion.ObtenerReactivosComp()+reaccion.ObtenerProductosComp(),"Ingrese el número del compuesto: ")
    tipoDato = menu(["Masa","Volumen Líquido","Volumen Solución","Volumen de Gas"],"¿Qué tipo de dato desea ingresar? Ingrese el número correspondiente: ")
    if tipoDato==1:
        dimensionales = menuString(Conversiones.listaDimensionales("Masa"))
        magnitud = float(input("Ingrese la magnitud de la masa: "))
    if tipoDato==2:
        dimensionales = menuString(Conversiones.listaDimensionales("Volumen"))
        magnitud = float(input("Ingrese la magnitud del volumen: "))
        densidad = float(input("Ingresela densidad del compuesto: "))

        
    
import pandas as pd
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