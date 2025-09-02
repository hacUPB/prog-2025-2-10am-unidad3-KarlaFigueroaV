# Tarea Fibbonacci

num = int(input("Ingrese un número entero para generar la serie de Fibonacci: "))

# Validar el número ingresado
if num <= 0:
    print("Por favor, ingrese un número entero positivo.")
elif num == 1:
    print("Serie de Fibonacci:")
    print(0)
else:
    a, b = 0, 1
    print("Serie de Fibonacci:")
    print(a)
    print(b)

    contador = 2
    while contador < num:
        siguiente = a + b
        print(siguiente)
        a, b = b, siguiente
        contador += 1
