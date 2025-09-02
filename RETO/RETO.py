# RETO PYTHON
## Por: Karla Figueroa Velilla y Santiago Duarte Cueto

print("=== MENÚ PRINCIPAL ===")
print("1. Límite de ángulo de ataque")
print("2. Peso y balance")
print("3. Plan de vuelo con reserva de combustible")
print("4. Salir")

opcion = int(input("Selecciona una opción: "))

match opcion:
    case 1:
        print("Límite de ángulo de ataque")
    case 2:
        print("Peso y balance")
    case 3:
        print("Plan de vuelo con reserva de combustible")
    case 4:
        print("Saliendo del programa...")
    case _:
        print("Opción inválida.")
