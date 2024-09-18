import pandas as pd

class Elemento:
    # Cargar el CSV de los elementos en un DataFrame (atributo estático de la clase)
    elementos_df = pd.read_csv(r'C:/Users/isaac/Downloads/tabla CSV/c2dd862cd38f21b0ad36b8f96b4bf1ee-1d92663004489a5b6926e944c1b3d9ec5c40900e/Periodic Table of Elements.csv')

    def __init__(self, simbolo):
        # Buscamos el elemento en el dataframe
        elemento_info = self.elementos_df[self.elementos_df['Symbol'] == simbolo]
        
        if not elemento_info.empty:
            # Asigna los atributos al elemento
            self.elemento = elemento_info['Element'].values[0]
            self.cant = 0  # Cantidad inicial (puede modificarse)
            self.masa_molar = elemento_info['AtomicMass'].values[0]
            self.densidad = elemento_info['Density'].values[0]
            self.nombre = elemento_info['Element'].values[0]
            self.otros = elemento_info.to_dict(orient='records')[0]  # Guarda otros datos como diccionario
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
        # Devuelve una lista cono toda la informacion
        return f"Elemento: {self.nombre}, Masa Molar: {self.masa_molar}, Densidad: {self.densidad}, Otros: {self.otros}"

    
    def iniciar_interaccion(cls):
        seguir = True
        while seguir:
            # Pide al usuario el símbolo del elemento
            simbolo = input("Introduce el símbolo del elemento (o escribe 'salir' para terminar): ")
            if simbolo.lower() == 'salir':
                seguir = False
                print("Saliendo del programa...")
            else:
                try:
                    elemento = cls(simbolo)
                    # Imprimir la información del elemento
                    print(elemento.toString())
                except ValueError as e:
                    print(e)
Elemento.iniciar_interaccion()
