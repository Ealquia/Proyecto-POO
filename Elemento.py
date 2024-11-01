import pandas as pd
import os 

class Elemento:
    try:
        ruta_relativa = 'Periodic Table of Elements.csv'  # Ruta relativa al archivo
        ruta_absoluta = os.path.join(os.path.dirname(__file__), ruta_relativa)
        elementos_df = pd.read_csv(ruta_absoluta)
    except FileNotFoundError:
        raise FileNotFoundError("El archivo de la tabla periódica no se encontró.")

    def __init__(self, simbolo, cant=1):
        simbolo = simbolo.strip()
        elemento_info = Elemento.elementos_df[Elemento.elementos_df['Symbol'] == simbolo]
        
        if not elemento_info.empty:
            # Asigna los atributos al elemento
            self.elemento = elemento_info['Element'].values[0]
            self.cant = cant
            self.masa_molar = elemento_info['AtomicMass'].values[0]
            self.densidad = elemento_info['Density'].values[0]
            self.nombre = elemento_info['Element'].values[0]
            self.otros = elemento_info.to_dict(orient='records')[0] 
        else:
            raise ValueError(f"El elemento con símbolo '{simbolo}' no fue encontrado en la tabla periódica.")

    def getElemento(self):
        return self.elemento

    def getCant(self):
        return self.cant

    def setCant(self, value):
        self.cant = value

    def getMasaMolar(self):
        return self.masa_molar

    def getDensidad(self):
        return self.densidad

    def toString(self):
        return f"Elemento: {self.nombre}, Masa Molar: {self.masa_molar}, Densidad: {self.densidad}, Otros: {self.otros}"

    @classmethod
    def iniciar_interaccion(cls):
        seguir = True
        while seguir:
            simbolo = input("Introduce el símbolo del elemento (o escribe 'salir' para terminar): ")
            if simbolo.lower() == 'salir':
                seguir = False
                print("Saliendo del programa...")
            else:
                try:
                    elemento = cls(simbolo)
                    print(elemento.toString())
                except ValueError as e:
                    print(e)
