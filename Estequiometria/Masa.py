from Estequiometria.TipoDato import TipoDato


class Masa(TipoDato):
    def __init__(self, compuesto, dimensional: str="g", magnitud: float = None, cifrasSig = [], teorico: bool = True, moles: float = None):
        super().__init__(dimensional, compuesto, magnitud, cifrasSig, teorico, moles)
        
    def getIncognita(self):
        if not(self.DatosInsuficientes()): #Si hay datos suficientes
            if self._Moles == None: #Si faltan los moles, 
                return self.aMoles() #encontrar con el método aMoles
            if self._Magnitud == None: #Si falta la magnitud
                mag = self._Moles*self._Compuesto.masaMolar() #Encontrar con el proceso inverso
                self._Magnitud = self.C.convert(mag, self._Dimensional) #Convertir la incógnita encontrada a la unidad del dato. Actualizar magnitud
                return self._Magnitud #Devolver magnitud
        else: #Si los datos son insuficTientes
            raise Exception("No hay datos suficientes")
        
    def aMoles(self):
        self.SI()
        moles = self._Magnitud/self._Compuesto.masaMolar() #Didivir la magnitud (masa) dentro de la masa molar
        self._Moles = moles #Actualizar el atributo moles
        return moles
