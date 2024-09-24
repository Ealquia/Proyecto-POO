from Compuesto import Compuesto

class TipoDato:
    #Constructor
    def __init__(self, dimensional, compuesto, magnitud = None, moles = None, cifrasSig = [], teorico = True):
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
    
    