from Compuesto import Compuesto
from Estequiometria.Conversiones import Conversiones
from Estequiometria.Moles import Moles

class TipoDato:
    def cifrasSignificativas(magnitud: float):
        #Contar el número de dígitos en la magnitud y devolverlo
        cifrasSig = str(magnitud) 
        return sum(c.isdigit() for c in cifrasSig if c != '.')
        
    #Constructor
    def __init__(self, dimensional: str, compuesto, magnitud: float = None, cifrasSig = None, teorico: bool = True, moles: float = None):
        self._Magnitud = magnitud #Float magnitud (Pueda inicializarse como None)
        self._Dimensional = {"Magnitud": dimensional} #String con la dimensional
        if isinstance(compuesto, str): #Si el parámetro es el string del compuesto, crear el objeto y asignarlo al atributo
            self._Compuesto = Compuesto(compuesto)
        else: self._Compuesto = compuesto 
        if cifrasSig==None: #Si no se dan cifras significativas
            self._CifrasSig = TipoDato.cifrasSignificativas(magnitud) #Calcular las cifras significativas usando el método estático
        else:
            self._CifrasSig = cifrasSig
        self._Moles = moles #Número de moles (puede inicializarse como None)
        self._Teorico = teorico #True por default. Útil si el problema trabaja con porcentajes de rendimiento
        self._PuntoPartida = not(magnitud==None) #Verdadero solo si la magnitud no es nula
        self.C = Conversiones() #Crear un objeto de tipo conversiones para que lo use la clase
        self.Atributos = [self._Moles, self._Magnitud] #Lista de los atributos que pueden ser incógnitas
         
    #Convierte el dato a su unidad estándar del SI y actualiza los atributos Magnitud y Dimensional
    def SI(self):
        self._Magnitud = self.C.aSI(self._Magnitud,self._Dimensional["Magnitud"]) #Convertir la magnitud
        if self._PuntoPartida: self._Dimensional["Magnitud"] = self.C.dimensionalSI(self._Dimensional["Magnitud"]) #Actualizar la dimensional (a menos que se trate de una incógnita)
        return self._Magnitud #Devolver la nueva magnitud
    
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
    def getIncognita(self, getOtrasIncognitas, moles: Moles = None):
        if not(moles == None): #Si se pasó algún parámetro para moles
            self.setMoles(moles.getMoles())
        datos = self.DatosInsuficientes()
        if not(datos): #Si hay datos suficientes
            if self._Moles == None: #Si faltan los moles, 
                return self.aMoles() #encontrar con el método aMoles
            else: #De lo contrario, realizar la función pasada como parámetro
                return getOtrasIncognitas()
        if datos: #Si los datos son insuficTientes
            raise Exception("No hay datos suficientes para encontrar la incógnita")
        
    #Verdadero si hay más de una incógnita
    def DatosInsuficientes(self):
        vacios = 0
        for atribute in self.Atributos:
            if atribute == None:
                vacios = vacios + 1
        return vacios>1

    #toString
    def __str__(self):
        dimensional = self._Dimensional if type(self._Dimensional) == str else self._Dimensional["Magnitud"]
        info = f"{self._Magnitud} {dimensional} de {self._Compuesto.getCompuesto()}"
        return info
        
    #Setters and getters
    def getMagnitud(self):
        return self._Magnitud 
    
    def setMagnitud(self, magnitud: float):
        self._Magnitud = magnitud
        self.Atributos[1] =  magnitud

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
        self.Atributos[0] = moles
    
    def getTeorico(self):
        return  self._Teorico
    
    def getPuntoPartida(self):
        return  self._PuntoPartida
    
    def setPuntoPartida(self, cambio: bool):
        self._PuntoPartida = cambio
        
