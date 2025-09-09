'''
Crear una función llamada menu()
Parámetros de entrada : Ninguno
Lo que realiza: Muestra un menú y pide al usuario que seleccione una opción.
Valor de retorno: la opción seleccionada 
'''
def menu ():
    print("1. Entradas\n2. Platos fuertes\n3. Bebidas\n4. Postres\n5. Salir")
    opcion = int(input("Elija una opción: "))
    return opcion

def entradas():
    print("1. Ceviche\t\t$18000")
    print("2. Chips de Platano\t\t$10000")

def fuertes():
    print("1. Arroz de Camarón\t\t$40000")
    print("2. Cazuela de Mariscos\t\t$35000")

def bebidas():
    print("1. Jugo de corozo\t\t$7000")
    print("2. Coca Cola\t\t$5000")

def postres():
    print("1. Brownie con Helado\t\t$15000")
    print("2. Postre de Milo\t\t$20000")


# Función principal
def main():  
    eleccion = menu()
    print(eleccion)

    match(eleccion):
        case 1:
            entradas()
        case 2:
            fuertes()
        case 3:
            bebidas()
        case 4:
            postres()
        case _:
            print("Opción no válida")

# Aquí se llama a la función principal 
if __name__ == "__main__":
    main()