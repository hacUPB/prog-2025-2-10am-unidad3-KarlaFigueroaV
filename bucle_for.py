'''
for cont in range(-20, 0, 1):               
    print(cont)


num = int(input("Ingrese un número positvo"))
while num < 0:
    num = int(input("Ingrese un número positvo"))
acum = 0
for cont in range(1, num+1):
    if cont % 2 == 0:
        acum += cont
print(f"La suma de los pares es: {acum}")
'''

mensaje = "Universidad pontificia Bolivariana"
num = int(input("Ingrese un número positvo: "))
# imprimir el mensaje un número de veces
for cont in range(0, num, 1):
    print(mensaje)
