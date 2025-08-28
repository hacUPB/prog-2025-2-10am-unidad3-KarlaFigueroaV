# RETO PYTHON
## Por: Karla Figueroa Velilla y Santiago Duarte Cueto

print("=== MENÚ PRINCIPAL ===")
print("1. Problema 1")
print("2. Problema 2")
print("3. Problema 3")
print("4. Salir")

opcion = int(input("Selecciona una opción: "))

match opcion:
    case 1:
        print("Problema 1")
    case 2:
        print("Problema 2")
    case 3:
        print("Problema 3")
    case 4:
        print("Saliendo del programa...")
    case _:
        print("Opción inválida.")
