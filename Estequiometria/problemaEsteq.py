from Estequiometria.TipoDato import TipoDato
from Reaccion import Reaccion
import copy

class problemaEsteq:
    def  __init__(self, Datos, Incognita: TipoDato = None, reaccion = None, compuesto = None, Rendimiento: float =  100):
        self.__Datos = [] #Crear una lista vacía de datos
        self.__Datos.extend(Datos) #Añadir los datos pasados como parámetro
        self.__Incognita = Incognita
        if isinstance(Reaccion, str):
            reaccion = Reaccion(reaccion)
        self.__Compuesto = compuesto
        self.__Reaccion = reaccion
        self.__Rendimiento = Rendimiento
        self.__cifrasRendimiento = None
        self.__Respuesta = None

    def TipoProblema(self):
        if not(self.__Compuesto ==None):  
            return "unaCosa" #Hay un compuesto y la conversión es entre el mismo  compuesto
        if len(self.__Datos)==1 and not(self.__Incognita==None) and not(self.__Reaccion==None): 
            return "deCosaACosa"  #Hay un solo dato, una incógnita y una reacción, es un problema de esequiometría simple
        if len(self._Datos)>1  and not(self.__Incognita==None) and not(self.__Reaccion==None):
            return "reactivoLimitante" #Hay más de un dato, una incógnita y una reacción, es un problema de reactivo limitante
        if len(self.__Datos)>1 and (self.__Incognita==None) and not(self.__Rendimiento==100): #Hay más de un dato y no hay incógnita 
            return "porcentajeRendimiento"

    def deCosaACosa(self, de=0, a=None):
        de = self.__Datos[de] #Obtener el dato de la lista de datos (el primer dato es el default)
        if (a==None): a = self.__Incognita #Si no se pasa parámetro "a" se asume que es la incógnita
        moles1 = de.aMoles() #Convertir el primer dato a moles
        moles2 = moles1.aMolesDe(self.__Reaccion, a.getCompuesto()) #Convertir a moles del segundo compuesto
        #Encontrar el valor de la incógnita 
        return a.getIncognita(moles2), a
    
    def reactivoLimitante(self, datos=None):
        if  datos==None: datos = self.__Datos #Si no se pasa lista de datos se asume  que es la lista de datos del problema
        valorCritico = 0
        for i  in range(len(self.__Datos)): #Por cada dato en la lista
            if self.__Datos[i]._PuntoPartida: #Si el dato es un punto de partida válido, 
                prueba = copy.deepcopy(self.__Incognita) #Hacer una copia de la incognita
                result = self.deCosaACosa(de=i, a=prueba) #obtener el valor de la incognita a partir de ese dato
                if i == 0: valorCritico = result #Si es el primer dato, asignar el resultado a valor crítico
                if result <= valorCritico: #Si el resultado es menor al valor crítico, cambiar el valor crítico
                    valorCritico = result
                    reactivoLimitante = self.__Datos[i] #Asignar el dato correspondiente al reactivo limitante
        return reactivoLimitante #Devolver el reactivo limitante
    
    def porcentajeRendimiento(self):
        datosReales = []
        for dato in self.__Datos: #Recorrer la lista de datos
            if dato.getTeorico(): #Si se encuentra el dato teórico
                self.__Incognita = copy.deepcopy(dato) #Asignar a la incógnita una copia del dato teórico
                self.__Incognita.setMagnitud(None) #Quitarle la magnitud a la incógnita
            else:
                datosReales.append(dato) #Añadir el dato real a la lista de datos reales
        #if len(datosReales) > 1:
            #reactivo