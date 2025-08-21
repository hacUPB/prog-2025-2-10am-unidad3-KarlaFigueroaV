print("Ingresa tu nombre y apellido")
nombre = input ()
print("Bienvenido: ")
print(nombre)
#Opción 2
print("Bienvenido: ", nombre)
#Calcular el IMC de esa persona
#Leer peso, altura
peso = input ("Ingresa tu peso en kg: ")
peso = float(peso)
altura = input ("Ingresa tu talla en metros: ")
altura = float(altura)
#Cálculos
imc = peso/altura**2
#Mostrar imc
print("Tu IMC = ", imc)
if 18.5 <= imc <= 24.9:
    print("Clasificación normal")
else:
    if 25 <= imc <= 29.9:
        print("Clasificación sobre peso")
    else :
        if 30 <= imc <= 34.9:
            print("Clasificación Obesidad I")
        else:
            if 35 <= imc <= 39.9:
                print("Clasificación Obesidad II")
            else:
                if imc >= 40:
                    print("Clasificación Obesidad Extrema III")
                    