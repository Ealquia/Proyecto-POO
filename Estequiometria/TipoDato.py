from Compuesto import Compuesto
from Estequiometria.Conversiones import Conversiones
from Estequiometria.Moles import Moles

class TipoDato:
    #Constructor
    def __init__(self, dimensional: str, compuesto, magnitud: float = None, cifrasSig = [], teorico: bool = True, moles: float = None,):
        self._Magnitud = magnitud #Float magnitud (Pueda inicializarse como None)
        self._Dimensional = dimensional #String con la dimensional
        if isinstance(compuesto, Compuesto): #Si el parámetro es un objeto Compuesto asignarlo al atributo
            self._Compuesto = compuesto 
        if isinstance(compuesto, str): #Si el parámetro es el string del compuesto, crear el objeto y asignarlo al atributo
            self._Compuesto = Compuesto(compuesto)
        self._CifrasSig = cifrasSig #Cifras significativas como una lista de enteros (para todos los subdatos asociados)
        self._Moles = moles #Número de moles (puede inicializarse como None)
        self._Teorico = teorico #True por default. Útil si el problema trabaja con porcentajes de rendimiento
        self._PuntoPartida = not(magnitud==None) #Verdadero solo si la magnitud no es nula
        self.C = Conversiones() #Crear un objeto de tipo conversiones para que lo use la clase
        
    #Convierte el dato a su unidad estándar del SI y actualiza los atributos Magnitud y Dimensional
    def SI(self):
        conversion = self.C.aSI(self._Magnitud,self._Dimensional) #Convertir la magnitud dada a las unidades estándar del SI
        self._Magnitud = conversion #Actualizar el atributo Magnitud
        self._Dimensional = self.C.dimensionalSI(self._Dimensional) #Actualizar el atributo Dimensional
        return conversion #Devolver la nueva magnitud
    
    #Convierte el dato (que debe estar en forma estándar) a la unidad pasada como parámetro
    def Convert(self, nuevadimensional: str):
        conversion = self.C.convert(self._Magnitud,self._Dimensional) #Encontrar la conversión
        self._Magnitud = conversion #Actualizar Magnitud
        self._Dimensional = nuevadimensional #Actualizar Dimensional
        return conversion #Devolver la conversión
        
    #Convierte la magnitud a moles. Devuelve un objeto tipo moles 
    def aMoles(self):
        return Moles(compuesto = self._Compuesto, magnitud = self._Moles) #Devolver un objeto moles
    
    #Encuentra el valor faltante
    def getIncognita(self, getOtrasIncognitas: function, moles: float =None):
        if not(moles == None): #Si se pasó algún parámetro para moles
            self._Moles = moles
        if not(self.DatosInsuficientes([self._Magnitud, self._Moles, self._Molaridad])): #Si hay datos suficientes
            if self._Moles == None: #Si faltan los moles, 
                return self.aMoles() #encontrar con el método aMoles
            else: #De lo contrario, realizar la función pasada como parámetro
                getOtrasIncognitas()
        else: #Si los datos son insuficTientes
            raise Exception("No hay datos suficientes")
        
    #Verdadero si hay más de una incógnita
    def DatosInsuficientes(self, atributos):
        vacios = 0
        for atribute in atributos:
            if atribute == None:
                vacios =+ 1
        return vacios>1

    #toString
    def __str__(self):
        info = f"{self._Magnitud} {self._Dimensional} de {self._Compuesto.getCompuesto()}"
        return info

    #Setters and getters
    def getMagnitud(self):
        return self._Magnitud 
    
    def setMagnitud(self, magnitud: float):
        self._Magnitud = magnitud
    
    def getDimensional(self):
        return  self._Dimensional
    
    def getCompuesto(self):
        return  self._Compuesto
    
    def getCifrasSig(self):
        return  self._CifrasSig

    def setCifrasSig(self,cifras):
        self._CifrasSig = cifras
    
    def getMoles(self):
        return  self._Moles
    
    def setMoles(self, moles):
        self._Moles = moles
    
    def getTeorico(self):
        return  self._Teorico
    
    def getPuntoPartida(self):
        return  self._PuntoPartida
    
    def setPuntoPartida(self, cambio: bool):
        self._PuntoPartida = cambio
        
