from Compuesto import Compuesto
from Elemento import Elemento
def main():
    continuar = True  # Variable de control
    while continuar:
        compuesto_input = input("Introduce la fórmula del compuesto (o escribe 'salir' para terminar): ")
        if compuesto_input.lower() == 'salir':
            continuar = False  # Cambia el estado para salir del ciclo
            print("Saliendo del programa...")
        else:
            try:
                # Crear el objeto Compuesto usando la fórmula ingresada por el usuario
                compuesto = Compuesto(compuesto_input)
                # Calcular la masa molar del compuesto
                masa_molar = compuesto.masaMolar()
                print(f"La masa molar de {compuesto_input} es: {masa_molar:.2f} g/mol")
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    main()
