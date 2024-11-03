from Estequiometria.Moles import Moles
from Estequiometria.TipoDato import TipoDato

class Gas(TipoDato):
    def __init__(self, compuesto, magnitud: float = None, dimVolumen: str = "L", temperatura: float = None, dimTemperatura: str = "C", presion: float = None, dimPresion: str = "atm", cifrasSig=None, teorico: bool = True, moles: float = None):
        super().__init__(dimVolumen, compuesto, magnitud, cifrasSig, teorico, moles) #Llamar al constructor de la clase padre
        self._Dimensional = {"Magnitud": dimVolumen, "Temperatura": dimTemperatura,  "Presion": dimPresion} #Actualizar las dimnesionales a un diccionario
        if isinstance(temperatura, str): #Si se pasa la temperatura como un string
            #Calcular las cifras significativas usando el método estático, asignar en el diccionario
            self._CifrasSig["Temperatura"] = TipoDato.CifrasSig(temperatura)
            temperatura = float(temperatura) #Covertir la temperatura a float
        self._Temperatura = temperatura
        if isinstance(presion, str): #Si se pasa la presion como un string
            #Calcular las cifras significativas usando el método estático, asignar en el diccionario
            self._CifrasSig["Presion"] = TipoDato.CifrasSig(presion)
            presion = float(presion) #Covertir la presion a float
        self._Presion = presion
        self.Atributos.extend([self._Temperatura, self._Presion]) #Añadir los atributos presion y temperatura a la lista de atributos
        self._PuntoPartida = not(magnitud==None) and not(temperatura==None) and  not(presion==None) #Si alguno de los atributos no está vacío
    
    def CifrasSigTemp(self,decimalesAntes):
        cantDecimales = min(decimalesAntes,2) #Calcular la cantidad de decimales que debe tener la temperatura
        return len(str(int(self._Temperatura))) + cantDecimales #Devolver la cantidad de enteros más la de decimales
       
    #Override 
    def SI(self):
        if not(self._Magnitud == None): super().SI() #Proceso general para convertir la magnitud (volumen)
        if not(self._Presion == None): 
            self._Presion = self.C.aSI(self._Presion,self._Dimensional["Presion"]) #Convertir la presion a atm
            if self._PuntoPartida: self._Dimensional["Presion"] = self.C.dimensionalSI(self._Dimensional["Presion"]) #Actualizar las dimensionales
        if not(self._Temperatura == None):
            decimalesAntes = TipoDato.cantDecimales(self._Temperatura,self._CifrasSig["Temperatura"]) if self._CifrasSig != None else 0 #Guardar la cantidad de decimales original
            self._Temperatura = self.C.aSI(self._Temperatura,self._Dimensional["Temperatura"]) #Convertir la temperatura a Kelvin
            if self._PuntoPartida: self._Dimensional["Temperatura"] = self.C.dimensionalSI(self._Dimensional["Temperatura"]) #Actualizar las dimensionales
            self._CifrasSig["Temperatura"] = self.CifrasSigTemp(decimalesAntes) if  self._CifrasSig != None else None #Actualizar las cifras significativas de la temperatura
        return self._Magnitud #Devolver la nueva magnitud 
        
    #Override
    def aMoles(self):
        R = 0.08205746  #Constante de gas ideal  en L atm/mol K
        #PV = nRT ->  n = PV/RT
        if self._PuntoPartida:
            self.SI() #Estandarizar
            self._Moles = (self._Presion * self._Magnitud) / (R * self._Temperatura) #Convertir utilizando la ecuación de los gases ideales
        return super().aMoles()
    
    #Override
    def getIncognita(self, moles: Moles = None):
        R = 0.08205746  #Constante de gas ideal  en L atm/mol K
        #PV = nRT ->  V =  nRT/P,  T = nR/PV, P = nRT/V
        def getOtrasIncognitas():
            self.SI() #Estandarizar
            def convert(volumen=self._Magnitud, presion=self._Presion,temp = self._Temperatura):
                #Convertir a las dimensionales del dato
                self._Magnitud = self.C.convert(volumen, self._Dimensional["Magnitud"]) 
                self._Presion = self.C.convert(presion, self._Dimensional["Presion"])
                self._Temperatura = self.C.convert(temp, self._Dimensional["Temperatura"]) 
            if self._Magnitud == None: #Si falta el volumen
                volumen = self._Moles*R*self._Temperatura/self._Presion #Encontrar con la ecuación de los gases ideales
                convert(volumen=volumen)
                return self._Magnitud
            if self._Presion == None: #Si falta la presion
                presion = self._Moles*R*self._Temperatura/self._Magnitud #Encontrar con la ecuación de los gases ideales
                convert(presion=presion)
                return self._Presion
            if self._Temperatura == None: #Si falta la temperatura
                temp = self._Moles*R/self._Magnitud/self._Presion #Encontrar con la ecuación de los gases ideales
                convert(temp=temp)
                return  self._Temperatura
        return super().getIncognita(getOtrasIncognitas, moles)
   
    #Override
    def __str__(self):
        info = super().__str__() + f", a {self._Temperatura} {self._Dimensional["Temperatura"]} y {self._Presion} {self._Dimensional["Presion"]}"
        return info
    
    def getTemperatura(self):
        return self._Temperatura
    
    def setTemperatura(self,  temperatura):
        self._Temperatura = temperatura
    
    def getPresion(self):
        return  self._Presion
    
    def setPresion(self, presion):
        self._Presion = presion
