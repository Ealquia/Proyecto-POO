#Se importan librerías útiles
import pandas as pd #usado en el manejo de dataframes y lectura de csv
import random as rn #usado en el método generarEjercicio
iones = pd.read_csv("Iones.csv") #dataframe de los iones registrados

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
        if opcion == 1:
            ionesNivel = self.getIones()[self.getIones["Nivel"]== 1] #se extrae los iones que tienen nivel = 1
        elif opcion == 2:
            ionesNivel = self.getIones()[self.getIones["Nivel"]== 2] #se extrae los iones que tienen nivel = 2
        elif opcion == 3:
            ionesNivel = self.getIones()[self.getIones["Nivel"]== 3] #se extrae los iones que tienen nivel = 3
        elif opcion == 4:
            ionesNivel = self.getIones()[self.getIones["Nivel"]== 4] #se extrae los iones que tienen nivel = 44
        elif opcion == 5:
            ionesNivel = self.getIones() # Opción si se quiere repasar sin importar el nivel
        else:
            ionesNivel = None # si el número ingresado no corresponde a ninguna de las opciones 
        return ionesNivel

    #función para determinar si el dataframe a utilizar es None
    #Esto es usado para atrapar el error de un número ingresado no correspondiente a ninguna opción
    def dtIsNone(self, ionesNivel):
        a = False
        if ionesNivel == None: # si es None de vuelve True
            a = True
        else:
            a = False # de lo contrario de vuelve False
        return a

    def Problema(self, ionesNivel):
        a = rn.randint(0,3)
        cantIones = ionesNivel.shape[0]
        b = rn.randint(1,cantIones)
        if a == 0: # caso en el que muestra el nombre del ión y pregunta la formula
            




#Métodos estáticos ======================================================================================

def menú():
    a = """¿Qué nivel desea repasar?
    1. Nivel 1
    2. Nivel 2
    3. Nivel 3
    4. Nivel 4
    5. Todos los niveles"""
    return a