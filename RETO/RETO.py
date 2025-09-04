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
        print("El ángulo límite seguro es 15°.")
        print("Si lo superas, el avión entra en pérdida.")

        angulo = float(input("Ingrese el ángulo inicial de ataque (°): "))
        limite = 15

        while True:
            print(f"Ángulo actual: {angulo}°")

        # Verificar si supera el límite

            if angulo > limite:
                print("Has superado el ángulo crítico. ¡El avión entra en pérdida")
                break

        # Menú de opciones
        print("¿Qué deseas hacer?")
        print("1. Aumentar el ángulo (+1°)")
        print("2. Mantener el ángulo")
        print("3. Salir de la simulación")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            angulo += 1
        elif opcion == "2":
            print("Manteniendo el ángulo constante...")
        elif opcion == "3":
            print("Simulación finalizada.")
break
        else:
            print("Opción no válida. Intenta de nuevo.")