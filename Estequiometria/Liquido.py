from Estequiometria.TipoDato import TipoDato
from Estequiometria.Masa import Masa
from Estequiometria.Moles import Moles

class Liquido(TipoDato):
    #Constructor
    def __init__(self, compuesto, dimMagnitud: str="L", dimDensidad: str = "g/L", magnitud: float = None, densidad:float = None, cifrasSig = None, teorico: bool = True, moles: float = None):
        super().__init__(dimMagnitud, compuesto, magnitud, cifrasSig, teorico, moles) #Llamar al constructor de la clase padre
        self._Densidad = densidad #Agregar atributo densidad
        self._Dimensional = {"Magnitud": dimMagnitud, "Densidad": dimDensidad} #Actualizar atributo dimensional: Diccionario con las dimensionales de la magnitud y la densidad
        if self._Compuesto.elementoPuro(): #Evaluar si el compuesto es un elemento puro
            self._Densidad = self._Compuesto.getElementos()[0].getDensidad() #Si lo es, encontrar la densidad del elemento
            self._Dimensional["Densidad"] = "g/mL" #Actualizar la dimensional de la densidad (las densidades de los elementos están en g/mL)
        self._PuntoPartida = not(magnitud==None) and not(densidad==None) #Actualizar punto partida: Verdadero si se tiene la magnitud y la densidad
        self.Atributos.append(self._Densidad) #Añadir el atributo  densidad a la lista de atributos
        self._CifrasSig = [self._CifrasSig, Liquido.cifrasSignificativas(densidad)] #Añadir las cifras significativas de la densidad

    def elementoPuro(self):
        return self._Compuesto.elementoPuro()
    
    def densidadElementoPuro(self):
        return self._Compuesto.getElementos()[0].getDensidad()
    
    def SI(self):
        super().SI() #Proceso general para convertir la magnitud
        self._Densidad = self.C.aSI(self._Densidad,self._Dimensional["Densidad"]) #Convertir la densidad a las unidades estándar del SI
        self._Dimensional["Densidad"] = self.C.dimensionalSI(self._Dimensional["Densidad"]) #Actualizar la dimensional de la densiddad
        return self._Magnitud #Devolver la nueva magnitud 
    
    def aMasa(self, dims = "g"):
        if self._Magnitud == None: #Si falta la magnitud (pero se tienen los moles)
            masa = Masa(compuesto = self._Compuesto, moles = self._Moles, dimensional = dims) #Crear un objeto masa con los moles
            masa.getIncognita() #Encontrar la masa con getIncognita
            return masa #devolver el objeto masa
        else: #Si se tiene la magnitud
            self.SI() #Estandarizar
            masa = self._Magnitud*self._Densidad #Convertir a masa (g) como magnitud (L) * densidad (g/L)
            masa = Masa(compuesto=self._Compuesto, magnitud=masa,dimensional=dims, cifrasSig=min(self._CifrasSig)) #Crear un objeto tipo masa con los atributos correspondientes 
            masa.getIncognita()
            return masa
    
    #Override
    def aMoles(self):
        if self._PuntoPartida:
            masa = self.aMasa() #Convertir a masa con el método aMasa
            self._Moles = masa.aMoles().getMoles() #Usar el método aMoles del objeto masa, actualizar atributo Moles
            return super().aMoles() #Devolver el objeto moles
        else:
            raise  ValueError("No se puede convertir a moles si no se tiene la magnitud o la densidad")
    
    #Override 
    def getIncognita(self, moles: Moles = None):
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
        return super().getIncognita(getOtrasIncognitas, moles) #Hacer el proceso general + el proceso "getOtrasIncognitas"
       
    #Override
    def __str__(self):
        info = super().__str__() + f", Densidad: {self._Densidad} {self._Dimensional["Densidad"]}"
        return info