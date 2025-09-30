'''
Variable de entrada
numero       int

Variable de salida
divisores
'''

numero = int(input("Ingrese un número entero mayor que 1: "))
cont = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        cont += 1

if cont == 2:
    print(f"{numero} es primo")
else:
    print(f"Los divisores de {numero} son: ")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)