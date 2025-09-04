
num = int(input("Ingrese el número del que quiere generar la tabla de multiplicar"))

contador = 1
while contador <= 15:
    resultado = contador * num
    print(f"{num} x {contador} = {resultado}")
    contador += 1
