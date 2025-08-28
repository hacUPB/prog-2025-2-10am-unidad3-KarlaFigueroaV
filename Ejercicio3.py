#Ejercicio 3
#Se le pide al usuario que ingrese un numero entero y que muestre un mensaje si el numero es divisible por 3.

numero = int(input("Ingrese un número:"))
residuo = numero % 3
#Si residuo es 0 es divisible entre 3
if residuo == 0:
    print(numero, "Divisible entre 3")


