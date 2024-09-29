import os
import pandas as pd

class Conversiones:
    def __init__(self):
        # Directorio donde está el script
        directorio_script = os.path.dirname(__file__)
        #Ruta relativa al archivo
        nombre_archivo = os.path.join(directorio_script,'TablaConversiones.csv')
        self.__Tabla = pd.read_csv(nombre_archivo, sep=";")

    #Convierte cualquier unidad a su equivalente en el SI definido como estándar
    #Valor: valor numérico a convertir
    #dimensional: unidad de medida que se desea convertir al SI estándar
    def aSI(self, valor: float, dimensional: str):
        def convert(valor: float, dimensional: str): #Sub proceso que hace una conversión con el factor dado en el df
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
    def convert(self, valor: float, dimensional: str):
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
    
    #Devuelve la dimensional estándar para el tipo de unidad (masa, volumen, etc) que se le pase como parámetro
    #dimensional: String con la dimensional que se tiene 
    def dimensionalSI(self,dimensional):
        tipo = self.__Tabla[self.__Tabla['Simbolo'] == dimensional].reset_index().at[0, "Tipo"] #Encontrar el tipo de la dimensional dada
        tipos = self.__Tabla[self.__Tabla['Tipo'] == tipo] #Crear un df con todas las filas de ese tipo
        if len(tipos) <1 :
            raise Exception("La dimensional no existe")
        else:
            dimensionalSI = tipos[tipos['Estandar?'] == 1].reset_index().at[0, "Simbolo"] #Encontrar el símbolo de la dimensional de ese tipo definida como estándar
            return dimensionalSI #Devolver la dimensional

    #Verdadero si las dos dimensionales son del mismo tipo
    def mismoTipo(self, dimensional1, dimensional2):
        tipo = self.__Tabla[self.__Tabla['Tipo'] == self.getTipo(dimensional1)] #Crear un df con todas las filas del tipo de la dimensional 1
        return dimensional2 in tipo["Simbolo"].values #Devolver verdadero si la segunda dimensional está en el df del tipo
    
    #Encontrar el tipo de una dimensional dada
    def getTipo(self,dimensional: str):
        tipo = self.__Tabla[self.__Tabla['Simbolo'] == dimensional].reset_index().at[0, "Tipo"] #Encontrar el tipo 
        return tipo
    
    #Devuelve una lista de las dimensionales para el tipo indicado
    def listaDimensionales(self, tipo: str):
        dimensionales = self.__Tabla[self.__Tabla["Tipo"] == tipo]["Tipo"].to_list
        return dimensionales