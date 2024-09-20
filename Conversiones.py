import pandas as pd

class Conversiones:
    def __init__(self):
        self.__Tabla = pd.read_csv('TablaConversiones.csv', sep=";")

    #Convierte cualquier unidad a su equivalente en el SI definido como estándar
    #Valor: valor numérico a convertir
    #dimensional: unidad de medida que se desea convertir al SI estándar
    def aSI(self, valor, dimensional):
        def convert(valor, dimensional): #Sub proceso que hace una conversión con el factor dado en el df
            estandar = self.__Tabla[self.__Tabla['Simbolo'] == dimensional].reset_index().at[0, "Estandarizar"] #Encontrar el factor correspondiente
            return valor*estandar #Devolver la conversión
        if self.__Tabla[self.__Tabla['Simbolo'] == dimensional].reset_index().at[0, "Tipo"] == "Densidad": #Si la medida es de densidad
            dims = dimensional.split("/") #Separar las dimensionales de masa y volumen
            return convert(valor,dims[0])/convert(1,dims[1]) #Convertir ambos masa y volumen y dividir  
        elif self.__Tabla[self.__Tabla['Simbolo'] == dimensional].reset_index().at[0, "Tipo"] == "Temperatura": #Si la medida es de temperatura
            if dimensional=="C": #Conversión de Celsius a Kelvin
                return valor + 273.15
            if dimensional=="F": #Conversión de Farenheit a Kelvin
                return (valor - 32)*(5/9) + 273.15
        else: #Para el resto de tipos de medida, usar el subproceso convert
            return convert(valor, dimensional)

    #Convierte un valor en unidades estándar a una unidad no estándar
    #Valor: valor numérico a convertir
    #Dimensional: unidad de medida a la que se desea convertir 
    def convert(self, valor, dimensional):
        def convert(valor, dimensional):
            estandar = self.__Tabla[self.__Tabla['Simbolo'] == dimensional].reset_index().at[0, "Estandarizar"]
            return valor/estandar
        if self.__Tabla[self.__Tabla['Simbolo'] == dimensional].reset_index().at[0, "Tipo"] == "Densidad":
            dims = dimensional.split("/")
            return convert(valor,dims[0])/convert(1,dims[1])
        elif self.__Tabla[self.__Tabla['Simbolo'] == dimensional].reset_index().at[0, "Tipo"] == "Temperatura": #Si la medida es de temperatura
            if dimensional=="C": #Conversión de Kelvin a Celsius
                return valor - 273.15
            if dimensional=="F": #Conversión de Kelvin a Farenheit
                return (valor - 273.15)*(9/5) + 32
        else:
            return convert(valor, dimensional)
    
    
