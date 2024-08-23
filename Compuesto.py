import pandas as pd

class Compuesto:
    #Constructor
    def __init__(self, compuesto, coheficiente=1):
                self.compuesto = compuesto #String con la fórmula del compuesto
                self.coheficiente = float(coheficiente) #Coeficiente estequimétrico si es parte de una reacción, 1 por default 

    #Devuelve un dataframe de qué elementos forman el compuesto y cuántos átomos de cada elemento tiene
    def getElementos(self):
        #Listas de las divisiones y coheficientes hasta ese punto
        div1 = [self.compuesto]
        coefs1 = [1]
        #Sub funcion para subdividir en base a *, () o []. Sep es el separador, y div1 y coefs1 las listas hasta ahora
        def dividir(sep,div1,coefs1):
            #Listas para trabajar las divisiones
            div2 = []
            coefs2 = []
            for x in range(len(div1)): #Por cada bloque en la lista anterior de divisiones 
                new = div1[x].split(sep) #Crear una nueva lista con las divisiones del bloque según el separador
                for i in range(len(new)): #Por cada nuevo string (nuevo bloque) que resultó de la división:
                    if sep == "*": #Si el separador es *
                        if new[i][0].isdigit(): #Si el primer caracter es un número, extraerlo como coheficiente del bloque
                            coefs2.append(int(new[i][0]))
                            new[i] = new[i][0:]
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
                        co = int(simb[-1])*coefs[x] #Extraerlo, multiplicarlo por el coheficiente anterior y añadirlo como el nuevo coheficiente
                        simb = simb[:-1] 
                        coefs2.append(co)
                    else:
                        coefs2.append(coefs[x]) #Si no hay coheficiente mantener el anterior
                    el.append(simb) #Añadir el símbolo del elemento a la lista de elementos
        elementos = pd.DataFrame({"Elementos":el, "Coheficientes": coefs2}) #Crear un dataframe con las dos listas como columnas
        elementos = elementos.groupby('Elementos', as_index=False).sum() #Si hay elementos duplicados, sumarlos y dejar una sola fila
    
        return elementos #Devolver el dataframe

y = Compuesto("H3COOH2Na")
print(y.getElementos())
