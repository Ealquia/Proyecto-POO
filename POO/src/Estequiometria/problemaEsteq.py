from Estequiometria.Moles import Moles
from Estequiometria.TipoDato import TipoDato
from Reaccion import Reaccion
import copy

class problemaEsteq:
    tipos = ["Masa", "Volumen de solución", "Volumen de líquido","Volumen de gas","Molaridad","Presión de un gas",
             "Temperatura de un gas","Calor de la reacción", "Entalpía de la reacción", "Entalpía molar", 
             "Cantidad de materia", "Porcentaje de rendimiento"]
    tiposDatos = ["Masa", "Volumen de solución", "Volumen de líquido","Volumen de gas","Cantidad de materia", "Calor de una reacción"]
    
    def  __init__(self, Datos, Incognita = None, reaccion = None, compuesto = None, tipo = None, Rendimiento: float =  100):
        self.__Datos = [] #Crear una lista vacía de datos
        self.__Datos.extend(Datos) #Añadir los datos pasados como parámetro
        self.__Incognita = Incognita
        self.__TipoIncognita = tipo
        if isinstance(reaccion, str):
            reaccion = Reaccion(reaccion)
        self.__Compuesto = compuesto
        if compuesto==None:
            if reaccion==None:
                self.__Compuesto = Datos[0].getCompuesto()
            else:
                self.__Compuesto = Incognita.getCompuesto()
        self.__Reaccion = reaccion
        self.__Rendimiento = Rendimiento
        self.__Respuesta = None
        self.__CifrasSig = []

    def Respuesta(self):
        if self.__Respuesta == None: self.Resolver()
        for i in range(12):
            if self.__TipoIncognita  == problemaEsteq.tipos[i]: 
                tipo = i 
                i = 13
        compuesto = self.__Incognita.getCompuesto().getCompuesto()
        respuesta = self.conCifrasSig()
        D = self.__Incognita.getDimensional()
        if tipo >= 0 and tipo <= 3: respuesta = f"{respuesta} {D["Magnitud"]} de {compuesto}"
        if tipo == 4: respuesta = f"Solución de {compuesto} {respuesta} Molar"
        if tipo == 5: respuesta = f"La presión del gas {compuesto} es {respuesta} {D["Presion"]}"
        if tipo == 6: respuesta = f"La temperatura del gas {compuesto} es {respuesta} {D["Temperatura"]}"
        if tipo == 7:
            direccion =  "liberan" if self.__Respuesta < 0 else "absorben"
            respuesta  = f"Se {direccion} {respuesta} {D["Magnitud"]} durante la reacción"
        if tipo == 8:  respuesta = f"La entalpía de la reacción es {respuesta}  {D["Entalpia"]}"
        if tipo == 9:   respuesta = f"La entalpía molar del {compuesto} es {respuesta}  {D["Entalpia"]}/mol"
        if tipo == 10: 
            if D != "particulas":
                respuesta = f"{respuesta} {D} de {compuesto}"
            else:
                particulas = "átomos" if self.__Compuesto.elementoPuro() and self.__Compuesto.getElementos()[0].getCant == 1 else "moléculas"
                respuesta = f"{respuesta}  {particulas} de {compuesto}"
        if tipo == 11: respuesta = f"El rendimiento es del {respuesta}%"
        return respuesta

    def CifrasSig(self,datos):
        for dato in datos:
            self.__CifrasSig.extend(list(dato.getCifrasSig().values())) if dato.getCifrasSig() != None else None

    def conCifrasSig(self):
        if  self.__CifrasSig != []:
            cifras = min(self.__CifrasSig) #Encontrar el número de cifras significativas
            respuestaCS = f"{abs(self.__Respuesta):.{cifras-1}e}" #Expresar en notación científica con las cifras correctas
            return respuestaCS
        else:
            return str(self.__Respuesta)

    def Resolver(self):
        tipo = self.TipoProblema()  
        if tipo=="deCosaACosa" or tipo=="unaCosa": #Si el problema es simple
            respuesta = self.deCosaACosa()
            self.CifrasSig([self.__Datos[0],self.__Incognita]) #Añadir las cifras significativas de los datos usados
        if tipo== "reactivoLimitante":
            reactLimitante = self.reactivoLimitante()
            respuesta = self.deCosaACosa(de=reactLimitante)
            self.CifrasSig([self.__Datos[reactLimitante],self.__Incognita])  #Añadir las cifras significativas de los datos usados
        if tipo=="porcentajeRendimiento":
            respuesta = self.porcentajeRendimiento()
        else:
            if tipo != "unaCosa":
                compuesto = self.__Incognita.getCompuesto().getCompuesto()
                respuesta = respuesta * self.__Rendimiento / 100 if self.__Reaccion.esProducto(compuesto) else  respuesta * 100 / self.__Rendimiento 
        self.__Respuesta = respuesta
        return respuesta

    def TipoProblema(self):
        if self.__Reaccion ==None:  
            return "unaCosa" #Hay un compuesto y la conversión es entre el mismo compuesto
        else:
            if len(self.__Datos)==1 and not(self.__Incognita==None): 
                return "deCosaACosa"  #Hay un solo dato, una incógnita y una reacción, es un problema de esequiometría simple
        if len(self.__Datos)>1  and not(self.__Incognita==None):
            return "reactivoLimitante" #Hay más de un dato, una incógnita y una reacción, es un problema de reactivo limitante
        if self.__TipoIncognita == "Porcentaje de Rendimiento": #Hay más de un dato y no hay incógnita 
            return "porcentajeRendimiento"

    def deCosaACosa(self, de=0, a=None):
        de = self.__Datos[de] #Obtener el dato de la lista de datos (el primer dato es el default)
        if (a==None): a = self.__Incognita #Si no se pasa parámetro "a" se asume que es la incógnita
        moles1 = de.aMoles() if type(de) != Moles else de #Convertir el primer dato a moles
        moles2 = moles1.aMolesDe(self.__Reaccion, a.getCompuesto()) if not(self.TipoProblema()=="unaCosa") else moles1 
        #Convertir a moles del segundo compuesto (a menos que no haya reacción, en cuyo caso mantener los moles obtenidos antes)
        #Encontrar el valor de la incógnita 
        respuesta = a.getIncognita(moles2)
        return respuesta
    
    def reactivoLimitante(self, datos=None):
        if  datos==None: datos = self.__Datos #Si no se pasa lista de datos se asume  que es la lista de datos del problema
        valorCritico = 0
        compuesto = self.__Incognita.getCompuesto()
        for i  in range(len(self.__Datos)): #Por cada dato en la lista
            if self.__Datos[i]._PuntoPartida: #Si el dato es un punto de partida válido, 
                moles1 =  self.__Datos[i].aMoles() #Convertir el dato a moles
                moles2 = moles1.aMolesDe(self.__Reaccion,compuesto).getMoles()
                if i == 0: valorCritico = moles2 #Si es el primer dato, asignar el resultado a valor crítico
                if moles2 <= valorCritico: #Si el resultado es menor al valor crítico, cambiar el valor crítico
                    valorCritico = moles2
                    reactivoLimitante = i #Asignar el dato correspondiente al reactivo limitante
        return reactivoLimitante #Devolver el reactivo limitante
    
    def porcentajeRendimiento(self):
        for dato in self.__Datos: #Recorrer la lista de datos
            if not dato.getTeorico(): #Si se encuentra el dato real
                self.__Incognita = copy.deepcopy(dato) #Asignar a la incógnita una copia del dato real
                self.__Incognita.setMagnitud(None) #Quitarle la magnitud a la incógnita
                self.__Datos.remove(dato) #Quitar el dato teórico de los datos
                real = dato  #Asignar el dato real a la variable real
                break #Terminar el for
        RL = self.reactivoLimitante() if len(self.__Datos) > 1 else 0  #Encontrar el reactivo limitante 
        teorico = self.deCosaACosa(de=RL) #Encontrar el dato teorico
        self.CifrasSig([self.__Datos[RL],real]) #Añadir las cifras significativas de los datos usados
        rendimiento = 100*real.getMagnitud()/teorico #Encontrar el porcentaje de rendimiento
        return rendimiento #Devolver el porcentaje de rendimiento

