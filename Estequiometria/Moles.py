from Compuesto import Compuesto
from Estequiometria.Conversiones import Conversiones
from Reaccion import Reaccion


class Moles:
    #Constructor
    def __init__(self, compuesto, magnitud: float, dimensional: str = "mol"):
        self.__Magnitud = magnitud #Float magnitud 
        self.__Dimensional = dimensional #String con la dimensional
        if isinstance(compuesto, Compuesto): #Si el parámetro es un objeto Compuesto asignarlo al atributo
            self.__Compuesto = compuesto 
        if isinstance(compuesto, str): #Si el parámetro es el string del compuesto, crear el objeto y asignarlo al atributo
            self.__Compuesto = Compuesto(compuesto)
        self.C = Conversiones() #Crear un objeto de tipo conversiones para que lo use la clase
    
    #Convierte de moles de un compuesto a otro según los coeficientes de la reacción pasada
    def aMolesDe(self, reaccion, otroCompuesto):
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
            
    