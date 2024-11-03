from Estequiometria.Moles import Moles
from Estequiometria.TipoDato import TipoDato
from Reaccion import Reaccion

class Calor(TipoDato):
    def __init__(self, reaccion: Reaccion,  compuesto = None, dimMagnitud: str="kJ", dimEntalpia: str = "kJ", magnitud: float = None, entalpia:float = None, cifrasSig = None, teorico: bool = True, moles: float = None):
        super().__init__(dimMagnitud, compuesto, magnitud, cifrasSig, teorico, moles) #Llamar al constructor de la clase padre
        if isinstance(entalpia, str): #Si se pasa la entalpia como un string
            #Calcular las cifras significativas usando el método estático, asignar en el diccionario
            self._CifrasSig["Entalpia"] = TipoDato.CifrasSig(entalpia)
            entalpia = float(entalpia) #Covertir la entalpia a float
        self._Entalpia = entalpia #Añadir el atributo entalpía
        self._Dimensional = {"Magnitud": dimMagnitud, "Entalpia": dimEntalpia}
        self._Reaccion = reaccion #Añadir el atributo reacción
        self._PuntoPartida = not(magnitud==None) and not(entalpia==None) #Actualizar punto partida: Verdadero si se tiene la magnitud y la densidad
        self._EntalpiaMolar = not(compuesto==None)
        self.Atributos.append(self._Entalpia) #Añadir el atributo  densidad a la lista de atributos
        
    #Override 
    def SI(self):
        if not(self._Magnitud == None): super().SI() #Proceso general para convertir la magnitud (calor)
        if not(self._Entalpia == None): 
            self._Entalpia = self.C.aSI(self._Presion,self._Dimensional["Entalpia"]) #Convertir la entalpia
            if self._PuntoPartida: self._Dimensional["Entalpia"] = self.C.dimensionalSI(self._Dimensional["Entalpia"]) #Actualizar las dimensionales
        return self
    
    def aEntalpiaMolar(self):
        if not(self._Compuesto==None): #Evaluar que se haya  ingresado un compuesto     
            self.SI() #Estandarizar       
            if not(self._EntalpiaMolar): #Si la entalpía es de la reaccion
                self._Reaccion.Balancear() #Balancear la reacción
                miCoef = self._Reaccion.getCompuesto(self.__Compuesto.getCompuesto()).getCoeficiente()  #Obtener el coeficiente de este compuesto
                self._Entalpia = self._Entalpia/miCoef  #Convertir la entalpía a molar (kJ/mol)
                self._EntalpiaMolar = True 
        else:
            raise  ValueError("No se ha ingresado un compuesto")
    
    #Override
    def aMoles(self):
        self.SI() #Estandarizar
        self.aEntalpiaMolar() #Asegurar que la entalpía sea molar 
        self._Moles = self._Magnitud / self._Entalpia # calor (kJ) / entalpia molar (kJ/mol) = moles (mol)
        return super.aMoles()

    #Override
    def getIncognita(self, moles: Moles = None):
        def getOtrasIncognitas():
            self.SI() #Estandarizar
            if self._Magnitud == None: #Si falta la magnitud (calor)
                self.aEntalpiaMolar() #Asegurar que la entalpía sea molar 
                self._Magnitud =  self._Entalpia * self._Moles #calor (kJ) = entalpia (jJ/mol) *  moles (mol)
                return self._Magnitud #Devolver la magnitud (calor)
            if self._Entalpia == None:  #Si falta la entalpia
                self._Entalpia = self._Magnitud / self._Moles #entalpia (KJ/mol)
                if not(self._EntalpiaMolar):  #Si la entalpía es de la reaccion
                    self._Reaccion.Balancear() #Balancear la reaccion
                    miCoef = self._Reaccion.getCompuesto(self.__Compuesto.getCompuesto()).getCoeficiente()  #Obtener el coeficiente de este compuesto
                    self._Entalpia  = self._Entalpia * miCoef  #entalpia molar (KJ/mol) *coeficiente mol  = entalpia (KJ)
                return  self._Entalpia #Devolver la entalpia
        return super().getIncognita(getOtrasIncognitas, moles) 
                
    #Override
    def __str__(self):
        if (self._Magnitud>0):
            return f"{self._Magnitud} {self._Dimensional}"

    def getEntalpia(self):
        return self._Entalpia
    
    def setEntalpia(self, entalpia):
        self._Entalpia = entalpia