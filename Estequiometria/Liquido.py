from Estequiometria.TipoDato import TipoDato
from Estequiometria.Masa import Masa

class Liquido(TipoDato):
    #Constructor
    def __init__(self, compuesto, dimMagnitud: str="L", dimDensidad: str = "g/L", magnitud: float = None, densidad:float = None, cifrasSig = None, teorico: bool = True, moles: float = None):
        super().__init__(dimMagnitud, compuesto, magnitud, cifrasSig, teorico, moles) #Llamar al constructor de la clase padre
        self._Densidad = densidad #Agregar atributo densidad
        self._Dimensional = {"Magnitud": dimMagnitud, "Densidad": dimDensidad} #Actualizar atributo dimensional: Diccionario con las dimensionales de la magnitud y la densidad
        if self._Compuesto.elementoPuro(): #Evaluar si el compuesto es un elemento puro
            print("true")
            self._Densidad = self._Compuesto.getElementos()[0].getDensidad() #Si lo es, encontrar la densidad del elemento
        self._PuntoPartida = not(magnitud==None) and not(densidad==None) #Actualizar punto partida: Verdadero si se tiene la magnitud y la densidad
        self._CifrasSig = [self._CifrasSig, Liquido.cifrasSignificativas(densidad)] #Añadir las cifras significativas de la densidad
        
    def elementoPuro(self):
        return self._Compuesto.elementoPuro()
    
    def densidadElementoPuro(self):
        return self._Compuesto.getElementos()[0].getDensidad()
    
    def SI(self):
        super().SI() #Proceso general para convertir la magnitud
        self._Densidad = self.C.aSI(self._Densidad,self._Dimensional["Densidad"]) #Convertir la densidad a las unidades estándar del SI
        self._Dimensional["Magnitud"] = self.C.dimensionalSI(self._Dimensional["Densidad"]) #Actualizar la dimensional de la densiddad
        return self._Magnitud #Devolver la nueva magnitud 
    
    def aMasa(self):
        if self._Magnitud == None: #Si falta la magnitud (pero se tienen los moles)
            masa = Masa(compuesto = self._Compuesto, moles = self._Moles) #Crear un objeto masa con los moles
            masa.getIncognita() #Encontrar la masa con getIncognita
            return masa #devolver el objeto masa
        else: #Si se tiene la magnitud
            self.SI() #Estandarizar
            masa = self._Magnitud*self._Densidad #Convertir a masa (g) como magnitud (L) * densidad (g/L)
            return Masa(compuesto=self._Compuesto, magnitud=masa,cifrasSig=min(self._CifrasSig)) #Devolver un objeto tipo masa con los atributos correspondientes 
    
    #Override
    def aMoles(self):
        masa = self.aMasa() #Convertir a masa con el método aMasa
        self._Moles = masa.aMoles().getMoles() #Usar el método aMoles del objeto masa, actualizar atributo Moles
        return super().aMoles() #Devolver el objeto moles
        
    #Override 
    def getIncognita(self, moles: float = None):
        def getOtrasIncognitas():
            masa = self.aMasa().getMagnitud() #Encotrar la masa (g) con el método aMasa
            if self._Magnitud == None: #Si falta la magnitud
                densidadEstandar = self.C.aSI(self._Densidad,self._Dimensional["Densidad"]) #Convertir la densidad a las unidades estándar del SI
                mag = masa/densidadEstandar #Encontrar magnitud (L) como masa (g) / densidad (g/L)
                self._Magnitud = self.C.convert(mag, self._Dimensional["Magnitud"]) #Convertir el volumen encontrado a la unidad del dato. Actualizar magnitud
                return self._Magnitud #Devolver magnitud
            if self._Densidad == None: #Si falta la densidad
                super().SI() #Estandarizar la magnitud
                dens = masa/self._Magnitud #Encontrar la densidad (g/L) como masa(g) / magnitud (L)
                self._Densidad = self.C.convert(dens, self._Dimensional["Densidad"]) #Convertir la densidad encontrada a la unidad del dato. Actualizar densidad
                return self._Densidad
        return super().getIncognita(getOtrasIncognitas, moles=moles) #Hacer el proceso general + el proceso "getOtrasIncognitas"
       
    #Override
    def __str__(self):
        info = super().__str__() + f", Densidad: {self._Densidad}"
        return info