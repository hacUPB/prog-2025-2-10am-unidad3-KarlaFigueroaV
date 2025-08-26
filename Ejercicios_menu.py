# Ejemplo de Menú con match-case

print("=== MENÚ PRINCIPAL ===")
print("1. Ver datos de sensores")
print("2. Configurar parámetros")
print("3. Salir")

opcion = int(input("Selecciona una opción: "))

match opcion:
    case 1:
        print("Mostrando datos de sensores...")
    case 2:
        print("Entrando a configuración...")
    case 3:
        print("Saliendo del programa...")
    case _:
        print("Opción inválida.")
