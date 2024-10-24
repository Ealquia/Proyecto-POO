#Se importan librerías útiles
import pandas as pd #usado en el manejo de dataframes y lectura de csv
import random as rn #usado en el método generarEjercicio
iones = pd.read_csv('Iones.csv') #dataframe de los iones registrados

class Nomenclatura:
    def __init__(self): # constructor
        self.__iones = iones

    def getIones(self):
        iones = self.__iones
        return iones

    def setIones(self, newIones):
        self.__iones = newIones

    #función para delimitar los iones que se quieren ejercitas
    def Nivel(self, opcion):
        iones = self.getIones()
        if opcion == 1:
            ionesNivel = iones[iones["Nivel"]== 1] #se extrae los iones que tienen nivel = 1
        elif opcion == 2:
            ionesNivel = iones[iones["Nivel"]== 2] #se extrae los iones que tienen nivel = 2
        elif opcion == 3:
            ionesNivel = iones[iones["Nivel"]== 3] #se extrae los iones que tienen nivel = 3
        elif opcion == 4:
            ionesNivel = iones[iones["Nivel"]== 4] #se extrae los iones que tienen nivel = 4
        elif opcion == 5:
            ionesNivel = iones # Opción si se quiere repasar sin importar el nivel
        else:
            ionesNivel = None # si el número ingresado no corresponde a ninguna de las opciones 
        return ionesNivel


    def Problema(self, ionesNivel):
        #función para generar un problema aleatorio de un ion específico
        if ionesNivel  is not None: # si el dataframe no es None
            pregunta = ""
            a = rn.randint(0,2) # variable aleatoria que determina que se pregunta
            cantIones = ionesNivel.shape[0]
            b = rn.randint(1,cantIones) # variable aleatoria que determina el fila del ión
            if a == 0: # caso en el que muestra el nombre del ión y pregunta la formula
                pregunta = "¿Cuál es la fórmula de este ión "+ str(ionesNivel.iloc[b,1])+ " ?"
            elif a == 1:  # caso en el que muestra la fórmula del ión y pregunta el nombre
                pregunta = "¿Cuál es el nombre del ión "+ str(ionesNivel.iloc[b,2])+ " ?"
            elif a  == 2:  # casos en el que pregunta la carga
                aleatorio2 =  rn.randint(0,1)
                if aleatorio2 == 0: # caso en el que muestra el nombre del ión y pregunta la carga
                    pregunta = "¿Cuál es la carga del ión "+ str(ionesNivel.iloc[b,1]) + " ?"
                elif aleatorio2 ==1:  # caso en el que muestra la fórmula del ión y pregunta la carga
                    pregunta = "¿Cuál es la carga del ión "+ str(ionesNivel.iloc[b,2]) +" ?"
                else: #error en la generación del número aleatorio 2
                    pregunta = "error en la generación del número aleatorio2"
            else:# error en la generación del número aleatorio 1
                pregunta = "error en la generación del número aleatorio1"
        else:
            pregunta = "Error en el dataFrame"
            b = 0

        return pregunta, b# retorna el problema así como el número del ión para poder  acceder a sus datos y comprobar la respuesta         




#Métodos estáticos ======================================================================================

def menú():
    a = """¿Qué nivel desea repasar?
    1. Nivel 1
    2. Nivel 2
    3. Nivel 3
    4. Nivel 4
    5. Todos los niveles"""
    return a