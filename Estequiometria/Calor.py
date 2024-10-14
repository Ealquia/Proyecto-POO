from Estequiometria.TipoDato import TipoDato
from Reaccion import Reaccion

class Calor(TipoDato):
    def __init__(self, reaccion: Reaccion,  compuesto = None, dimMagnitud: str="kJ", dimEntalpia: str = "kJ", magnitud: float = None, entalpia:float = None, cifrasSig = None, teorico: bool = True, moles: float = None):
        super().__init__(dimMagnitud, compuesto, magnitud, cifrasSig, teorico, moles) #Llamar al constructor de la clase padre
        self._Entalpia = entalpia #Añadir el atributo entalpía
        self._Dimensional = {"Magnitud": dimMagnitud, "Entalpia": dimEntalpia}
        self._Reaccion = reaccion #Añadir el atributo reacción
        self._PuntoPartida = not(magnitud==None) and not(entalpia==None) #Actualizar punto partida: Verdadero si se tiene la magnitud y la densidad
        self.Atributos.append(self._Entalpia) #Añadir el atributo  densidad a la lista de atributos
        
    #Override 
    def SI(self):
        if not(self._Magnitud == None): super().SI() #Proceso general para convertir la magnitud (calor)
        if not(self._Entalpia == None): 
            self._Entalpia = self.C.aSI(self._Presion,self._Dimensional["Entalpia"]) #Convertir la entalpia
            if self._PuntoPartida: self._Dimensional["Entalpia"] = self.C.dimensionalSI(self._Dimensional["Entalpia"]) #Actualizar las dimensionales
        return self
    