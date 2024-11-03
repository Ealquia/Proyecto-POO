from Estequiometria.Moles import Moles
from Estequiometria.TipoDato import TipoDato

class Solucion(TipoDato):
    #Constructor
    def __init__(self, compuesto, dimensional: str="L", magnitud: float = None, molaridad:float = None, teorico: bool = True, moles: float = None):
        super().__init__(dimensional, compuesto, magnitud, teorico, moles) #Llamar al constructor de la clase padre
        self._PuntoPartida = not(magnitud==None) and not(molaridad==None) #Actualizar punto partida: Verdadero si se tienen la magnitud y la molaridad
        if isinstance(molaridad, str): #Si se pasa la molairdad como un string
            #Calcular las cifras significativas usando el método estático, asignar en el diccionario
            self._CifrasSig["Molaridad"] = TipoDato.CifrasSig(molaridad)
            molaridad = float(molaridad) #Covertir la molaridad a float
        self._Molaridad = molaridad #Agregar atributo molaridad
        self.Atributos.append(self._Molaridad) #Añadir el atributo molaridad a la lista de atributos
        
    #Override
    def aMoles(self):
        if  self._PuntoPartida:
            self.SI() #Estandarizar
            moles = self._Magnitud*self._Molaridad #Multiplicar la magnitud (L) por la molaridad (mol/L)
            self._Moles = moles #Actualizar atributo moles
            return super().aMoles() #Devolver un objeto moles
        else:
            raise ValueError("El dato utilizado no era un punto de partida válido")
        
    #Override
    def getIncognita(self, moles: Moles = None):
        def getOtrasIncognitas():
            if self._Magnitud == None: #Si falta la magnitud
                mag = self._Moles/self._Molaridad #Encontrar con el proceso inverso
                self._Magnitud = self.C.convert(mag, self._Dimensional) #Convertir el volumen encontrado a la unidad del dato. Actualizar magnitud
                return self._Magnitud #Devolver magnitud
            if self._Molaridad == None: #Si falta la molaridad
                self._Molaridad = self._Moles/self.C.aSI(self._Magnitud, self._Dimensional["Magnitud"]) #Encontrarla como moles (mol) / Magnitud (L)
                return self._Molaridad
        return super().getIncognita(getOtrasIncognitas,moles) #Hacer el proceso general + el proceso "getOtrasIncognitas"
    
    #Override
    def __str__(self):
        info = super().__str__() + f" {self._Molaridad} Molar"
        return info