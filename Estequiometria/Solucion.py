from Estequiometria.TipoDato import TipoDato

class Solucion(TipoDato):
    #Constructor
    def __init__(self, compuesto, dimensional: str="L", magnitud: float = None, molaridad:float = None, cifrasSig = [], teorico: bool = True, moles: float = None):
        super().__init__(dimensional, compuesto, magnitud, cifrasSig, teorico, moles) #Llamar al constructor de la clase padre
        self._PuntoPartida = not(magnitud==None) and not(molaridad==None) #Actualizar punto partida: Verdadero si se tienen la magnitud y la molaridad
        self._Molaridad = molaridad #Agregar atributo molaridad
        
    #Override
    def aMoles(self):
        self.SI() #Estandarizar
        moles = self._Magnitud*self._Molaridad #Multiplicar la magnitud (L) por la molaridad (mol/L)
        self._Moles = moles #Actualizar atributo moles
        return super.aMoles() #Devolver un objeto moles
    
    def getIncognita(self,moles = None):
        def getOtrasIncognitas():
            if self._Magnitud == None: #Si falta la magnitud
                mag = self._Moles/self._Molaridad #Encontrar con el proceso inverso
                self._Magnitud = self.C.convert(mag, self._Dimensional) #Convertir el volumen encontrado a la unidad del dato. Actualizar magnitud
                return self._Magnitud #Devolver magnitud
            if self._Molaridad == None: #Si falta la molaridad
                self._Molaridad = self._Moles/self._Magnitud #Encontrarla como moles (mol) / Magnitud (L)
                return self._Molaridad
        return super.getIncognita(getOtrasIncognitas,moles) #Hacer el proceso general + el proceso "getOtrasIncognitas"
    
    