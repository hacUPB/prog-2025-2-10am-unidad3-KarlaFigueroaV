# RETO PYTHON
# Por: Karla Figueroa Velilla y Santiago Duarte Cueto
 
def limite_angulo():
    print("\n=== Simulación: Límite de ángulo de ataque ===")
    print("El ángulo límite seguro es 15°.")
    print("Si lo superas, el avión entra en pérdida.\n")
 
    angulo = float(input("Ingrese el ángulo inicial de ataque (°): "))
    limite = 15
    Cl0 = 0.4
    a_deg = 0.1
    t = 0
 
    while True:
        cl = Cl0 + a_deg * angulo
        print(f"\nÁngulo actual: {angulo}° - Coeficiente de sustentación (Cl): {cl:.2f}")
 
        if angulo > limite:
            print("¡Pérdida! El ángulo supera el límite.")
            break
 
        print("\nOpciones:")
        print("1. Aumentar ángulo (+1°)")
        print("2. Mantener ángulo")
        print("3. Ingresar nuevo valor de ángulo")
        print("4. Salir")
 
        opcion = input("Elige una opción: ")
        if opcion == "1":
            angulo += 1
        elif opcion == "2":
            print("Manteniendo el ángulo constante...")
        elif opcion == "3":
            angulo = float(input("Ingrese el nuevo ángulo (°): "))
        elif opcion == "4":
            print("Simulación finalizada.")
            break
        else:
            print("Opción no válida.")
 
        t += 1
        print(f"Tiempo de simulación: {t} segundos")
 
 
def peso_balance():
    print("\n=== Simulación: Peso y balance ===")
    peso_total = 0
    momento_total = 0
    limite_inferior = 10
    limite_superior = 20
    n = 0
 
    while True:
        print("\nOpciones de carga:")
        print("1. Pasajero")
        print("2. Carga")
        print("3. Combustible")
        print("4. Terminar")
        opcion = input("Selecciona: ")
 
        if opcion == "4":
            print("Simulación finalizada.")
            break
 
        masa_nueva = float(input("Ingrese el peso (kg): "))
        brazo_nuevo = float(input("Ingrese el brazo (m): "))
 
        peso_total += masa_nueva
        momento_total += masa_nueva * brazo_nuevo
        cg = momento_total / peso_total
        n += 1
 
        print(f"\nElemento agregado número: {n}")
        print(f"Peso total: {peso_total} kg")
        print(f"Centro de gravedad (CG): {cg:.2f} m")
 
        if limite_inferior <= cg <= limite_superior:
            print("Avión balanceado")
        else:
            print("¡Avión inestable!")
 
 
def plan_vuelo():
    print("\n=== Simulación: Plan de vuelo con reserva de combustible ===")
    consumo_ascenso = 5
    consumo_crucero = 3
    consumo_descenso = 2
    reserva_min = 30
    consumo_conservador = 3
    reserva_kg = reserva_min * consumo_conservador
 
    combustible_inicial = float(input("Ingrese el combustible inicial (kg): "))
    tiempo_vuelo = int(input("Ingrese la duración del vuelo (min): "))
 
    combustible = combustible_inicial
    minuto = 0
 
    while minuto < tiempo_vuelo:
        print("\nFases de vuelo:")
        print("1. Ascenso")
        print("2. Crucero")
        print("3. Descenso")
        fase = input("Seleccione fase: ")
 
        if fase == "1":
            consumo = consumo_ascenso
        elif fase == "2":
            consumo = consumo_crucero
        elif fase == "3":
            consumo = consumo_descenso
        else:
            print("Fase inválida, se usará consumo de crucero por defecto.")
            consumo = consumo_crucero
 
        combustible -= consumo
        minuto += 1
 
        print(f"Minuto: {minuto}, Combustible restante: {combustible:.2f} kg")
 
        if combustible <= 0:
            print("Emergencia: combustible agotado")
            return
 
    if combustible >= reserva_kg:
        print("Vuelo completado con reserva suficiente.")
    else:
        print("Vuelo completado sin reserva suficiente.")
 
 
# --- MENÚ PRINCIPAL ---
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Límite de ángulo de ataque")
    print("2. Peso y balance")
    print("3. Plan de vuelo con reserva de combustible")
    print("4. Salir")
 
    opcion = input("Selecciona una opción: ")
 
    if opcion == "1":
        limite_angulo()
    elif opcion == "2":
        peso_balance()
    elif opcion == "3":
        plan_vuelo()
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
 