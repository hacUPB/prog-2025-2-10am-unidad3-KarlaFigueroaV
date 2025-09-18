import Modulo_funciones
#Función principal
numero = int(input("Ingrese un número entero mayor que 1: "))
Modulo_funciones.primo(numero)
'''
variable = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
Modulo_funciones.fibonacci(variable)
multiplicando = int(input("Ingrese el número entero: "))
Modulo_funciones.tabla(multiplicando)
'''
from Modulo_funciones import *

def main():
    while True:
        opc = menu()
        match opc:
            case 1:
                print("Calcula si un número es primo. ")
                valor = int(input("Ingresa un entero mayor que 1 >> "))
                primo(valor)
            case 2:
                print("Imprime la serie de fibonacci. ")
                num = int(input("Ingresa el número de términos >> "))
                fibonacci(num)
            case 3:
                print("Imprime la tabla de multiplicar. ")
                num = int(input("Ingresa el número >> "))
                tabla(num)
            case 4:
                break
            case _:
                print("La opción no es válida")


if __name__ == "__main__":
    main()

