from Estequiometria.TipoDato import TipoDato
from Reaccion import Reaccion

class problemaEsteq:
    def  __init__(self, Datos, Incognita: TipoDato, reaccion, Rendimiento: float =  100):
        self.__Datos = Datos
        self.__Incognita = Incognita
        if isinstance(Reaccion, str):
            reaccion = Reaccion(reaccion)
        self.__Reaccion = reaccion
        self.__Rendimiento = Rendimiento
        self.__cifrasRendimiento = None
        self.__Respuesta = None

    def deCosaACosa(self, de: TipoDato = None):
        if de == None:
            de = self.__Datos
        a = self.__Incognita
        moles1 = de.aMoles() #Convertir el primer dato a moles
        print(moles1)
        moles2 = moles1.aMolesDe(self.__Reaccion, a.getCompuesto()) #Convertir a moles del segundo compuesto
        print(moles2)
        a.getIncognita(moles2)
        return a