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
        if problema == 1:
            print("Escribe la reacción química sin balancear separada por un signo = ")
            strReaccion = input()  #input de la fórmula
            reaccion  = Reaccion(strReaccion) #Creación del objeto
            
