'''
Variables de entrada    
Nombre                  tipo  
Opción                  str
temperatura             float / punto flotante
 
Variables de salida
Nombre                  Tipo
conversion              float / punto flotante
 
Variable de control
opcion                  
'''
 
opcion = 'L'                #Asigno un valor diferente de Q
while opcion != 'Q':
    opcion = input("F. Fahrenheit a Celsius\n  C. Celsius a Faharenheit\n Q. Salir\n")
    opcion = opcion.upper()
    if opcion != 'Q':
        temperatura = float(input("Ingrese la tempreatura a convertir: "))
        match opcion:
            case 'F':
                conversion = (temperatura - 32) *(5/9)
                print(f"{temperatura}°F = {conversion}°c")
            case 'C':
                conversion = (temperatura * 9/5) + 32
            case _:
                print("Opción no válida")

    else:
        print("Saliendo del programa...")

    
