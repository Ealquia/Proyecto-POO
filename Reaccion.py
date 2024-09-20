import chempy as ch
import numpy as np
from Compuesto import Compuesto

class Reaccion:
    def __init__(self, reaccionString): # la variable reaccion es un string que describe la reacción
        self.reaccionString = reaccionString
        self.reactivos = self.getReactivosComp()
        self.productos = self.getProductosComp()

    #función para obtener los reactivos como objetos tipo Compuesto
    def getReactivosComp(self):
        #Lista compuesta por dos elementos, reactivos y productos como un string. 
        list1 = self.reaccionString.replace(" ","").split("=")  #replace elimina los espacios en blanco y split divide los reactivos y productos en dos strings distintos
        react, products = dividir(list1) #se obtiene las listas de reactivos y productos

        reactivos=[] #lista donde se almacenaran los reactivos como objetos
        for x in react:
            #Para cada reactivo se crea un objeto tipo compuesto y se almacena en la lista
            reactivos.append(Compuesto(x))

        return reactivos #devuelve la lista de reactivos como objetos

    #función para obtener los reactivos como strings, esto para poder manejarlos con mayor facilidad al momento de balancear la reacción con la librería chempy
    def getReactivosString(self): 
        list1 = self.reaccionString.replace(" ","").split("=") # se separan los reactivos y productos en dos strings distintitos 
        react, produ = dividir(list1)
        return react

    def getProductosComp(self):
        #Lista compuesta por dos elementos, reactivos y productos como un string. 

        list1 = self.reaccionString.replace(" ","").split("=") 
        react, products = dividir(list1)

        productos=[]
        for x in products:
            productos.append(Compuesto(x))

        return productos

    def getProductosString(self):
        list1 = self.reaccionString.replace(" ","").split("=")
        
        react, produ = dividir(list1)
        return produ

    def Balancear(self):
        reactants = set(self.getReactivosString())
        products = set(self.getProductosString())
        react, produ = ch.balance_stoichiometry(reactants= reactants, products= products)
        return ch.Reaction(reac=react, prod=produ).string()

#Métodos estáticos ===============================================================================================================================

def dividir(list1):
            reactivos =list1[0].split("+")# se separa cada reactivo en un nuevo string
            productos = list1[1].split("+")# se separa cada producto en un nuevo string
            return reactivos, productos # de vuelve la lista de los strings de reactivos y productos 

