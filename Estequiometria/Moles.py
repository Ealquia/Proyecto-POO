from Compuesto import Compuesto
from Estequiometria.Conversiones import Conversiones
from Reaccion import Reaccion
from Estequiometria.Masa import Masa

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
        
    #Convierte moles a masa, puede pasársele un objeto tipo masa o no
    def aMasa(self, masa: Masa=None):
        gramos = self.__Magnitud*self.__Compuesto.masaMolar()
        if masa == None:
            return Masa(self.__Compuesto,magnitud=gramos,moles=self.__Magnitud)
        else:
            masa.setMagnitud(gramos)
            masa.setMoles(self.__Magnitud)
            masa.getIncognita()
            return masa
    
    #Convierte a la unidad pasada como parámetro
    def Convert(self, nuevadimensional: str):
        conversion = self.C.convert(self.__Magnitud,self.__Dimensional) #Encontrar la conversión
        self.__Magnitud = conversion #Actualizar Magnitud
        self.__Dimensional = nuevadimensional #Actualizar Dimensional
        return conversion #Devolver la conversión
        
    def __str__(self):
        info = f"{self.__Magnitud} {self.__Dimensional}es de {self.__Compuesto.getCompuesto()}"
        return info