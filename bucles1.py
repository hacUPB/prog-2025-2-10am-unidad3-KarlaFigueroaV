# EJERCICIOS
## WHILE
'''
numero = 100
while numero >=0:
    print(numero)
    numero -= 5
'''

### Solicitar 2 números enteros al usuario e imprimir los pares


num1 = int(input ("Ingrese el primer numero"))
num2 = int(input ("Ingrese el segundo numero"))
if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1
'''
while menor <= mayor:
    if menor % 2 == 0:
        print (menor)
    num1 += 1
'''
if menor % 2 == 1:
    menor += 1
while menor <= mayor:
    print(menor)
    menor +=2