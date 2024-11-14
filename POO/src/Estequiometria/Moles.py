from Compuesto import Compuesto
from Estequiometria.Conversiones import Conversiones
from Reaccion import Reaccion


class Moles:
    #Método para calcular cifras significativas
    def CifrasSig(dato:str):
        datoNum = float(dato)
        dato = dato.replace(".","") #Quitar el punto decimal
        for  i in range(len(dato)):
            if dato[i]!="0": 
                cifrasSig = len(dato[i:]) 
                break
            #Cortar la cadena después del primer dígito que no sea 0 y contar los dígitos
        return cifrasSig
    
    #Constructor
    def __init__(self, compuesto, magnitud: float = None, dimensional: str = "mol", teorico=True):
        self._CifrasSig = {}
        if isinstance(magnitud, str): #Si se pasa la magnitud como un string
            #Calcular las cifras significativas usando el método estático, crear un diccionario de cifras significativas y asignarlas ahí
            self._CifrasSig = {"Magnitud": Moles.CifrasSig(magnitud)}
            magnitud = float(magnitud) #Convertir la magnitud a float
        self.__Magnitud = magnitud #Float magnitud (Pueda inicializarse como None)
        self.__Dimensional =  dimensional
        if isinstance(compuesto, Compuesto): #Si el parámetro es un objeto Compuesto asignarlo al atributo
            self.__Compuesto = compuesto 
        if isinstance(compuesto, str): #Si el parámetro es el string del compuesto, crear el objeto y asignarlo al atributo
            self.__Compuesto = Compuesto(compuesto)
        self.__Teorico = teorico
        self.C = Conversiones() #Crear un objeto de tipo conversiones para que lo use la clase
    
    #Convierte de moles de un compuesto a otro según los coeficientes de la reacción pasada
    def aMolesDe(self, reaccion, otroCompuesto):
        if self.__Dimensional != "mol": self.__Magnitud = self.C.aSI(self.__Magnitud,self.__Dimensional) 
        if isinstance(reaccion, str):  #Si la reacción es un string, crear un objeto reaccion
            reaccion = Reaccion(reaccion)
        if isinstance(otroCompuesto, Compuesto):  #Si el otro compuesto es un objeto Compuesto, obtener la fórmula
            otroCompuesto = otroCompuesto.getCompuesto()
        reaccion.Balancear() #Balancear la reaccion
        miCoef = reaccion.getCompuesto(self.__Compuesto.getCompuesto()).getCoeficiente()  #Obtener el coeficiente de este compuesto
        otroCoef = reaccion.getCompuesto(otroCompuesto).getCoeficiente()  #Obtener el coeficiente del otro compuesto
        OtrosMoles = self.__Magnitud * (otroCoef / miCoef) #Calcular los moles del otro compuesto
        return Moles(otroCompuesto, OtrosMoles) #Crear y devolver objeto moles
    
    #Convierte a la unidad pasada como parámetro
    def Convert(self, nuevadimensional: str):
        conversion = self.C.convert(self.__Magnitud,self.__Dimensional) #Encontrar la conversión
        self.__Magnitud = conversion #Actualizar Magnitud
        self.__Dimensional = nuevadimensional #Actualizar Dimensional
        return conversion #Devolver la conversión
        
    def getIncognita(self,moles):
        self.__Magnitud = moles.getMoles()
        return self.Convert(self.__Dimensional)
        
    #ToString
    def __str__(self):
        info = f"{self.__Magnitud} {self.__Dimensional}es de {self.__Compuesto.getCompuesto()}"
        return info
    
    #Setters and getters
    def getMoles(self):
        return self.__Magnitud
    
    def setMoles(self,moles):
        self.__Magnitud = moles
        
    def getCompuesto(self):
        return self.__Compuesto
    
    def setCompuesto(self,compuesto):
        if isinstance(compuesto, Compuesto): #Si el parámetro es un objeto Compuesto asignarlo al atributo
            self.__Compuesto = compuesto 
        if isinstance(compuesto, str): #Si el parámetro es el string del compuesto, crear el objeto y asignarlo al atributo
            self.__Compuesto = Compuesto(compuesto)
            
    def getDimensional(self):
        return self.__Dimensional
    
    def setDimensional(self, dimensional):
        self.__Dimensional = dimensional

    def getCifrasSig(self):
        return  self._CifrasSig

    def getTeorico(self):
        return self.__Teorico
    
    def setTeorico(self, teorico):
        self.__Teorico = teorico