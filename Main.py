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

def datoEstequiometria(reaccion):
    print("Compuesto: ")
    compuesto = menuString(reaccion.ObtenerReactivosString()+reaccion.ObtenerProductosString(),"Ingrese el número del compuesto: ")
    tipoDato = menu(["Masa","Volumen Líquido","Volumen Solución","Volumen de Gas"],"¿Qué tipo de dato desea ingresar? Ingrese el número correspondiente: ")
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

def incognitaEstequiometria(reaccion):
    tipoDato = menu(["Masa","Volumen Líquido","Volumen Solución","Volumen de Gas","Densidad de un líquido","Molaridad de una solución", "Presión de un gas", "Temperatura de un gas"],
                    "¿Qué desea encontrar? Ingrese el número correspondiente: ")
    print("¿De qué compuesto?")
    compuesto = menuString(reaccion.ObtenerReactivosString()+reaccion.ObtenerProductosString(),"Ingrese el número del compuesto: ")
    C = Conversiones()
    if tipoDato==1:
        dimensionales = menuString(C.listaDimensionales("Masa"),"Ingrese  el número de la unidad correspondiente: ")
        incognita = Masa(dimensional=dimensionales)
    if tipoDato==2 or  tipoDato==5:
        if  tipoDato!=2:
            print("Dimensionales del volumen:")
            dimensionales = menuString(C.listaDimensionales("Volumen"),"Ingrese  el número de la unidad correspondiente: ")
            magnitud = float(input("Ingrese la magnitud del volumen del líquido: "))
        if  tipoDato!=3:
            print("Dimensionales de la densidad:")
            dimDensidad = menuString(C.listaDimensionales("Densidad"),"Ingrese  el número de la unidad correspondiente: ")
            densidad = float(input("Ingresela densidad del compuesto (si no la conoce,  ingrese 0): "))
            if densidad==0: densidad = None
        incognita = Liquido(compuesto=compuesto,dimMagnitud=dimensionales,dimDensidad=dimDensidad,magnitud=magnitud,densidad=densidad)
    if tipoDato==3 or tipoDato==6:
        if tipoDato!=3:
            print("Dimensionales del volumen:")
            dimensionales = menuString(C.listaDimensionales("Volumen"),"Ingrese  el número de la unidad correspondiente: ")
            magnitud = float(input("Ingrese la magnitud del volumen de la solución: "))
        if tipoDato != 6:
            molaridad = float(input("Ingrese la molaridad de la solución (M): "))
        incognita = Solucion(compuesto=compuesto,dimensional=dimensionales,magnitud=magnitud,molaridad=molaridad)
    if tipoDato==4 or tipoDato==7 or tipoDato==8:
        if  tipoDato!=4:
            print("Dimensionales del volumen:")
            dimensionales = menuString(C.listaDimensionales("Volumen"),"Ingrese  el número de la unidad correspondiente: ")
            magnitud = float(input("Ingrese la magnitud del volumen del gas: "))
        if tipoDato != 7:
            print("Dimensionales de la presión:")
            dimPresion =  menuString(C.listaDimensionales("Presion"),"Ingrese  el número de la unidad correspondiente: ")
            presion = float(input("Ingrese la magnitud de la presión: "))
        if  tipoDato != 8:
            print("Dimensionales de la temperatura")
            dimTemp =  menuString(C.listaDimensionales("Temperatura"),"Ingrese  el número de la unidad correspondiente: ")
            temp = float(input("Ingrese la magnitud de la temperatura: "))
        incognita = Gas(compuesto=compuesto,magnitud=magnitud,dimVolumen=dimensionales,dimPresion=dimPresion,
                   presion=presion,dimTemperatura=dimTemp,temperatura=temp)
    return incognita, tipoDato

from Compuesto import Compuesto
from Reaccion import Reaccion
from Estequiometria.Conversiones import Conversiones

#Main
print("Gracias por ser un beta tester de nuestra app de química! ¿Qué función deseas usar?")
continuar = True
while(continuar):
    opcion = menu(["Masa Molar", "Balanceo", "Estequiometría", "Nomenclatura"],"Ingrese el número de la opción correspondiente: ")
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
        print("Escribe la reacción química sin balancear separada por un signo = ")
        strReaccion = input()  #input de la fórmula
        reaccion  = Reaccion(strReaccion) #Creación del objeto
        if problema==1:
            print("Ingrese el primer dato:")
            dato = datoEstequiometria(reaccion)
            print(dato)
            print("Ingrese la incógnita: ")
            incognita = incognitaEstequiometria(reaccion)
            
