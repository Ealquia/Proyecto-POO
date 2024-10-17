import chempy as ch
import numpy as np
from Compuesto import Compuesto

class Reaccion:
    def __init__(self, reaccionString): # la variable reaccion es un string que describe la reacción
        self.reaccionString = reaccionString
        self.reactivos = self.ObtenerReactivosComp()
        self.productos = self.ObtenerProductosComp()

    def getReactivos(self):
        return self.reactivos
    def getProductos(self):
        return self.productos

    #función para obtener los reactivos como objetos tipo Compuesto
    def ObtenerReactivosComp(self):
        #Lista compuesta por dos elementos, reactivos y productos como un string. 
        list1 = self.reaccionString.replace(" ","").split("=")  #replace elimina los espacios en blanco y split divide los reactivos y productos en dos strings distintos
        react, products = dividir(list1) #se obtiene las listas de reactivos y productos
        reactivos=[] #lista donde se almacenaran los reactivos como objetos
        react.sort()
        for x in react:
            #Para cada reactivo se crea un objeto tipo compuesto y se almacena en la lista
            reactivos.append(Compuesto(x))

        return reactivos #devuelve la lista de reactivos como objetos

    #función para obtener los reactivos como strings, esto para poder manejarlos con mayor facilidad al momento de balancear la reacción con la librería chempy
    def ObtenerReactivosString(self): 
        list1 = self.reaccionString.replace(" ","").split("=") # se separan los reactivos y productos en dos strings distintitos 
        react, produ = dividir(list1) #se realiza la separación de reactivos y productos
        return react #de vuelve la lista de reactivos como strings

    def ObtenerProductosComp(self):
        #Lista compuesta por dos elementos, reactivos y productos como un string. 

        list1 = self.reaccionString.replace(" ","").split("=") 
        react, products = dividir(list1)
        products.sort()

        productos=[]
        for x in products:
            #Para cada producto se crea un objeto tipo compuesto y se almacena en la lista
            productos.append(Compuesto(x))

        return productos # de vuelve la lista de productos como objetos

    def ObtenerProductosString(self):
        list1 = self.reaccionString.replace(" ","").split("=")
        
        react, produ = dividir(list1)
        return produ

    #Función para balancear la reacción
    def Balancear(self):
        reactants = sorted(set(self.ObtenerReactivosString())) # se obtienen los reactivos
        products = sorted(set(self.ObtenerProductosString())) # se obtienen los productos
        react, produ = ch.balance_stoichiometry(reactants= reactants, products= products) # con la librería chempy se balancea
        #listas para almacenar los coeficientes
        coefreac =[]
        coefprodu = []

        #se extrae el valor de los coeficientes de cada reactivo
        for valor in react.values():
            coefreac.append(valor) # se almacenan en su respectiva lista
        
        #se extrae el valor de los coeficientes de cada reactivo
        for valor in produ.values():
            coefprodu.append(valor) # se almacena en su respectiva lista

        #Se actualiza el valor de los coeficientes en cada atributo de cada objeto
        i1=0
        for x in self.reactivos: #obtiene cada reactivo como objeto
            x.setCoeficiente(coefreac[i1]) # actualiza los coeficientes de cada reactivo
            i1 = i1+1
        i2=0
        for x in self.productos: # obtiene cada producto como objeto
            x.setCoeficiente(coefprodu[i2]) #actualiza los coeficientes de cada producto
            i2= i2+1

        return ch.Reaction(reac=react, prod=produ).string() # usando la librería chempy se retorna la reacción ya balanceada

    #Método que devuelve el reactivo o producto cuya fórmula es la pasada como parámetro
    def getCompuesto(self, formula:str):
        found = False
        for compuesto in self.reactivos: #Buscar entre los reactivos
            if compuesto.getCompuesto() == formula: #Si se encuentra, devolverlo
                found = True
                return compuesto 
        if not(found): #Si no se encuentra  entre los reactivos, buscar entre los productos
            for compuesto  in self.productos:  
                if compuesto.getCompuesto() == formula:  #Si se encuentra, devolverlo
                    found = True
                    return compuesto 
        if not(found): 
            raise ValueError("El compuesto no se encuentra en la reacción") #Si no se encuentra, lanzar excepción 

        



#Métodos estáticos ===============================================================================================================================

def dividir(list1): # sirve para separar cada compuesto
            reactivos =list1[0].split("+")# se separa cada reactivo en un nuevo string
            productos = list1[1].split("+")# se separa cada producto en un nuevo string
            return reactivos, productos # de vuelve la lista de los strings de reactivos y productos 
 