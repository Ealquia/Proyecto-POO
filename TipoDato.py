from Compuesto import Compuesto
from Conversiones import Conversiones

class TipoDato:
    #Constructor
    def __init__(self, dimensional: str, compuesto, magnitud: float = None, cifrasSig: list[int] = [], teorico: bool = True, moles: float = None,):
        self.__Magnitud = magnitud #Float magnitud (Pueda inicializarse como None)
        self.__Dimensional = dimensional #String con la dimensional
        if isinstance(compuesto, Compuesto): #Si el parámetro es un objeto Compuesto asignarlo al atributo
            self.__Compuesto = compuesto 
        if isinstance(compuesto, str): #Si el parámetro es el string del compuesto, crear el objeto y asignarlo al atributo
            self.__Compuesto = Compuesto(compuesto)
        self.__CifrasSig = cifrasSig #Cifras significativas como una lista de enteros (para todos los subdatos asociados)
        self.__Moles = moles #Número de moles (puede inicializarse como None)
        self.__Teorico = teorico #True por default. Útil si el problema trabaja con porcentajes de rendimiento
        self.__PuntoPartida = not(magnitud==None) #Verdadero solo si la magnitud no es nula
        self.C = Conversiones() #Crear un objeto de tipo conversiones para que lo use la clase
        
    #Convierte el dato a su unidad estándar del SI y actualiza los atributos Magnitud y Dimensional
    def SI(self):
        conversion = self.C.aSI(self.__Magnitud,self.__Dimensional) #Convertir la magnitud dada a las unidades estándar del SI
        self.__Magnitud = conversion #Actualizar el atributo Magnitud
        self.__Dimensional = self.C.dimensionalSI(self.__Dimensional) #Actualizar el atributo Dimensional
        return conversion #Devolver la nueva magnitud
    
    #Convierte el dato (que debe estar en forma estándar) a la unidad pasada como parámetro
    def Convert(self, nuevadimensional: str):
        conversion = self.C.convert(self.__Magnitud,self.__Dimensional) #Encontrar la conversión
        self.__Magnitud = conversion #Actualizar Magnitud
        self.__Dimensional = nuevadimensional #Actualizar Dimensional
        return conversion #Devolver la conversión
        
    #Convierte la magnitud a moles
    def aMoles(self):
        if self.__Dimensional == self.C.dimensionalSI(self.__Dimensional): #Verifica si el dato está en forma estándar
            moles = self.__Magnitud/self.__Compuesto.masaMolar() #Versión más general del método, se divide la magnitud dentro de la masa molar
            self.__Moles = moles #Actualizar el atributo moles
            return moles #Devolver los moles
        else:
            raise Exception("El dato no está en forma estándar")
    
    #Encuentra el valor faltante
    def getIncognita(self):
        if not(self.DatosInsuficientes()): #Si hay datos suficientes
            if self.__Moles == None: #Si faltan los moles, 
                return self.aMoles() #encontrar con el método aMoles
            if self.__Magnitud == None: #Si falta la magnitud
                mag = self.__Moles*self.__Compuesto.masaMolar() #Encontrar con el proceso inverso
                self.__Magnitud = self.C.convert(mag, self.__Dimensional) #Convertir la incógnita encontrada a la unidad del dato. Actualizar magnitud
                return self.__Magnitud #Devolver magnitud
        else: #Si los datos son insuficTientes
            raise Exception("No hay datos suficientes")
        
    #Verdadero si hay más de una incógnita
    def DatosInsuficientes(self):
        return self.__Magnitud == None and self.__Moles == None

    #toString
    def __str__(self):
        info = f"{self.__Magnitud} {self.__Dimensional} de {self.__Compuesto.getCompuesto()}"
        return info

    #Setters and getters
    def getMagnitud(self):
        return self.__Magnitud 
    
    def setMagnitud(self, magnitud: float):
        self.__Magnitud = magnitud
    
    def getDimensional(self):
        return  self.__Dimensional
    
    def getCompuesto(self):
        return  self.__Compuesto
    
    def getCifrasSig(self):
        return  self.__CifrasSig

    def setCifrasSig(self,cifras: list[int]):
        self.__CifrasSig = cifras
    
    def getMoles(self):
        return  self.__Moles
    
    def setMoles(self, moles):
        self.__Moles = moles
    
    def getTeorico(self):
        return  self.__Teorico
    
    def getPuntoPartida(self):
        return  self.__PuntoPartida
    
    def setPuntoPartida(self, cambio: bool):
        self.__PuntoPartida = cambio