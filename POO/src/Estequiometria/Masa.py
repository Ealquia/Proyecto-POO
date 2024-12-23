from Estequiometria.Moles import Moles
from Estequiometria.TipoDato import TipoDato

class Masa(TipoDato):
    def __init__(self, compuesto, dimensional: str="g", magnitud: float = None, teorico: bool = True, moles: float = None):
        super().__init__(dimensional, compuesto, magnitud, teorico, moles) #Llamar a la clase padre
        
   #Override 
    def getIncognita(self, moles: Moles = None):
        def getOtrasIncognitas():
            if self._Magnitud == None: #Si falta la magnitud
                mag = self._Moles*self._Compuesto.masaMolar() #Encontrar con el proceso inverso
                self._Magnitud = self.C.convert(mag, self._Dimensional["Magnitud"]) #Convertir la masa encontrada a la unidad del dato. Actualizar magnitud
                return self._Magnitud #Devolver magnitud
            else: #Si se tienen los dos
                self._Magnitud = self.C.convert(self._Magnitud, self._Dimensional) #Convertir la masa a la unidad del dato. Actualizar magnitud
        return super().getIncognita(getOtrasIncognitas, moles=moles) #Hacer el proceso general + el proceso "getOtrasIncognitas"
        
    #Override
    def aMoles(self):
        if self._PuntoPartida:
            self.SI() #Estandarizar
            moles = self._Magnitud/self._Compuesto.masaMolar() #Didivir la magnitud (g) dentro de la masa molar (g/mol)
            self._Moles = moles #Actualizar el atributo moles
            return super().aMoles() #Devolver un objeto moles
        else:
            raise ValueError("El dato utilizado no es un punto de partida válido")
