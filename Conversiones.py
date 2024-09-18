import pandas as pd

class Conversiones:
    def __init__(self):
        self.tabla = pd.read_csv('TablaConversiones.csv', sep=";")

    #Convierte cualquier unidad a su equivalente en el SI definido como estándar
    #Valor: valor numérico a convertir
    #dimensional: unidad de medida que se desea convertir al SI estándar
    def aSI(self, valor, dimensional):
        def convert(valor, dimensional):
            estandar = self.tabla[self.tabla['Simbolo'] == dimensional].reset_index().at[0, "Estandarizar"]
            return valor*estandar
        if self.tabla[self.tabla['Simbolo'] == dimensional].reset_index().at[0, "Tipo"] == "Densidad":
            dims = dimensional.split("/")
            return convert(valor,dims[0])/convert(1,dims[1])
        else:
            return convert(valor, dimensional)

    #Convierte un valor en unidades estándar a una unidad no estándar
    #Valor: valor numérico a convertir
    #Dimensional: unidad de medida a la que se desea convertir 
    def convert(self, valor, dimensional):
        def convert(valor, dimensional):
            estandar = self.tabla[self.tabla['Simbolo'] == dimensional].reset_index().at[0, "Estandarizar"]
            return valor/estandar
        if self.tabla[self.tabla['Simbolo'] == dimensional].reset_index().at[0, "Tipo"] == "Densidad":
            dims = dimensional.split("/")
            return convert(valor,dims[0])/convert(1,dims[1])
        else:
            return convert(valor, dimensional)
    
x = Conversiones()
print(x.convert(43.5,"kg/L"))