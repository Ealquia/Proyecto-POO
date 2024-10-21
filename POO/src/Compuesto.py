# -*- coding: utf-8 -*-
import pandas as pd
from Elemento import Elemento 

class Compuesto:
    #Constructor
    def __init__(self, compuesto, coheficiente=1):
                self.__Compuesto = compuesto #String con la fórmula del compuesto
                self.__Coeficiente = float(coheficiente) #Coeficiente estequimétrico si es parte de una reacción, 1 por default 
                self.__Elementos = []

    #Devuelve un dataframe con los símbolos de los elementos del compuesto y la cantidad de cada uno
    def DFElementos(self):
        #Listas de las divisiones y coheficientes hasta ese punto
        div1 = [self.__Compuesto]
        coefs1 = [1]
        #Sub funcion para subdividir en base a *, () o []. Sep es el separador, y div1 y coefs1 las listas hasta ahora
        def dividir(sep,div1,coefs1):
            #Listas para trabajar las divisiones
            div2 = []
            coefs2 = []
            for x in range(len(div1)): #Por cada bloque en la lista anterior de divisiones 
                #Crear una nueva lista con las divisiones del bloque según el separador, y asegurarse de no incluir strings vacíos
                new = [elemento for elemento in div1[x].split(sep) if elemento != '']
                for i in range(len(new)): #Por cada nuevo string (nuevo bloque) que resultó de la división:
                    if sep == "*": #Si el separador es *
                        if new[i][0].isdigit(): #Si el primer caracter es un número
                            coef = new[i][0] #Extraerlo
                            if len(new[i])>1 and new[i][1].isdigit(): #Verificar si el siguiente caracter también es un número
                                coef = coef + new[i][1]
                                new[i] = new[i][1:] #Eliminar los dos dígitos de la cadena
                            else:
                                new[i] = new[i][0:] #Eliminar el númúnico dígito de la cadena
                            coefs2.append(int(coef)) #Añadir el coeficiente a la lista 
                        else:
                            coefs2.append(1) #Si no, el coheficiente es 1
                    else: #Si el separador es ( o [ el fin del bloque será ) o ] respectivamente
                        if sep == "(":
                            fin = ")"
                        if sep == "[":
                            fin = "]"
                        if new[i][-1].isdigit() and new[i][-2] == fin: #Si el último caracter es un número y el penúltimo el cierre respectivo:
                            coefs2.append(int(new[i][-1])*coefs1[x]) #Extraerlo y multiplicarlo por el coheficiente anterior en la jerarquía para obtener el nueve coheficiente
                            new[i] = new[i][:-1]
                        else:
                            coefs2.append(coefs1[x]) #Si no, mantener el coheficiente anterior
                        new[i] = new[i].replace(fin, '') #Eliminar el ] o el )
                div2 = div2 + new #Concatenar la lista de trabajo a la resultante
            return div2, coefs2 #Devolver las listas resultantes de bloques y coheficientes

        #Hacer el proceso de división 3 veces, con cada separador, reemplazando las listas actuales con las resultantes del proceso anterior
        div1, coefs1 = dividir("*",div1, coefs1)
        div1, coefs1 = dividir("[",div1, coefs1)
        iones, coefs = dividir("(",div1, coefs1)
        #Crear las listas que tendrán los datos finales
        el = []
        coefs2 = []
        for x in range(len(iones)): #Por cada elemento (bloque) en la lista de las últimas divisiones:
            cut = None 
            for i in range(len(iones[x])): #Este proceso se repite cuantas veces como caracteres tenga el elemento:
                if iones[x][-(i+1)].isupper(): #Si el caracter encontrado de atrás hacia adelante es una mayúscula:
                    simb = iones[x][-(i+1):cut] #Se guarda la sección de la cadena desde la mayúscula hasta el punto de corte en una nueva variable 
                    cut = -(i+1) #El punto de corte es el final de la cadena la primera vez, y la última mayúscula el resto de veces
                    if simb[-1].isdigit(): #Si el último caracter de la subcadena es un número:
                        co = simb[-1]
                        simb = simb[:-1] #Quitar el número
                        if simb[-1].isdigit(): #Verificar si el siguiente caracter también es un número
                            co = simb[-1] + co #Añadirlo al coeficiente
                            simb = simb[:-1] #Quitar el otro dígito
                        coefs2.append(int(co)*coefs[x]) #Convertir coeficiente a entero, multiplicarlo por el coheficiente anterior y añadirlo como el nuevo coheficiente      
                    else:
                        coefs2.append(coefs[x]) #Si no hay coheficiente mantener el anterior
                    el.append(simb) #Añadir el símbolo del elemento a la lista de elementos
        elementos = pd.DataFrame({"Elementos":el, "Coeficientes": coefs2}) #Crear un dataframe con las dos listas como columnas
        elementos = elementos.groupby('Elementos', as_index=False).sum() #Si hay elementos duplicados, sumarlos y dejar una sola fila
    
        return elementos #Devolver el dataframe
        
    #Devuelve una lista de objetos elemento de los elementos que forman el compuesto 
    #El atributo cant de cada objeto representa cuántos átomos del elemento hay en el compuesto
    def getElementos(self):
        if self.__Elementos == []:
            for row in self.DFElementos().itertuples(index=True):
                self.__Elementos.append(Elemento(row.Elementos, row.Coeficientes))
        return self.__Elementos

    #Devuelve la masa molar
    def masaMolar(self):
        masaMolar = 0
        for elemento in self.getElementos(): #Por cada elemento del compuesto
            masaMolar = masaMolar + elemento.masa_molar*elemento.cant #Se multiplica la masa molar por la cantidad y se suma
        return masaMolar
    
    #Verdadero si el compuesto es un solo elemento
    def elementoPuro(self):
        return len(self.getElementos())==1

    #Sets y gets
    def getCompuesto(self):
        return self.__Compuesto

    def getCoeficiente(self):
        return self.__Coeficiente
    
    def setCoeficiente(self,nuevoCoef):
        self.__Coeficiente = nuevoCoef